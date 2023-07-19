import winreg
import os
import random
import subprocess
try:
    installpath = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\WOW6432Node\Valve\Steam"), "InstallPath")[0]
except:
    print("Couldn't locate Steam.")
    quit()
ids = []
for file in os.listdir(installpath + "\\steamapps"):
    if file.startswith("appmanifest_") & file.endswith(".acf"):
        with open(file) as f:
            if not '"InstallScripts"' in f.read():
                ids.append(file[12:][:-4])
id = ids[random.randint(0, len(ids)-1)]
subprocess.call(installpath + "\\Steam.exe -applaunch " + id)
