#!/bin/python3
import dis

def magic_calculation(a, b):
    result = 98
    result += a ** b

    # Disassemble the bytecode
    dis.dis(magic_calculation.__code__)

    return result

# Example usage
a = 1
b = 2
result = magic_calculation(a, b)
print(result)
