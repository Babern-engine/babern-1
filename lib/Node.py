import time
import threading
from functools import lru_cache
def create_thread(function):
   thread = threading.Thread(target=function)
   return thread.start()

tic = time.perf_counter()
class parent(object):
	def __init__(self, name):
		self.name = name

class child(object): ...
class tree(object): ...

class Node(object):
	def __init__(self, name, parent, child):
		self.name = name
		self.parent = parent
		self.child = child

	def visit_child(self):
		return self.child

	def visit_parent(self):
		return self.parent




#cur = node1
#cur = nodes

# test none
@lru_cache()
def i1():
	nodes = Node("test", [parent("hello"), parent("jello")], child)
	nodes.visit_parent()[1].name

@lru_cache()
def i2():
	node1 = Node("in1", [parent("llo"), parent("jo")], child)
	node1.visit_parent()[1].name

@lru_cache()
def i3():
	node1 = Node("in1", [parent("llo"), parent("kol")], child)
	node1.visit_parent()[1].name

@lru_cache()
def i4():
	node1 = Node("in1", [parent("llo"), parent("jde")], child)
	node1.visit_parent()[1].name

@lru_cache()
def i5():
	node1 = Node("in1", [parent("llo"), parent("crro")], child)
	node1.visit_parent()[1].name

@lru_cache()
def i6():
	node1 = Node("in1", [parent("llo"), parent("eos")], child)
	node1.visit_parent()[1].name

@lru_cache()
def i7():
	node1 = Node("in1", [parent("llo"), parent("jeo")], child)
	node1.visit_parent()[1].name

@lru_cache()
def i8():
	node1 = Node("in1", [parent("llo"), parent("neo")], child)
	node1.visit_parent()[1].name

@lru_cache()
def i9():
	node1 = Node("in1", [parent("llo"), parent("pjk")], child)
	node1.visit_parent()[1].name

@lru_cache()
def i10():
	node1 = Node("in1", [parent("llo"), parent("deo")], child)
	node1.visit_parent()[1].name

create_thread(i1)
create_thread(i2)
create_thread(i3)
create_thread(i4)
create_thread(i5)
create_thread(i6)
create_thread(i7)
create_thread(i8)
create_thread(i9)
create_thread(i10)

toc = time.perf_counter()
print(tic)
print(toc)
