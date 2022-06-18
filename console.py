from platform_utils import *

if on_mac():
    import subprocess    

def prompt():
    opened = False
    while opened:
        opened = False
        if on_mac():
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Unity.app"])
            opened = True

prompt()

            