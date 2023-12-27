from pytube import YouTube
import os 
from moviepy.editor import VideoFileClip,AudioFileClip
import shutil
import mysql.connector

def print_music(list_music):
    for music in list_music:
         print(f"({music['id']}) : {music['name']} and bpm = {music['bpm']}")
         

def select_song(path):
    list_songs = []
    id_song = 0
    id_bpm = 0
    path = path+"/song"

    test = os.walk(path, topdown=True)

    for bpm_list_all in test:
        break

    bpm_list = bpm_list_all[1]

    print(bpm_list)

    for (root,dirs,files) in os.walk(path, topdown=True): 
        if (id_bpm<len(bpm_list)):
            for file in files:
               list_songs.append({"name":file[:-4],"id":id_song,"bpm":bpm_list[id_bpm-1]})
               id_song +=1
            
        id_bpm +=1

    print_music(list_songs)   

    res = int(input("Select the number of the song you want : "))

    bpm_selected = list_songs[res]["bpm"]
    os.chdir(path+"/"+str(bpm_selected))

    print(bpm_selected)

    audio_clip = AudioFileClip(list_songs[res]["name"]+".wav")

    return audio_clip,int(bpm_selected),list_songs[res]["name"]


def select_chore(path,bpm_selected):
    id_file = 0
    list_chore = []

    for bpm in range(bpm_selected-1,bpm_selected+2):
        for (root,dirs,files) in os.walk(path+"/chore/"+str(bpm), topdown=True): 

            if (id_file<len(files)):
                for file in files:
                   list_chore.append({"name":file[:-4],"id":id_file,"bpm":bpm})
                   id_file +=1

    print_music(list_chore)  

    if (len(list_chore)==0) :
        print("There is no bpm matching for this song, sorry....")
        pass

    res = int(input("Select the number of the song you want : "))

    bpm_selected = list_chore[res]["bpm"]
    os.chdir(path+"/chore/"+str(bpm_selected))
    
    video_clip = VideoFileClip(list_chore[res]["name"]+".mp4")

    return video_clip,list_chore[res]["name"]                  

    

if __name__ == "__main__":


    path = "/media/mehdi/MyPocketDisk"

    #response = choose_choice(mycursor,path)

    #dic_chore,dic_songs,N_chore,N_song = choice(path,response)

    #name_chore,bpm_chore,name_song,bpm_song = get_video_and_music(dic_chore,dic_songs,N_chore,N_song)

    audio_clip,bpm,song_name = select_song(path)
    video_clip,chore_name = select_chore(path,bpm)
    
    os.chdir(path)

    
    #time = audio_clip.duration
    
    # Set the audio of the video clip to the loaded audio clip
    video_clip = video_clip.set_audio(audio_clip)

    # Define the output file path
    output_file = chore_name[:-4] + "_chore_with_" + song_name[:-4] +"_song" + ".mp4"

    # Write the merged video to a file
    os.chdir(path)

    if not(os.path.exists(path+"/final")):
            os.mkdir(str("final"))

    os.chdir(path+"/final")        

    video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")



