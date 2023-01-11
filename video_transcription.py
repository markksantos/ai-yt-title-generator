from youtube_transcript_api import YouTubeTranscriptApi
import openai

# set the OpenAI API key
openai.api_key = "API HERE"

# replace this with the YouTube video ID
video_id = 'VIDEO_ID_HERE'

prompt_input = "create title ideas based on this transcript: "

# fetch the transcript of the YouTube video
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# create a string with the transcript text
transcript_text = ' '.join([x['text'] for x in transcript])

# the number of tokens that can be handled by the model
max_tokens = 4096

# go through the transcript text
i = 0
while i < len(transcript_text):
    # take a chunk of the transcript text
    chunk = transcript_text[i:min(i + max_tokens, len(transcript_text))]
    #print(f'Transcript text: {chunk}')
    # Use GPT-3 to analyze the transcript and identify sections that could be turned into short videos
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{prompt_input} {chunk}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the text of the most likely completion
    message = completions.choices[0].text
    print("Generating title ideas here:", message)

    # go through the transcript to find the timestamp of the sections
    for tr in transcript[i:]:
        if tr['text'] in message:
            print(f"Timestamp: {tr['start']} - {tr['start'] + tr['duration']}")
    i += max_tokens
