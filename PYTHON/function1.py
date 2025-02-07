#!/usr/bin/python3
def greet(name):
    return f"Hello, {name}"

say_hello = greet
print(say_hello("Alice"))

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet1(func):
    print(func("Hello world"))

greet1(shout)
greet1(whisper)

def make_mult(n):
    def mult(x):
        return n * x
    return mult
times3 = make_mult(3)
print(times3(5))

