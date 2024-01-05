from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
import json
import os
from openai import OpenAI
from dotenv import load_dotenv  


load_dotenv()  # Load environment variables from .env file
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.getenv('OPENAI_API_KEY1')
)

#YoutubeTranScript API get_transcript      
def get_transcript(url):   
    print("Url:",url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Print the transcript
    title=soup.title.text
    print("Title:",title)
    # script = soup.find('script', type='application/ld+json')
    # print("Script::",script)
    # data = json.loads(script.text)
    # print("Data::",data)



    video_id = url.replace("https://www.youtube.com/watch?v=", "")
    #print(video_id)
    # Get available transcript languages
    #available_languages = YouTubeTranscriptApi.list_transcripts(video_id)
    #print(available_languages)

    # Get English transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    #print(transcript)

    # Print the transcript text in a readable format
    output=""
    for segment in transcript:
        output+=segment["text"]
        #print(segment["text"])

    MODEL = "gpt-3.5-turbo"
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
        {"role": "system", "content": "Web Scraping Youtube"},
        {"role": "assistant", "content": "write a 55 word summary of this videos"},
        {"role": "user", "content": output}
        ],
        temperature = 0,    
        max_tokens = 250,
    )
   
    message =response.choices[0].message.content.strip() #.lower().translate(str.maketrans('', '', string.punctuation))
    print(message)
   