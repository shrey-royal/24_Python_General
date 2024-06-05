# single line comment
'''
multi
line
comment
'''

"""
multi
line
comment
"""
'''
print statement:
syntax:
    (*objects, sep=' ', end="\n", file=file.sysout, flush=False) -> None

'''

# print("this is an object", '\t', "this is another line", end='\t')
# print("Apple", "Banana", "Cherry", sep="_")

# Data Types
"""

1. Text: str
2. Numeric: int, float, complex(117j)
3. Sequence: list, tuple, range
4. Mapping: dict
5. Set: set, frozenset
6. Boolean: bool
7. Binary: bytes(binary), bytearray(array of binary nums)
8. None: NoneType

"""

print("\"Hello World!\"")
# print('"""Hello World!"""')
# print("\"\"\"Hello World!\"\"\"")

# id() - used to verify the identity of any variable
# type() - used to identify the data type (return classes)

# Variables

# a = "str"
# b = "str1"
# print(id(a))
# print(id(b))
# print(type(a))

# a = 12      # int
# a = 12.6    # float
# a = 1-12j   # complex
# a = "str"   # str
# a = True    # bool (True/False)
# a = b'\x01' # bytes
# a = None
a = 12

print(id(a), '-> ', type(a), '-> ', a)