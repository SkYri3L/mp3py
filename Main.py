import pygame
Open = 1
pygame.mixer.init()
pygame.mixer.music.load('Songs/Song.mp3')


while Open == 1:
    print("Current Song: ")
    check = input("Play/Stop/Exit :")
    if check == "P" or check == "Play" or check == "play" or check == "p":
        pygame.mixer.music.play()
    elif check == "S" or check == "stop" or check == "Stop" or check == "s":
        pygame.mixer.music.stop()
    elif check == "Exit" or check == "exit" or check == "E" or check == "e":
        quit()
    else:
        print("Wrong Input")