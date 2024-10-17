def xor(arg1, arg2):
    return not(arg1 and arg2)

print(xor(5, 0) == True)
print(xor(False, False) == False)
print(xor(1, 1) == False)
print(xor(True, True) == False)