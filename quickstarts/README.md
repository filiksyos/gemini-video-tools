# Video Understanding Quickstarts

Comprehensive guides to get started with Gemini video capabilities.

## 📘 Quickstart Guide

### Video_understanding.ipynb

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/filiksyos/gemini-video-tools/blob/main/quickstarts/Video_understanding.ipynb)

**Complete tutorial covering:**

1. **Basic Setup**
   - API key configuration
   - SDK initialization
   - Model selection (2.5 Flash, 2.5 Pro, 3.0 Pro)

2. **Video Upload & Processing**
   - File API usage
   - Upload status monitoring
   - Processing state handling

3. **Search Within Videos**
   - Scene detection
   - Object identification
   - Timestamp-based results

4. **Text Extraction**
   - Reading on-screen text
   - Organizing extracted content
   - Table generation from notes

5. **Structured Analysis**
   - Product catalogs from videos
   - Pricing and dimension extraction
   - Real-world object understanding

6. **Screen Recording Analysis**
   - UI/UX testing
   - User study insights
   - Action logging with timestamps

7. **YouTube Video Analysis**
   - Direct URL support
   - No download required
   - Public video search

8. **Advanced Preprocessing**
   - Time-based clipping
   - Custom FPS (frames per second)
   - Targeted scene analysis

## 🎓 Learning Path

### For Beginners
1. Start with **Video_understanding.ipynb** sections 1-3
2. Try the examples with your own short videos
3. Experiment with different prompts

### For Intermediate Users
1. Explore time-based clipping (section 8)
2. Try YouTube video analysis (section 7)
3. Customize FPS for your use case

### For Advanced Users
1. Combine multiple features
2. Build custom preprocessing pipelines
3. Integrate with your applications

## 🚀 Quick Start Commands

```bash
# Open in Colab
# Click the badge above

# Run locally
jupyter notebook Video_understanding.ipynb

# Convert to Python script
jupyter nbconvert --to python Video_understanding.ipynb
```

## 📊 Example Outputs

### Scene Detection
```json
[
  {
    "time": "00:15-00:30",
    "description": "Product demonstration showing...",
    "objects": ["laptop", "phone", "desk"]
  }
]
```

### Text Extraction
```markdown
| Item | Price | Dimensions |
|------|-------|------------|
| Mug  | $12   | 4"h x 3"d  |
```

## 🔧 Customization Options

### Time Ranges
```python
video_metadata=types.VideoMetadata(
    start_offset='60s',   # Start at 1 minute
    end_offset='120s'     # End at 2 minutes
)
```

### Frame Rate
```python
video_metadata=types.VideoMetadata(
    fps=24  # Analyze 24 frames per second
)
```

### System Instructions
```python
config=types.GenerateContentConfig(
    system_instruction="Focus on technical details"
)
```

## 🆘 Troubleshooting

**Notebook won't run?**
- Use Colab (recommended) - zero setup required
- Check Python version (3.10+ required)
- Install missing packages: `pip install -r ../requirements.txt`

**Video upload fails?**
- Check file format (MP4, WebM, AVI, MOV)
- Verify file size is under 2GB
- Ensure stable internet connection

**Out of API quota?**
- Check usage at [Google AI Studio](https://aistudio.google.com/)
- Consider upgrading to paid tier
- Use lower FPS or shorter clips

## 🔗 Additional Resources

- [Gemini API Docs](https://ai.google.dev/gemini-api/docs/video-understanding)
- [Google AI Studio](https://aistudio.google.com/)
- [Developer Forum](https://discuss.ai.google.dev/)
- [Full Cookbook](https://github.com/google-gemini/cookbook)