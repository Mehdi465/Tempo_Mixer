import os 
import youtube_download
from moviepy.editor import VideoFileClip
import shutil
import librosa
import mysql.connector

import youtube_download

def compute_bpm(audio_file_path):
        # Load the audio file
        audio, sr = librosa.load(audio_file_path)

        # Compute the tempo (BPM)
        tempo, _ = librosa.beat.beat_track(audio, sr=sr)

        return tempo


if __name__ == "__main__":
    
    
    # Create the connector to the Music DB

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Reshiram1",
        database="Music"
        )

    cursor = mydb.cursor()

    
    path = "/media/mehdi/MyPocketDisk/song"

    os.chdir(path)
    link = input("Enter the YouTube video URL: ")
    name = youtube_download.Download(link)[:-4] 

    videoclip = VideoFileClip(name + ".mp4")

    audio = videoclip.audio

    wav_file = name + ".wav"

    audio.write_audiofile(wav_file, codec="pcm_s16le")

    bpm = int(youtube_download.compute_bpm(wav_file)[0])

    if os.path.exists(path+"/"+str(bpm)):
        
        shutil.move(wav_file,path+"/"+str(bpm))

    else:
        os.mkdir(str(bpm))
        shutil.move(wav_file,path+"/"+str(bpm))

    path = os.getcwd()
    new_clip_no_audio = videoclip.without_audio()

    os.remove(name + ".mp4")

    new_clip_no_audio.write_videofile(name + "_chore.mp4") 

    if not(os.path.exists(str(bpm))):   
        os.mkdir(str(bpm))


    shutil.move(name + "_chore.mp4","/media/mehdi/MyPocketDisk/chore/"+str(bpm))   

 
    print("Conversion complete!")

    db_name  = name[31:]

    cursor.execute("INSERT INTO Chore (name,bpm) VALUES (%s,%s)",(db_name,bpm))
     
    mydb.commit()
        



