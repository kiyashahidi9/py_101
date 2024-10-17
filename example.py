bar = 0
foo = []
baz = 3

try:
    qux = (bar or foo) and (baz / bar)
except ZeroDivisionError:
    qux = 0

print(qux)

if qux:
    print("Operation succeeded")
else:
    print("Operation failed")