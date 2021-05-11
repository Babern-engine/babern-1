print(UserWarning("Dont include this test on production"))
import unittest
import inspect
print(inspect.getfile(unittest))
unittest.main()
