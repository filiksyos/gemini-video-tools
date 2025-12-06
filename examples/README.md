# Video Analysis Examples

This directory contains practical examples of using Gemini for video understanding.

## 📁 Examples

### Analyze_a_Video_Summarization.ipynb

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/filiksyos/gemini-video-tools/blob/main/examples/Analyze_a_Video_Summarization.ipynb)

**What it demonstrates:**
- Uploading and processing a longer video file
- Using system instructions to guide summarization
- Generating concise 2-3 sentence summaries
- Proper file cleanup after analysis

**Use cases:**
- Quick video content review
- Meeting recording summaries
- Educational content overview
- Content moderation pre-screening

## 🎯 Running Examples

### Option 1: Google Colab (Recommended)
Click the Colab badge above each notebook - runs in browser, no setup needed.

### Option 2: Local Jupyter
```bash
# Install Jupyter if needed
pip install jupyter

# Start Jupyter
jupyter notebook

# Navigate to examples/ and open the notebook
```

### Option 3: VS Code
Install the Jupyter extension for VS Code and open the .ipynb files directly.

## 💡 Tips

1. **Start with small videos** - Test with 30-60 second clips first
2. **Use system instructions** - Guide the model's analysis style
3. **Experiment with prompts** - Different questions yield different insights
4. **Check FPS settings** - Adjust based on your video content type

## 🔗 More Examples

For advanced examples including:
- YouTube video analysis
- Custom time ranges
- Multi-video comparison
- Real-time video streaming

Check the [full Gemini Cookbook](https://github.com/google-gemini/cookbook/tree/main/examples/).