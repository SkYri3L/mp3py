import pygame, os
from pygame import mixer

mixer.init()

Open = 1
Vol_Stat = "unmuted"

def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def song_dir():
    global track
    global Dir
    Dir = input("Please Enter Songs Directory: ")
    track = os.listdir(Dir)

def song_reset():
    global playing
    global paused
    global status
    status = "Music Stopped"
    paused = False
    playing = False

def Select():
    global Song_Select
    global track
    mixer.music.unload()
    num = 0
    for tracks in track:
        print(num,": "+tracks)
        num = num + 1
    Song_Select = int(input("Enter Track Number: "))
    print(track[Song_Select])
    song = (Dir+"/"+track[Song_Select])
    print(song)
    mixer.music.load(song)

def playsong():
    global status
    global playing
    global paused
    if playing == False:
        mixer.music.play()
        status = "Music Playing"
        playing = True
    elif playing == True:
        pass
    elif paused == True and playing == False:
        mixer.music.unpause()
        playing = True
        paused = False
    else:
        pass

def stopsong():
    global status
    global playing
    if playing == True:
        mixer.music.stop()
        status = "Music Stopped"
        playing = False
    elif playing == False:
        pass

def pausesong():
    global status
    global playing
    global paused
    if playing == False:
        pass
    elif playing == True:
        mixer.music.pause()
        status = "Music Paused"
        playing = False
        paused = True
    else:
        pass

def loopsong():
    global status
    global playing
    playing = True
    status = "Looping current song"
    mixer.music.play(-1)

def mute():
    global Vol_Stat
    Vol_Stat = "Muted"
    mixer.music.set_volume(0)

def unmute():
    global Vol_Stat
    Vol_Stat = "unmuted"
    mixer.music.set_volume(100)




song_dir()
Select()
song_reset()

while Open == 1:
    clearconsole()

    print("Current Song: ", track[Song_Select])
    print("Current Status: ", status)
    print("Current Volume: ", Vol_Stat)

    check = input("1: Play\n2: Stop\n3: Pause\n4: Loop Song\n5: Song Select\n6: Change Directoy\n7: Mute\n8: Unmute\n9: Exit\nEnter Number:")

    if check == "1" or check == "play" or check == "Play":
        playsong()
    elif check == "2" or check == "stop" or check == "Stop":
        stopsong()
    elif check == "3" or check == "Pause" or check == "pause":
        pausesong()
    elif check == "4" or check == "loop" or check == "Loop":
        loopsong()
    elif check == "5" or check == "Song" or check == "song":
        mixer.music.stop()
        song_reset()
        Select()
    elif check == "6" or check == "Change" or check == "directory" or check == "Change Directory" or check == "Directory" or check == "change" or check == "dir" or check == "Dir":
        mixer.music.stop()
        song_reset()
        song_dir()
    elif check == "7" or check == "mute" or check == "Mute":
        mute()
    elif check == "8" or check == "Unmute" or check == "unmute":
        unmute()
    elif check == "9" or check == "exit" or check == "Exit":
        quit()
