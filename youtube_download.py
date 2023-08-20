from pytube import YouTube
import os 
from moviepy.editor import VideoFileClip
import shutil
import librosa
from moviepy.editor import *
import mysql.connector

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    res = " ERROR"
    try:
        res = youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

    return res

def compute_bpm(audio_file_path):
        # Load the audio file
        audio, sr = librosa.load(audio_file_path)

        # Compute the tempo (BPM)
        tempo = librosa.beat.beat_track(audio, sr=sr)

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
    name = Download(link)[:-4] 

    # Specify the path and name of the MP4 file
    mp4_file = name + ".mp4"

    # Specify the path and name of the output WAV file

    wav_file = name + ".wav"

    print("The music name is : " + name)

    # Load the MP4 file
    video = VideoFileClip(mp4_file)

    # Extract the audio from the video
    audio = video.audio
    
    # Save the audio as WAV file
    audio.write_audiofile(wav_file, codec="pcm_s16le")

    print("Conversion complete!")


    # Path to your audio file
    audio_file_path = wav_file

    # Compute the BPM
    
    bpm = int(compute_bpm(audio_file_path)[0])
    print("BPM:", bpm)


    # Moves the wav file in the corresponding directory
    os.remove(mp4_file)

    db_name  = name[31:]

    if os.path.exists(path+"/"+str(bpm)):
        
        shutil.move(audio_file_path,path+"/"+str(bpm))

    else:
        os.mkdir(str(bpm))
        shutil.move(audio_file_path,path+"/"+str(bpm))


    # Add the new song in the Music Table
    cursor.execute("INSERT INTO Song (name,bpm) VALUES (%s,%s)",(db_name,bpm))
     
    mydb.commit()
        




    



   