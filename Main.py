# Winthrop_VA_Project - A fun Voice Assistant from my friend's, Winthrop, voice.

#* TODO: get rid of \n characters in the lists and continue with the query system

import sys
import os
import json
import pygame


def main():
    os.system('cls')
    print("#" * 50)
    print("#        Winthrop Voice Assistant Project!       #")
    print("#              By Brayden Cotterman              #")
    print("#" * 50)
    start = input('\nType Q at anytime to quit!\nPress enter to start!')
    # Nice intro page Me!
    
    Compliments_List = Read_File("Querys_List/Compliments_List.json")
    Greetings_List = Read_File("Querys_List/Greetings_List.json")
    Insults_List = Read_File("Querys_List/Insults_List.json")
    Questions_List = Read_File("Querys_List/Questions_List.json")
    Query_list = [Compliments_List,Greetings_List,Insults_List,Questions_List]
    
    while True:
        Query = input('Winthrop is listening... type your query!\n')
        for List in Query_list:
            if Query in List:
                os.system('cls')
                music(List[Query])
                break
            
            elif Query == "q":
                sys.exit()
            
            
            
def Read_File(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)
        return data

def music(mp3):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
  



if "__main__" == __name__: 
    main()