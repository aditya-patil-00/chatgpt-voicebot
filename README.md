# Personal Voice Bot

A conversational AI assistant that responds as if it were you! This Streamlit application combines voice and text input with a personalized AI personality based on your background, experiences, and communication style.

## Features

- **🎤 Voice Input**: Record your questions using the built-in audio recorder
- **📝 Text Input**: Type your questions directly
- **🤖 Personalized Responses**: AI responds as if it were you, drawing from your background
- **🔊 Text-to-Speech**: Responses are automatically spoken back to you
- **☁️ Cloud-Ready**: Robust deployment with fallback speech recognition
- **💬 Natural Conversations**: Authentic, conversational responses based on your personality

## Quick Start

### Prerequisites

- Python 3.8 or higher
- DeepInfra API key (for AI responses)
- Microphone access (for voice input)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd chatgpt-voicebot
   ```

2. **Install dependencies**
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

## Deployment

### Streamlit Cloud Deployment

This application is optimized for Streamlit Cloud deployment with the following features:

- **Graceful Fallback**: If local speech recognition fails, automatically uses OpenAI Whisper
- **System Dependencies**: Includes `packages.txt` for audio processing libraries
- **Error Handling**: Robust error handling for cloud environments

#### Deployment Steps:

1. **Push to GitHub**: Ensure your code is in a public GitHub repository
2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Add your `DEEPINFRA_API_KEY` in the secrets section
   - Deploy!

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DEEPINFRA_API_KEY` | Your DeepInfra API key for AI responses | Yes |

## Technical Details

### Speech Recognition

The application uses a dual approach for speech recognition:

1. **Local Recognition**: Uses `speech_recognition` library with Google's speech API
2. **Cloud Fallback**: Automatically falls back to OpenAI Whisper when local recognition fails

### AI Model

- **Model**: Meta Llama-4-Maverick-17B-128E-Instruct-FP8
- **Provider**: DeepInfra
- **Features**: Personalized responses based on your background

### Audio Processing

- **Format**: WAV (16kHz, mono)
- **Processing**: PyDub for audio conversion
- **Playback**: Browser-based text-to-speech

## Project Structure

```
chatgpt-voicebot/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── packages.txt          # System dependencies
├── README.md             # This file
└── .streamlit/
    └── secrets.toml      # API keys (create this)
```

## Configuration

### Personalizing the AI

To customize the AI's personality, edit the system prompt in `app.py`. The current configuration includes:

- Professional background and experience
- Personality traits and communication style
- Values and work philosophy
- Response guidelines

### Speech Recognition Settings

- **Sample Rate**: 16kHz
- **Channels**: Mono
- **Format**: WAV
- **Fallback**: OpenAI Whisper API

## Troubleshooting

### Common Issues

#### Speech Recognition Not Working
- **Local Development**: Ensure microphone permissions are granted
- **Cloud Deployment**: The app automatically falls back to Whisper API
- **Dependencies**: Check that `packages.txt` is included in your repository

#### API Key Issues
- Verify your DeepInfra API key is correct
- Ensure sufficient balance in your DeepInfra account
- Check the key is properly set in Streamlit secrets

#### Audio Recording Problems
- Grant microphone permissions to your browser
- Try refreshing the page
- Check if your microphone is working in other applications

### Error Messages

| Error | Solution |
|-------|----------|
| "Insufficient Balance" | Add funds to your DeepInfra account |
| "Speech recognition not available" | The app will use Whisper fallback |
| "Could not understand audio" | Speak more clearly or try again |

## Usage Statistics

The application displays token usage for each conversation:
- **Prompt Tokens**: Tokens used in the input
- **Completion Tokens**: Tokens used in the response
- **Total Cost**: Based on DeepInfra's pricing

## Privacy & Security

- **Audio Processing**: Audio is processed locally when possible
- **API Calls**: Only transcribed text is sent to AI services
- **No Storage**: Audio recordings are not stored permanently
- **Secure**: API keys are stored in Streamlit secrets

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io) for the web framework
- [DeepInfra](https://deepinfra.com) for AI model hosting
- [OpenAI](https://openai.com) for Whisper speech recognition
- [PyDub](https://pydub.com) for audio processing

## Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Review the error messages in the application
3. Ensure all dependencies are properly installed
4. Verify your API keys and account balance

---

**Happy chatting! 🎉**