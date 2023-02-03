# Winthrop_VA_Project - A fun Voice Assistant from my friend's, Winthrop, voice.

import regex

def Read_File(file):
    with open(file,"r") as dt:
        data = dt.readlines()
    return data

def main():
    testing = Read_File("Querys_List/Compliments_List.txt")
    print(testing)

#* use this to get certain lines [index]




if "__main__" == __name__: 
    main()