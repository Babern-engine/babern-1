
from hashlib import sha256
print(sha256("hello world".encode('utf-8', None)).hexdigest())
def hash(n):
  return ((0x0000FFFF & n)<<16) + ((0xFFFF0000 & n)>>16)
print(hash(sha256("hello world".encode('utf-8', 'UnicodeError')).hexdigest()))
