#!/usr/bin/env python3
"""
Simple video upload and analysis example for Gemini.

Usage:
    python simple_video_upload.py path/to/video.mp4 "Your question about the video"

Example:
    python simple_video_upload.py demo.mp4 "What happens in this video?"
"""

import os
import sys
import time
from google import genai
from google.genai import types


def analyze_video(video_path: str, prompt: str, model_id: str = "gemini-2.5-flash"):
    """
    Upload a video to Gemini and analyze it.
    
    Args:
        video_path: Path to the video file
        prompt: Question or instruction for the model
        model_id: Gemini model to use (default: gemini-2.5-flash)
    
    Returns:
        str: Model's response text
    """
    # Get API key from environment
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY environment variable not set.\n"
            "Get your API key at: https://aistudio.google.com/app/apikey\n"
            "Then set it: export GOOGLE_API_KEY='your-key-here'"
        )
    
    # Initialize client
    print(f"🔧 Initializing Gemini client...")
    client = genai.Client(api_key=api_key)
    
    # Upload video
    print(f"📤 Uploading video: {video_path}")
    video_file = client.files.upload(file=video_path)
    print(f"✅ Upload complete: {video_file.name}")
    
    # Wait for processing
    print("⏳ Processing video...")
    while video_file.state.name == "PROCESSING":
        print("   Still processing...")
        time.sleep(5)
        video_file = client.files.get(name=video_file.name)
    
    if video_file.state.name == "FAILED":
        raise RuntimeError(f"Video processing failed: {video_file.state}")
    
    print(f"✅ Video ready for analysis")
    
    # Generate response
    print(f"🤖 Analyzing with {model_id}...")
    response = client.models.generate_content(
        model=model_id,
        contents=[
            prompt,
            video_file
        ]
    )
    
    # Clean up
    print("🗑️  Deleting uploaded file...")
    client.files.delete(name=video_file.name)
    
    return response.text


def main():
    """Main entry point for CLI usage."""
    if len(sys.argv) < 3:
        print("Usage: python simple_video_upload.py <video_path> <prompt>")
        print("\nExample:")
        print('  python simple_video_upload.py video.mp4 "Summarize this video"')
        sys.exit(1)
    
    video_path = sys.argv[1]
    prompt = sys.argv[2]
    
    # Optional: specify model as third argument
    model_id = sys.argv[3] if len(sys.argv) > 3 else "gemini-2.5-flash"
    
    if not os.path.exists(video_path):
        print(f"❌ Error: Video file not found: {video_path}")
        sys.exit(1)
    
    print("="*60)
    print("🎥 Gemini Video Analysis Tool")
    print("="*60)
    print()
    
    try:
        result = analyze_video(video_path, prompt, model_id)
        print()
        print("="*60)
        print("📋 RESULT:")
        print("="*60)
        print(result)
        print()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()