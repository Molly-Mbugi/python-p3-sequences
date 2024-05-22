#!/usr/bin/env python3

def print_fibonacci(length):
    pass
def print_fibonacci(length):
    
    fn = [0, 1,]
    for i in range(2, length):
        fn.append(fn[i-1] + fn[i-2])
    return fn