# YouTube Video Transcript Titling :movie_camera: 

This script utilizes the YouTube Transcript API to fetch the transcript of a given YouTube video, and the OpenAI API to analyze the transcript and generate title ideas for sections of the video. The OpenAI API key is required to use this script.

## Usage
1. Replace `video_id` with the YouTube video ID.
2. Set the `openai.api_key` to your own OpenAI API key.
3. Run the script.
4. The script will output the title ideas for different section of videos, along with the timestamp of the section in the video.

## Dependencies
- `youtube_transcript_api`
- `openai`

You can install these using `pip install youtube_transcript_api openai`

## Customization
- The `prompt_input` can be changed to adjust the prompt for the OpenAI API.
- The `max_tokens` can be adjusted to handle transcripts of different lengths.
- `engine`, `max_tokens`, `n`, `stop`, and `temperature` can also be adjusted in the `openai.Completion.create()` function to fine-tune the results.
