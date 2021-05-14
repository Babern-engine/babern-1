import time
tic = time.perf_counter()
import pyglet

class window(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


toc = time.perf_counter()
print(tic,'\n',toc)
