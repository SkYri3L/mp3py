import pygame, os
from pygame import mixer

mixer.init()

Open = 1
volume = 50


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
    if playing == False:
        mixer.music.play()
        status = "Music Playing"
    elif playing == True:
        pass
    else:
        pass

def stopsong():
    global status
    mixer.music.stop()
    status = "Music Stopped"
def pausesong():
    global status
    if paused == True:
        pass
    elif paused == False:
        mixer.music.pause()
        status = "Music Paused"
    else:
        pass

def unpausesong():
    global status
    if paused == True:
        mixer.music.unpause()
        status = "Music Playing"
    elif paused == False:
        pass
    else:
        pass
def loopsong():
    global status
    status = "Looping current song"
    mixer.music.play(-1)

def vol_up():
    global volume
    volume = volume + 10
    mixer.music.set_volume(volume)


def vol_down():
    global volume
    volume = volume - 10
    mixer.music.set_volume(volume)




song_dir()
Select()
song_reset()
mixer.music.set_volume(volume)

while Open == 1:
    clearconsole()

    print("Current Song: ", track[Song_Select])
    print("Current Status: ", status)
    print("Current Volume: ", volume)

    check = input("1: Play\n2: Stop\n3: Pause\n4: Unpause\n5: Loop Song\n6: Song Select\n7: Change Directoy\n8: Volume Up\n9: Volume Down\n10: Exit\nEnter Number:")

    if check == "1" or check == "play" or check == "Play":
        playsong()
    elif check == "2" or check == "stop" or check == "Stop":
        stopsong()
    elif check == "3" or check == "Pause" or check == "pause":
        pausesong()
    elif check == "4" or check == "Unpause" or check == "unpause":
        unpausesong()
    elif check == "5" or check == "loop" or check == "Loop":
        loopsong()
    elif check == "6" or check == "Song" or check == "song":
        mixer.music.stop()
        song_reset()
        Select()
    elif check == "7" or check == "Change" or check == "directory" or check == "Change Directory" or check == "Directory" or check == "change" or check == "dir" or check == "Dir":
        mixer.music.stop()
        song_reset()
        song_dir()
    elif check == "8" or check == "Up" or check == "up":
        vol_up()
    elif check == "9" or check == "Down" or check == "down":
        vol_down()
    elif check == "10" or check == "exit" or check == "Exit":
        quit()
