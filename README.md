# Gemini Video Tools

Simple, focused tools for sending video to **Gemini 2.5** and **Gemini 3.0** models as input data.

> **Note**: This is a streamlined MVP derived from the [Google Gemini Cookbook](https://github.com/google-gemini/cookbook), focusing specifically on video input capabilities.

## 🎯 What This Does

This repository provides:
- ✅ Quick-start examples for video understanding with Gemini
- ✅ Support for Gemini 2.5 Flash, 2.5 Pro, and 3.0 Pro Preview
- ✅ Simple Python scripts and Jupyter notebooks
- ✅ Video upload, analysis, and summarization examples

## 🚀 Quick Start

### Prerequisites

1. **Python 3.10+**
2. **Google AI API Key** - Get one at [Google AI Studio](https://aistudio.google.com/app/apikey)

### Installation

```bash
# Clone this repository
git clone https://github.com/filiksyos/gemini-video-tools.git
cd gemini-video-tools

# Install dependencies
pip install -r requirements.txt

# Set your API key
export GOOGLE_API_KEY='your-api-key-here'
```

### Basic Usage

```python
from google import genai
from google.genai import types
import time

# Initialize client
client = genai.Client(api_key='YOUR_API_KEY')

# Upload video
video_file = client.files.upload(file='path/to/your/video.mp4')

# Wait for processing
while video_file.state.name == "PROCESSING":
    print('Processing video...')
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# Analyze video with Gemini
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        'Summarize this video in 2-3 sentences.',
        video_file
    ]
)

print(response.text)
```

## 📚 Examples

### 1. Video Understanding Quickstart
**Location**: `quickstarts/Video_understanding.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/filiksyos/gemini-video-tools/blob/main/quickstarts/Video_understanding.ipynb)

Comprehensive guide covering:
- Video upload and processing
- Scene detection and captioning
- Text extraction from videos
- Screen recording analysis
- YouTube video analysis
- Custom FPS and time offsets

### 2. Video Summarization
**Location**: `examples/Analyze_a_Video_Summarization.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/filiksyos/gemini-video-tools/blob/main/examples/Analyze_a_Video_Summarization.ipynb)

Focused example on:
- Uploading longer videos
- Generating concise summaries
- Using system instructions

### 3. Simple Python Script
**Location**: `simple_video_upload.py`

Minimal working example for quick testing.

## 🎥 Supported Models

| Model | Best For | Speed | Context Window |
|-------|----------|-------|----------------|
| **gemini-2.5-flash** | General video analysis | Fast | 1M tokens |
| **gemini-2.5-pro** | Complex reasoning | Moderate | 2M tokens |
| **gemini-3-pro-preview** | Latest capabilities | Moderate | 2M tokens |

## 📖 Key Features Explained

### Video Upload
Videos are uploaded via the File API and processed server-side:
- Supports MP4, AVI, MOV, WebM formats
- Maximum file size: 2GB
- Processing extracts 1 FPS by default (customizable)

### Time-Based Analysis
You can specify exact time ranges:
```python
from google.genai import types

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part(
            file_data=types.FileData(file_uri=video_file.uri),
            video_metadata=types.VideoMetadata(
                start_offset='60s',  # Start at 1 minute
                end_offset='120s',   # End at 2 minutes
                fps=24               # Analyze 24 frames/second
            )
        ),
        'What happens in this clip?'
    ]
)
```

### YouTube Videos
Direct YouTube analysis (no download required):
```python
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part(
            file_data=types.FileData(
                file_uri='https://www.youtube.com/watch?v=VIDEO_ID'
            )
        ),
        'Summarize this video.'
    ]
)
```

## ⚙️ Advanced Options

### Custom Frame Rate
Control how many frames per second are analyzed:
- **Lower FPS (0.5-1)**: Lectures, interviews, static content
- **Higher FPS (8-24)**: Action scenes, sports, fast-paced content

### System Instructions
Guide the model's behavior:
```python
config = types.GenerateContentConfig(
    system_instruction="You are a film critic. Provide detailed scene analysis."
)
```

## 🔧 Troubleshooting

### Common Issues

**Video processing fails**
- Check file format is supported (MP4, WebM, AVI, MOV)
- Ensure file size is under 2GB
- Wait longer for processing (large files take time)

**API key errors**
- Verify key is valid at [Google AI Studio](https://aistudio.google.com/app/apikey)
- Check environment variable is set: `echo $GOOGLE_API_KEY`

**Out of tokens**
- Use shorter videos or lower FPS
- Specify time ranges instead of full video

## 📦 Dependencies

- `google-genai>=1.16.0` - Official Google Generative AI SDK
- `pillow` - Image processing
- `opencv-python` - Video handling
- `matplotlib` - Visualization

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

Apache License 2.0 - See [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

This project is based on the [Google Gemini Cookbook](https://github.com/google-gemini/cookbook). All credit for the original examples goes to the Google Gemini team.

## 🔗 Resources

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Full Gemini Cookbook](https://github.com/google-gemini/cookbook)
- [Video Understanding Guide](https://ai.google.dev/gemini-api/docs/video-understanding)

---

**Have questions?** Check the [Google AI Developer Forum](https://discuss.ai.google.dev/).