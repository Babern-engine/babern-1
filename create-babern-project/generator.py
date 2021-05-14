import os, sys, platform, pathlib
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
p = pathlib.Path("temp/").mkdir(parents=True, exist_ok=True)
f = open("temp/demofile2.txt", "a")
