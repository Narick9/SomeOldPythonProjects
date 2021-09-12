
def foo(a):
    return a

print(
"""
def foo(a):
    return a
print(foo(4))
"""
, end = "")
print(foo(4))