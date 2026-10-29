#Question 1
def greet():
    print("Hello World!!!")

greet()

#Question 2
def personalized_greeting(name):
    print("Hello " + name)

personalized_greeting("Ismaeel")

#Question 3
def square(n):
    return n * n

print(square(5))

#Question 4
def rectangle_area(length, width):
    return length * width

print(rectangle_area(4, 5))

#question 5
def apply_operation(func, n):
    return func(n)

def double(n):
    return n * 2

print(apply_operation(double, 7))
print(apply_operation(square, 3))