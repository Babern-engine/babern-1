import os, sys, pathlib

foldername = input("Project Name: ")
p = pathlib.Path(foldername).mkdir(parents=True, exist_ok=True)
f = open(f"{foldername}/config.py", "w")
f.write(f"PROJECT_NAME='{foldername}'\nNETWORK='socket'\nID={hash(foldername)}\nPLUGINS=[]\nDB='json'\nLOG=False\nENV='dev'")
f.close()
