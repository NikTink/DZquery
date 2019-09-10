# DZquery
a simple query tool with a simple HUD for the game DayZ.

The tool sniffs your port 2304 for outgoing traffic. When it finds the destination address, the tool contacts api.steampowered.com to find out the query port for that server. After the query port is found, the tool begins to (by default) query the server every minute for player- and time-data and displays it on the screen. 

   This was more of a proof of concept idea/project. feel free to improve on it (please!!)

Usage:

    run the compiled .exe and join a server.
    
    to change the overlay position: hold shift and one of the arrowkeys. This is saved across restarts in the config file. Optionally you can change the location manually in the config file. All changes done to the config file will update in real time to the HUD-element
    Kill the program at any time by pressing ctrl+c

Compiling:

    1. have your poke around the code and config as much as you'd like
    2. install python 3.7
    3. run the "compile.bat" 

Notes:

    -Currently optimized for 1920x1080p displays by default. Alter the location to your liking
    -The loading of all necessary libraries takes a while. Read the console prompt
    -The HUD does not work when the game is in fullscreen-mode. Use borderless windowed. I will not start messing with Direct3d drivers and memory

config:
   
   
    "updateRate": The rate in seconds the server is queried (TYPE: INT)
    "PfromTop": How many pixels from the top of the display the overlay is placed (TYPE: STRING)
    "PfromSide": How many pixels from the LEFT side of the display the overlay is placed (TYPE: STRING)
    "TextColour": Colour of the overlay text(TYPE: STRING)
    "BGColour": Colour of the background. Doesnt really change much, but bleeds a bit, so black is the best to use for most "TextColour" options
    
    ALL SETTINGS ARE UPDATED IN RUNTIME and take effect immediately once you save the file
    
    
If the server is not reached during runtime, the HUD will turn red. As soon as the server can be reached again, it will return to your configured colour (default: green)
