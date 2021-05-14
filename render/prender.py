import time
tic = time.perf_counter()
import OpenGL
OpenGL.ERROR_CHECKING = False
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

def main():
	# Initialize the library
	if not glfw.init():
		return
	# Create a windowed mode window and its OpenGL context
	window = glfw.create_window(640, 480, "Hello World", None, None)
	if not window:
		glfw.terminate()
		return
	# Make the window's context current
	glfw.make_context_current(window)

	# Loop until the user closes the window
	while not glfw.window_should_close(window):
		# Render here, e.g. using pyOpenGL

		# Swap front and back buffers
		glfw.swap_buffers(window)

		# Poll for and process events
		glfw.poll_events()
	glfw.terminate()

toc = time.perf_counter()
print(tic,'\n',toc)
