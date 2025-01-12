# bgChange
A tool written in Python that changes backgrounds! (Only on Windows.)

## Capabilities / Functions
- Changing backgrounds on windows without administrator permissions! (Even workspace-locked versions!)
- The ability to set a default background to use when using an option in the main menu! (Handy for school)
- Restarting explorer.exe from inside the program.
- Supports .webp, .jpg, .jpeg and .png files.

## How does it work?
This script changes the background of the current user by changing the background file in the appdata folder.
Using that, it also tries to change the EncodedWallpaper file. By restarting explorer after that you get a background
that even lasts after a restart! (At least to my knowledge.)

## Compiling it yourself
I mean, I wouldn't recommend it. But sure! Why not? here are the instructions:
- Download the repo as a zip
- Install necesarry libraries using
  ```
  pip install -r requirements.txt
  ```
  (MenuKit is a proprietary library I made in Python, I guess I'll include that in the repo too)
- Install [pyinstaller](https://pypi.org/project/pyinstaller/) or [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/)
- Compile it to an exe, include stock.jpg as a starter background (in case the program's never run yet on a pc, make sure to include a file with this name)
- Save it

## Credits
- J4y_boi (me :O) - All the code
- WanWan09 (a friend of mine) - the app icon

## Screenshot
![Screenshot of the program](screenshot.png?raw=true)
