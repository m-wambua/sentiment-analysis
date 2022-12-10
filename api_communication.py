import requests
from configure import auth_key
import time
import json
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint="https://api.assemblyai.com/v2/transcript"
headers = {'authorization': auth_key,
            'content-type': 'application/json'}


def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                yield data


    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))

    #print(response.json())
    audio_url=upload_response.json()['upload_url']
    return audio_url
def transcribe(audio_url,sentiment_analysis):
    transcript_request={"audio_url":audio_url,
    "sentiment_analysis":sentiment_analysis}
    transcript_response=requests.post(transcript_endpoint,json=transcript_request,headers=headers)

    #print(response.json())
    job_id=transcript_response.json()['id']

    return job_id

# poll
def poll(transcript_id):
    polling_endpoint= transcript_endpoint + '/' + transcript_id

    polling_response=requests.get(polling_endpoint,headers=headers)
    return polling_response.json()

    #print(polling_response.json())
def get_transcription_url(url,sentiment_analysis):
    transcript_id=transcribe(url,sentiment_analysis)
    while True:
        data=poll(transcript_id)
        #polling_response=requests.get(polling_endpoint,headers=headers)

        if data['status']=='completed':
            return data , None
        elif data['status']=='error':
            return data , data["error"]
        print("waiting 30 seconds....")
        time.sleep

#transcipt_id=transcribe(audio_url)

def save_transcirpt(url,title,sentiment_analysis=False):
    data,error=get_transcription_url(url,sentiment_analysis)
    #print(job_id)


    #text_filename=filename+ ".txt"

    if data:
        filename=title + '.txt'
        with open(filename,"w") as f:
            f.write (data['text'])

        if sentiment_analysis:
            filename= title + "_sentiments.json"
            with open(filename, "w") as f:
                sentiments=data["sentiment_analysis_results"]
                json.dump(sentiments ,f , indent=4)

        print("Transcription is saved!!!")

    elif error:
        print("Error!",error)

    #print(data)


