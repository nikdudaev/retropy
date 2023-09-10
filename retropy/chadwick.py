import subprocess
from os import environ, getcwd
import config

# Checking if Chadwick tools are installed
def check_tools(tool):
    command = subprocess.run["which", tool], capture_output=True, text=True)
    returncode = command.returncode
    return returncode

def tool_path(tool):
    if check_tools(tool) == 0:
        dir = subprocess.run(["which", tool], capture_output=True, text=True)
        return(dir.stdout.replace("\n", ""))
    else:
        return("")

def install_tools():
    home_dir = environ['HOME']
    subprocess.run(["cd", home_dir])
    try:
        subprocess.run(["wget", config.chadwick_url])
    except Exception as err:
        print(f"Error: {err}"
        exit(1)
    print("Configuring package...")
    subprocess.run(["tar", "xfz", config.chadwick_tar])
    subprocess.run(["cd", config.chadwick_folder])
    subprocess.run(["./configure"])
    subprocess.run(["make"])
    print("You will be asked to enter sudo password to continue the installation")
    subprocess.run(["sudo make install"])

def chadwick_check_and_install():
    pass
