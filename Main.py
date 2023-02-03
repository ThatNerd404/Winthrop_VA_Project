# Winthrop_VA_Project - A fun Voice Assistant from my friend's, Winthrop, voice.

import re

def Read_File(file):
    with open(file,"r") as dt:
        data = dt.readlines()
    return data

def Search_File(file):
    for lines in file:
        print(lines)
        
def main():
    
    Compliments_List = Read_File("Querys_List/Compliments_List.txt")
    Greetings_List = Read_File("Querys_List/Greetings_List.txt")
    Insults_List = Read_File("Querys_List/Insults_List.txt")
    Questions_List = Read_File("Querys_List/Questions_List.txt")
    
    Search_File(Compliments_List)
        
    
#* use this to get certain lines [index]




if "__main__" == __name__: 
    main()