def plus(n1, n2) :
    return n1 + n2

def minus(n1, n2) :
    return n1 - n2 

def multiply(n1, n2) :
    return n1 * n2 

def divide(n1, n2) :
    return n1 / n2

def test() :
    print('test')

print(f"__name__ : {__name__}")

#메인모듈일때만 실행시키고 싶을 때 
if __name__ == '__main__' : 
    import random

    print(plus(1,1))
    print(minus(10,5))
    print(multiply(10,2))
    print(random.randint(1,10))

    # my_module : main 모듈 , # random : sub 모듈 