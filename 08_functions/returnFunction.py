def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(20, 10)

print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])