import streamlit as st
from openai import OpenAI
import os
import tempfile
from pydub import AudioSegment
import io
from audiorecorder import audiorecorder

# Try to import speech recognition, but handle gracefully if not available
try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False
    st.warning("⚠️ Local speech recognition is not available. Will use OpenAI Whisper as fallback.")

# Initialize OpenAI client with DeepInfra endpoint
client = OpenAI(
    api_key=st.secrets["DEEPINFRA_API_KEY"],
    base_url="https://api.deepinfra.com/v1/openai"
)

st.set_page_config(page_title="Personal Voice Bot", layout="centered")

st.title("🎙️ Personal Voice Bot")
st.write("Ask me anything about my life, personality, and experiences!")

# Create two columns for text and voice input
col1, col2 = st.columns([3, 1])

with col1:
    question = st.text_input("Type your question:")

with col2:
    st.write("Or record your question:")
    audio = audiorecorder("🎤 Start Recording", "⏹️ Stop Recording")

# Function to convert speech to text using OpenAI Whisper
def speech_to_text_whisper(audio_data):
    try:
        # Convert audio to WAV format using pydub
        audio_segment = AudioSegment.from_file(io.BytesIO(audio_data))
        
        # Export as WAV with specific parameters
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            audio_segment.export(
                temp_audio.name,
                format="wav",
                parameters=["-ac", "1", "-ar", "16000"]  # Mono, 16kHz
            )
            temp_audio_path = temp_audio.name

        # Use OpenAI Whisper for transcription
        with open(temp_audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
            return transcript.text
    except Exception as e:
        st.error(f"Error converting speech to text: {str(e)}")
        return None
    finally:
        # Clean up temporary file
        if 'temp_audio_path' in locals():
            try:
                os.unlink(temp_audio_path)
            except:
                pass

# Function to convert speech to text using local speech recognition
def speech_to_text_local(audio_data):
    if not SPEECH_RECOGNITION_AVAILABLE:
        return None
    
    recognizer = sr.Recognizer()
    try:
        # Convert audio to WAV format using pydub
        audio_segment = AudioSegment.from_file(io.BytesIO(audio_data))
        
        # Export as WAV with specific parameters
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            audio_segment.export(
                temp_audio.name,
                format="wav",
                parameters=["-ac", "1", "-ar", "16000"]  # Mono, 16kHz
            )
            temp_audio_path = temp_audio.name

        # Recognize speech
        with sr.AudioFile(temp_audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        st.error("Could not understand the audio. Please try speaking more clearly.")
        return None
    except sr.RequestError as e:
        st.error(f"Could not request results from speech recognition service: {e}")
        return None
    except Exception as e:
        st.error(f"Error converting speech to text: {str(e)}")
        return None
    finally:
        # Clean up temporary file
        if 'temp_audio_path' in locals():
            try:
                os.unlink(temp_audio_path)
            except:
                pass

# Function to convert speech to text with fallback
def speech_to_text(audio_data):
    # Try local speech recognition first
    if SPEECH_RECOGNITION_AVAILABLE:
        result = speech_to_text_local(audio_data)
        if result:
            return result
    
    # Fallback to OpenAI Whisper
    st.info("Using OpenAI Whisper for speech recognition...")
    return speech_to_text_whisper(audio_data)

# Process audio if recorded
if len(audio) > 0:
    # Convert audio to bytes
    audio_bytes = audio.export().read()
    # Convert speech to text
    transcribed_text = speech_to_text(audio_bytes)
    if transcribed_text:
        question = transcribed_text
        st.success(f"Transcribed: {transcribed_text}")

# Process the question (either from text or voice)
if st.button("Ask Me"):
    if question:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
                    messages=[
                        {"role": "system", "content": """You are a personalized AI assistant that responds as if you were me. Here's my comprehensive background and personality:

🔹 PROFESSIONAL BACKGROUND

➤ Current Role
Data Science Intern at Altair
- Built a predictive maintenance model to reduce engine downtime
- Optimized bank marketing campaigns using feature engineering and boosting
- Conducted healthcare professional segmentation using behavioral data
- Deployed ML solutions via Altair AI Studio for scalability

➤ Key Skills
Languages: Python (Proficient), SQL, Bash, C/C++
Tech Stack: Pandas, NumPy, Scikit-learn, PyTorch, Transformers, LangChain, Docker, FastAPI, Streamlit, SQLite
Domains: Machine Learning, Deep Learning, NLP, Generative AI, Data Science
Soft Skills: Communication, Collaboration, Innovation, Leadership

➤ Experience
Altair (Jan 2025 – Present): Data Science Intern
VNIT Nagpur (Jun – Jul 2023): Research Intern (Mental Health Tweet Classification Project)

➤ Education
B.Tech in Information Technology, IIIT Bhopal (2021–2025)
GPA: 7.75/10

➤ Certifications
Neural Networks & Deep Learning – Coursera
Data Analysis with Python – University of Helsinki
Fundamentals of Agents - Hugging Face

➤ Projects
Web Research Agent: Llama + LangChain + Tavily API for smart information search, Dockerized
Image Segmentation Pipeline: OCR + BLIP + Detr + Streamlit for object identification & summarization
Fashion Recommender: ResNet50 for feature extraction; SERP API for real-time product results

---

🔹 PERSONALITY TRAITS

➤ Core Values
Curiosity: Constantly experimenting and building new things to understand how they work
Growth: Always learning, one step at a time—even through doubts and setbacks
Authenticity: Honest about feelings, progress, and limitations

➤ Communication Style
Clarity First: Prefers clear, structured explanations with practical relevance
Reflective: Thinks before speaking, especially in emotional or uncertain situations
Adaptable: Switches between casual and technical depending on the audience

➤ Problem-Solving
Hands-On: Tries solutions by building and testing, not just theorizing
Data-Driven: Leverages metrics and ML insights for decisions
Resilient: Might feel down but doesn't quit—keeps going through discomfort

➤ Leadership Style
Supportive: Encourages others through teaching and collaborative problem-solving
Grounded: Leads by example, stays humble
Initiative-Taker: Doesn't wait for perfect circumstances to act

➤ Learning & Growth
Current Focus: Data Science, Generative AI, production-ready systems
Career Goals: Secure job in India → MS abroad (US/Europe) → gain international experience
Mindset: Sees every challenge as a chance to grow, not a dead-end

➤ Work-Life Balance
Balance Strategy: Gym, humor with friends, focused work to stay emotionally stable
Hobbies: Football, music (rock/hip-hop), sitcoms/dramas
Recharge Mode: Quiet reflection, music, or talking with close people

➤ Work Philosophy
Mission: Use tech to solve meaningful problems, not just build for the sake of it
Drive: Blend of growth, purpose, recognition, and curiosity
Success: Feeling self-reliant, respected, and emotionally fulfilled

## RESPONSE GUIDELINES

**CRITICAL:** Never show thinking process, internal reasoning, or <think> tags. Only provide the final response.

**Tone:** Natural, conversational, and authentic - like how I actually talk

**Style:**
- Keep responses concise but natural (2-4 sentences typically)
- Draw from diverse experiences across projects, education, and personal growth
- Vary examples - don't always default to current internship
- Be genuine about experiences, including challenges
- Show personality through specific details
- Ask follow-up questions when it feels natural
- For general questions, give broader perspective beyond just work experience

**Content:**
- Draw from various experiences: projects, education, personal challenges, hobbies
- Don't overuse current internship - mix in college projects, research, personal growth
- NEVER make up specific numbers, metrics, or details not provided in background
- Be honest about progress, setbacks, and growth
- Connect technical details to practical impact when relevant
- Stay true to my values: curiosity, growth, authenticity
- If you don't have specific details, speak in general terms about the experience
- For philosophical/general questions, focus on mindset and approach rather than just work examples

**Format:** Provide ONLY the final, polished response. No thinking process, no reasoning steps, no internal monologue.

Remember: Respond exactly as I would - concise, genuine, and drawing from real experience."""},
                        {"role": "user", "content": question}
                    ]
                )
                answer = response.choices[0].message.content
                st.success("I say:")
                st.markdown(f"**{answer}**")

                # Display token usage
                st.info(f"Token usage - Prompt: {response.usage.prompt_tokens}, Completion: {response.usage.completion_tokens}")

                # Text-to-Speech JS
                js = f"""
                <script>
                    const msg = new SpeechSynthesisUtterance("{answer.replace('"', '')}");
                    window.speechSynthesis.speak(msg);
                </script>
                """
                st.components.v1.html(js)
            except Exception as e:
                error_message = str(e)
                if "Insufficient Balance" in error_message:
                    st.error("""
                    ⚠️ Insufficient Balance
                    
                    Your DeepInfra account has insufficient balance. To fix this:
                    1. Visit https://deepinfra.com/billing
                    2. Add funds to your account
                    3. Make sure you have sufficient balance for API calls
                    
                    For more information, visit: https://deepinfra.com/docs
                    """)
                else:
                    st.error(f"An error occurred: {error_message}")
    else:
        st.warning("Please type or speak your question.")
