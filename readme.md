# STEMC-Snapshot Tool
As part of our work we’ve developed a tool to compare iterations of code students make. The goal is not just to easily see what they’ve changed between updates but automate detecting rigor and creative alterations. The model for what qualifies as an ideal change was established by comparing screen capture of coding activities. 

Currently, the tool pulls code files from ComputerCraft at regular intervals from a defined local or FTP location but it could be adapted for use with any set of text files, with adjustment to the library of recognized functions by language (in our case Lua).

---
## Installing
Place snapshot.py in your root Forge (ComputerCraft) directory and run it via CLI with python (or pyhton3) snapshot.py

## Operation
To stop the program just hit enter, results will be available as a CSV in the defined directory.