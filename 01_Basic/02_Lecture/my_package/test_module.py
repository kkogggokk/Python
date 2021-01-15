def hello_world() : 
    print('hello world')

def greeting(name) :
    print(f"{name}님, 안녕하세요.")

class Person :
    
    def __init__(self, name, age) :
        self.name = name
        self.age = age 

    def __str__(self) :
        return f"{self.name}, {self.age}"