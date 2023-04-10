# STEMC-Snapshot and Differences Tools
As part of our work we’ve developed a tool to compare iterations of code students make. The goal is not just to easily see what they’ve changed between updates but automate detecting rigor and creative alterations. The model for what qualifies as an ideal change was established by comparing screen capture of coding activities. 

Currently, snapshot.py pulls code files from ComputerCraft directory on the active Minecraft server at regular intervals from a defined local location. The script could be adapted for use with any set of text files, with adjustment to the library of recognized functions by language (in our case Lua).

differences.py operates on the data collected with snapshot.py. It generates an overview csv file with characteristics of each iteration of student work. Additionally, differences.py generates a html file for each project that highlights differences between iterations.

---
## Using snapshot.py
Place snapshot.py in your root Forge (ComputerCraft) directory and run it via CLI with python (or pyhton3) snapshot.py

To stop the program just hit enter, results will be available as a folder of iterations in the defined directory.

## Using differences.py
After snapshot.py has stopped running, place differences.py in the directory immediately above the folder that is outputted by snapshot.py.

Run the script via CLI with python (or pyhton3) differences.py