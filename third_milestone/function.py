def greet():
    print("Hello world")

def add(*args):
    result=0
    for nums in args:
        result+=nums
    return result

def multiply(*args):
    result=1
    for nums in args:
        result*=nums
    return result


def usdtoeuro(a):
    return round(a*0.92,2)

def eurotousd(a):
    return round(a*1.09,2)

print(usdtoeuro(10))
print(eurotousd(10))
# print(add(4,5,6,7,8,9,10))
# print(multiply(4,5,6,7,8))