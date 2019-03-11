import os
import backInPath as bip

def getpath():
    try:
        cur_path = os.getcwd()
        print("You are currently in: ")
        print(cur_path)
        listDir = os.listdir(cur_path)
        print("Directory contains: \n")
        for file in listDir:
            print(file)
    except Exception as e:
        print("Failed to load file-path")
