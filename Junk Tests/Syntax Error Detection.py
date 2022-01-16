import subprocess
import os



for x in os.listdir('Lua to test'):
    if (0 != subprocess.run('luac -p ' + '"Lua to test/' + x + '"', shell=True, capture_output=True).returncode):
        print(x)