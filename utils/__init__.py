"""babern utils
babern unitlity classes and functions,
as you know unitlity are very useful so i include it to the engine
careful you must know the path and where you in especially for filesystem like untility
Returns:
		untility
"""

import os, sys, pathlib

def x_reverse(string:str) -> str:return string[::-1];
def x_setlist(lists:list, value:int, changes:object) -> object:lists[value] = changes;
def x_removesame(objects:object)-> object:return set(objects)
def f_folder(foldername:str)->object:return pathlib.Path(foldername).mkdir(parents=True, exist_ok=True)
def f_write(filename, content): open(f"{filename}", "a").write(content)
def f_overwrite(filename, content): open(f"{filename}", "w").write(content)
def f_read(filename, content): return open(f"{filename}", "a").read(content)
def f_delete(filename): os.remove(filename)
def f_delete_folder(foldername): os.rmdir(foldername)
