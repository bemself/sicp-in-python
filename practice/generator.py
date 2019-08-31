def example():
    l = [1, 2,3 ,4]
    for i in l:
        yield i 

gen = example()
print(gen)

print(dir(gen))