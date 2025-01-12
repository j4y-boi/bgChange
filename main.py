#Imports
from menuKit import *
from shutil import copyfile
from time import sleep as wait
from tkinter import Tk,filedialog
from PIL import Image
import os,sys
import keyboard

# - Important setup stuffs - #
exeLocal = sys._MEIPASS #i included a VERY epic background in the stock exe :)
appdata = os.getenv('APPDATA')
bgdir = fr"{appdata}\\Microsoft\Windows\Themes"
ogDir = fr"{exeLocal}\stock.jpg"
configlen = 70 #for da linez (epik c:)
debug = False
root = Tk()
root.withdraw()

SetLogo('''
                █▄▄ █▀▀ ▄▄ █▀▀ █░█ ▄▀█ █▄░█ █▀▀ █▀▀
                █▄█ █▄█ ░░ █▄▄ █▀█ █▀█ █░▀█ █▄█ ██▄''')
# - - - #

if os.path.exists(fr"{appdata}\bgChange\stock.jpg") == False:
    if os.path.exists(fr"{appdata}\bgChange") == False:
        os.mkdir(fr"{appdata}\bgChange")
    target = fr"{appdata}\bgChange\stock.jpg"
    copyfile(ogDir,target)

def browseFiles(): #Finished
    global filename
    root.attributes('-topmost', 1)  # Make the file dialog stay on top
    filename = filedialog.askopenfilename(initialdir = "Downloads",
                                          title = "Select a File",
                                          filetypes = (("Image files",
                                                        "*.jpg .jpeg .png .webp*"),
                                                       ("All files",
                                                        "*.*")))
    root.attributes('-topmost', 0)  # Make the file dialog stay on top
def EnterWait(text): #Finished ig
    Experimental = False
    if text == "":
        displaytext = "Press Enter to go back to the main menu."
    else:
        displaytext = text
    if Experimental:
        print(displaytext)
        while True:
            if keyboard.is_pressed('enter'):
                break
            wait(0.1)  # Add a small delay to avoid high CPU usage
    else:
        input(displaytext)
    OptionMenuReal()
def is_valid_image_pillow(file_name): #Finished
    try:
        with Image.open(file_name) as img:
            img.verify()
            return True
    except (IOError, SyntaxError):
        return False
def changeBG(path): #Finished
    try:
        LogoAboveText("",configlen,True,False)
        if os.path.exists(path):
            if is_valid_image_pillow(path):
                print('Note: DO NOT close the window during this process.')
                print('Loading file...')
                original = fr'{path}'
                target = fr'{bgdir}\TranscodedWallpaper'
                target2 = fr'{bgdir}\CachedFiles\CachedImage_1920_1080_POS4.jpg'

                print('Removing old files...')
                if os.path.exists(target):
                    os.remove(target)
                if os.path.exists(target2):
                    os.remove(target2)

                if path[-4:].lower() == ".jpg" or path[-5:].lower() == ".jpeg":
                    print('Copying files over...')
                    copyfile(original, target)
                    copyfile(original, target2)
                elif path[-4:].lower() == ".png" or path[-5:].lower() == ".webp":
                    print("Converting and moving over...")
                    im = Image.open(original).convert("RGB")
                    im.save(target,"jpeg")
                    im.save(target2,"jpeg")

                print('Restarting Explorer...')
                print('NOTE: This is gonna close the file explorer window.')
                os.system("taskkill /F /IM explorer.exe & start explorer")
                wait(5)
                EnterWait("Done! Press Enter to go back to main menu.")
            else:
                print('There seems to be an issue with this image file...')
                EnterWait("")
        else:
            print('Whoops! That\'s not a valid path.')
            EnterWait("")
    except Exception as e:
        print(f"An error has occurred! ({e})")
        print("If a restart doesn't fix this, maybe you should contact us...")
        EnterWait("")
def OptionMenuReal(): #Finished
    LogoAboveText("",configlen,True,False)
    print('Welcome to bg-Change! Please choose an option:')
    OptionMenu("Change current background.", "Restore background.", "Change background to restore to", "Restart Explorer.exe [In case of glitchy backgrounds]","Credits","Quit")
    choice = str(OptionMenuInput())
    if choice == "1":
        LogoAboveText("",configlen,True,False)
        print('Choose a file from the dialog.')
        browseFiles()
        changeBG(filename)
    elif choice == "2":
        LogoAboveText("",configlen,True,False)
        if os.path.exists(fr"{appdata}\bgChange\stock.jpg") == True:
            print('We\'re now going to revert to the stock background. (Or the one you\'ve chosen.)')
            print('Press Enter to continue. Press backspace to return.')
            wait(0.25)
            while True:
                if keyboard.is_pressed("Enter"):
                    exitType = 1
                    break
                elif keyboard.is_pressed("Backspace"):
                    exitType = 0
                    break
            
            if exitType == 0:
                OptionMenuReal()
            else:
                changeBG(fr"{appdata}\bgChange\stock.jpg")
        else:
            print('It appears you haven\'t set a proper background to restore to yet.')
            print('You can do this in the main menu.')
            EnterWait()
    elif choice == "3":
        LogoAboveText("",configlen,True,False)
        print('Choose a file from the dialog.')
        browseFiles()
        LogoAboveText("",configlen,True,False)
        if os.path.exists(filename) == True:
            print('Updating settings... (This might take a second...)')
            original = fr'{filename}'
            target = fr"{appdata}\bgChange\stock.jpg"

            if os.path.exists(target):
                os.remove(target)

            if filename[-4:].lower() == ".jpg" or filename[-5:].lower() == ".jpeg":
                copyfile(original, target)
            elif filename[-4:].lower() == ".png" or filename[-5:].lower() == ".webp":
                im = Image.open(original).convert("RGB")
                im.save(target,"jpeg")
            LogoAboveText("",configlen,True,False)
            print('Finished changing image.')
            input("Press Enter to continue.")
            OptionMenuReal()
        else:
            LogoAboveText("",configlen,True,False)
            print('This isn\'t a valid path/image file.')
            input("Press Enter to continue.")
            OptionMenuReal()
    elif choice == "4":
        LogoAboveText("",configlen,True,False)
        print('You\'re about to restart explorer. Only do this if your background is glitchy after pressing Window+Crtl+Shift+B.')
        print('Please also note that this will close your file explorer window.')
        print('Press Enter to continue. Press backspace to return.')
        wait(0.25)

        while True:
            if keyboard.is_pressed("Enter"):
                exitType = 1
                break
            elif keyboard.is_pressed("Backspace"):
                exitType = 0
                break
        
        if exitType == 0:
            OptionMenuReal()
        else:
            LogoAboveText("",configlen,True,False)
            print('Restarting Explorer...')
            print('Note: This gonna close the file explorer window')
            os.system("taskkill /F /IM explorer.exe & start explorer")
            wait(5)
            
            input('Done! Press enter to go back to the main menu.')
            OptionMenuReal()
    elif choice == "5":
        LogoAboveText("Created by j4y_boi",configlen,True,True)
        print('This program was made and created by j4y_boi.'.center(configlen))
        print('Check me out on YouTube!'.center(configlen))
        print('https://www.youtube.com/@j4y_boi'.center(configlen))
        print('For extra info check the repo or contact us.'.center(configlen))
        print('-'.center(configlen))
        EnterWait('Press Enter to go back to the main menu.'.center(configlen))
    elif choice == "6":
        os.system("cls")
        sys.exit()
    else:
        LogoAboveText("",configlen,True,False)
        print("That isn't a valid option.")
        EnterWait("")

OptionMenuReal()
