# Generators - only generates the value on demand

def generator(n):
    for x in range(n):
        yield x

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()

print(next(values))
print(next(values))
print(next(values))
print(next(values))
