# Personal Voice Bot

A personalized AI voice bot that responds as you would, using your resume and personality traits. Built with Streamlit and powered by DeepInfra's API.

## Features

- **Voice Input**: Record questions using your microphone
- **Text Input**: Type questions directly
- **Personalized Responses**: AI responds as if it were you, based on your background
- **Text-to-Speech**: Hear responses spoken aloud
- **Real-time Transcription**: Automatic speech-to-text conversion
- **User-Friendly Interface**: Simple, intuitive design for non-technical users

## Quick Start

### Prerequisites

- Python 3.8 or higher
- DeepInfra API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd chatgpt-voicebot
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Create a `.streamlit/secrets.toml` file:
   ```toml
   DEEPINFRA_API_KEY = "your-deepinfra-api-key-here"
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🎯 How to Use

1. **Access the app**: Open your browser and go to `http://localhost:8501`

2. **Ask questions**: You can either:
   - Type your question in the text input field
   - Click "🎤 Start Recording" to record your voice
   - Click "⏹️ Stop Recording" when done

3. **Get responses**: Click "Ask Me" to receive a personalized response

4. **Listen**: The response will be read aloud automatically

## Customization

### Personalizing the Bot

To make the bot respond as you, update the system prompt in `app.py` with your:

- **Professional Background**: Current role, skills, experience
- **Personality Traits**: Communication style, values, approach to work
- **Personal Experiences**: Projects, achievements, learning journey
- **Response Guidelines**: How you typically communicate

### Example System Prompt Structure

```python
{"role": "system", "content": """
You are a personalized AI assistant that responds as if you were me.

PROFESSIONAL BACKGROUND:
- Current Role: [Your position]
- Key Skills: [Your skills]
- Experience: [Your work history]

PERSONALITY TRAITS:
- Communication Style: [How you talk]
- Values: [What matters to you]
- Approach: [How you handle situations]

RESPONSE GUIDELINES:
- Keep responses concise and authentic
- Use real examples from your background
- Maintain your personality and tone
"""}
```

## Technical Details

### Architecture

- **Frontend**: Streamlit web interface
- **Audio Processing**: `streamlit-audiorecorder` for voice input
- **Speech Recognition**: Google Speech Recognition API
- **AI Model**: DeepInfra's Llama-4-Maverick-17B model
- **Text-to-Speech**: Browser's built-in speech synthesis

### Key Components

- `app.py`: Main application file
- `requirements.txt`: Python dependencies
- `.streamlit/secrets.toml`: API key configuration

### Dependencies

- `streamlit`: Web framework
- `openai`: API client for DeepInfra
- `streamlit-audiorecorder`: Voice recording component
- `SpeechRecognition`: Speech-to-text conversion
- `pydub`: Audio processing
- `requests`: HTTP requests

## Deployment

### Local Development
```bash
streamlit run app.py
```

### Cloud Deployment

**Streamlit Cloud:**
1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your API key in the secrets management
4. Deploy

**Other Platforms:**
- Heroku
- Railway
- DigitalOcean App Platform

## Security

- API keys are stored in Streamlit secrets
- No sensitive data is logged or stored
- Audio is processed locally and not saved

## Troubleshooting

### Common Issues

1. **"No module named 'audiorecorder'"**
   ```bash
   pip install streamlit-audiorecorder
   ```

2. **Audio recording not working**
   - Check microphone permissions
   - Use HTTPS or localhost (required for microphone access)

3. **API errors**
   - Verify your DeepInfra API key
   - Check your account balance
   - Ensure the model is available

4. **Speech recognition issues**
   - Check internet connection
   - Ensure clear audio input
   - Try shorter recordings

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

For issues and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the Streamlit documentation

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [DeepInfra](https://deepinfra.com/) for the AI model
- [streamlit-audiorecorder](https://github.com/theevann/streamlit-audiorecorder) for voice recording
- Google Speech Recognition for transcription

---

**Note**: This bot is designed to respond as you would based on your provided background and personality traits. Make sure to customize the system prompt with your authentic information for the best results.