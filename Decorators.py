import time

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('lgofile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}")
        return value
    
    return wrapper

@logged
def add(x, y):
    return x + y


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value

    return wrapper


@timed
def myfunction(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    
    return result


res = myfunction(10000)

# res = add(10,20)
# print(res)
