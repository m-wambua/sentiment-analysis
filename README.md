# sentiment-analysis #

### prequisites ###
#### pip install youtube-dl ####
#### Have an AssemblyAI API key ####
which should be copied in the **configure.py** following line of code:
''' 
auth_key="your-assembly-api-key"

'''

#### To run the code open the **main.py** file and put in your YouTube URL in the following block of code:####
'''

if __name__ =="__main__":
    video_info=get_video_infos("copy-your-youtube-video-link-here")
    audio_url=get_audio_url(video_info)
    print(audio_url)
'''
#### in the **yt_extractor.py** file ####

''' 

if __name__ =="__main__":
    save_video_sentiments("copy-the-youtube-video-link-here")
    '''

#### as well as in the  main.py file ####

##### The transcription will be stored in the ~~data~~ folder. ####
