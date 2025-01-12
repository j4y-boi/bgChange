import sys,os
from time import sleep as wait

#MenuKit#
locallogo = ""
logoLength = 0
strAllowList = []

class LogoNotDefined(Exception):
    "Raised when the logo hasn't been set yet."
    pass

def OptionMenu(*options:str):
    'Prints the defined options. Accepts as many as possible.'
    global optionNum
    num = 0
    for r in options:
        num = num+1
        print(f'{num}) {r}')
    optionNum = num

def OptionMenuInput():
    'Asks ouput based on size of last printed OptionMenu. Arguments are the function name respective to each optionmenu item. It will throw an exception if the amount of function names and the amount of choices are different. Use this as a variable'
    try:
        inp = input('Enter choice: ')
        if not inp.lower() in strAllowList:
            inp = int(inp)
            return inp
        else:
            return inp
    except IndexError:
        return ""
    except ValueError:
        return ""
    
def SetLogo(logo:str):
    'Sets logo. Can also be multiple line.'
    global locallogo
    locallogo = logo

def PrintLogo(centerLogo:bool):
    'Prints the logo plain without extra stuff. You can center the logo.'
    if len(locallogo) == 0:
        print('Logo not defined, did you forget Setlogo()?')
        raise LogoNotDefined
        sys.quit() #in case
    os.system('cls')
    print(locallogo)

def LogoAboveText(text:str,drawline:int,centeredText:bool,textEnable:bool):
    'Prints the logo above text using the text variable (Toggled with textEnable). The drawline variable sets the character length of the line. You can also center the text using the CenteredText boolean.'
    if len(locallogo) == 0:
        print('Logo not defined, did you forget Setlogo()?')
        raise LogoNotDefined
        sys.quit() #in case    
    output = ""
    os.system('cls')
    print(locallogo)
    if textEnable == True:
        if centeredText == True:
            print(text.center(drawline))
        else:
            print(text)
    for x in range(drawline):
        output = output + "-"
    print(output)

def strTolerate(*allowed: str):
    global strAllowList
    for a in allowed:
        strAllowList.append(a.lower())

#print('Loaded MenuKit!')