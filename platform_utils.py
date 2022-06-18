import platform

def on_mac():
    return platform.system() == "Darwin"
