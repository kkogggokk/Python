# 42. 데코레이터
- 데코레이터 : 장식하다, 꾸미다 
- 클래스에서 메서드를 만들때 @staticmethod, @classmethod, @abstractmethod 
- 이때, '@' 로 시작하는 것이 데코레이터
- 즉, 함수(메서드)를 장식한다고 해서 붙여진 이름
- 데코레이터는 기존 함수를 수정하지 않으면서 추가 기능을 구현할 때 사용

## 42.1 데코레이터 만들기 


```python
# 예) 함수의 시작과 끝을 출력 
def hello() :
    print('hello start')
    print('hello')
    print('hello end')
    
def world() :
    print('world start')
    print('world')
    print('world end')
```

- 다른 함수도 시작과 끝을 출력하고 싶다면 함수를 만들때 마다 print를 넣어야 하므로 번거로움 
- 이런경우 데코레이터를 활용하면 편리함. 


```python
# 함수의 시작과 끝을 출력하는 데코레이터 
def trace(func):                            # 호출할 함수를 매개변수로 받음
    def wrapper():                          # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                              # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')     # 함수의 끝을 알리는 문자열 출력
    return wrapper                         # wrapper 함수 반환
 
def hello():
    print('hello')
 
def world():
    print('world')
 
trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
trace_hello()                 # 반환된 함수를 호출
trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
trace_world()                 # 반환된 함수를 호출
```

- 데코레이터 trace는 호출할 함수를 매개변수로 받는다.               
- wrapper함수에서는               
- 함수의 시작을 알리는 문자열을 출력하고, 호출 시 매개변수로 받은 함수의 원래 이름을 출력할 때는 \_\_name__속성을 활용한다.               
- trace에서 매개변수로 받은 func를 호출한다.               
- 그 다음에 함수의 끝을 알리는 문자열을 출력한다.            
- wrapper함수를 다 만들었으며 return을 사용하여 wrapper함수 자체를 반환한다.     
- 즉, 함수안에서 함수를 만들고 반환하는 클로저이다. 

### 42.1.1 @ 데코레이터 사용하기
- '@'을 사용하여 좀 더 간편하게 데코레이터 사용하기
- 다음과 같이 호출할 함수 위에 @데코레이터 형식으로 지정


```python
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
@trace    # @데코레이터
def hello():
    print('hello')
 
@trace    # @데코레이터
def world():
    print('world')
 
hello()    # 함수를 그대로 호출
world()    # 함수를 그대로 호출
```

![데코레이터](https://dojang.io/pluginfile.php/14011/mod_page/content/3/042001.png)

> <B>참고 > 데코레이터를 여러개 지정하기</b>
> - 함수 위에 데코레이터를 여러줄로 지정하여 여러개 지정할 수 있다. 
> - 데코레이터가 실행되는 순서는 위에서 아래 순이다. 


```python
def decorator1(func) :
    def wrapper() :
        print('decorator1')
        func()
    return wrapper
    
def decorator2(func) :
    def wrapper() :
        print('decorator2')
        func()
    return wrapper

# 데코레이터 여러개 지정
@decorator1
@decorator2
def hello() :
    print('hello')

    
hello()
```

## 42.2 매개변수와 반환값을 처리하는 데코레이터 만들기
- 지금까지 매개변수와 반환값이 없는 함수의 데코레이터를 만들어 보았다.
- 이번에는 매개변수와 반환값을 처리하는 데코레이터는 어떻게 만드는지 알아보자.


```python
def trace(func):          # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b)    # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a : {1}, b : {2}) = {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
        return r          # func의 반환값을 반환
    return wrapper        # wrapper 함수 반환
 
@trace              # @데코레이터
def add(a, b):      # 매개변수는 두 개
    return a + b    # 매개변수 두 개를 더해서 반환
 
print(add(10, 20))
```

### 42.2.1 가변인수 함수 데코레이터
- def add(a, b) 는 매개변수의 개수가 고정된 함수이다.
- 그러면 매개변수(인수)가 고정되지 않는 함수는 어떻게 처리할까?


```python
def trace(func):                     # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):    # 가변 인수 함수로 만듦
        r = func(*args, **kwargs)    # func에 args, kwargs를 언패킹하여 넣어줌 : args는 튜플, kwargs는 딕셔너리
        print('{0}(args : {1}, kwargs : {2}) -> {3}'.format(func.__name__, args, kwargs, r))
                                     # 매개변수와 반환값 출력
        return r                     # func의 반환값을 반환 
    return wrapper                   # wrapper 함수 반환
 
@trace                   # @데코레이터
def get_max(*args):      # 위치 인수를 사용하는 가변 인수 함수
    return max(args)
 
@trace                   # @데코레이터
def get_min(**kwargs):   # 키워드 인수를 사용하는 가변 인수 함수
    return min(kwargs.values())
 
print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))\
```

> <b>참고 > 메서드에 데코레이터 사용하기</b>
> - 클래스를 만들면서 메서드에 데코레이터를 사용할 때는 self를 주의해야 한다.
> - 인스턴스 메서드는 항상 self를 받으므로 데코레이터를 만들때좆 wrapper함수의 첫번째 매개변수는 self로 지정
> - 클래스 메서드는 cls로 지정 
> - 마찬가지로 func를 호출 할때도 self와 매개변수를 그대로 넣어야 한다.


```python
def trace(func):
    def wrapper(self, a, b):   # 호출할 함수가 인스턴스 메서드이므로 첫 번째 매개변수는 self로 지정
        r = func(self, a, b)   # self와 매개변수를 그대로 넣어줌
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))   # 매개변수와 반환값 출력
        return r               # func의 반환값을 반환
    return wrapper
 
class Calc:
    @trace
    def add(self, a, b):    # add는 인스턴스 메서드
        return a + b
 
c = Calc()
print(c.add(10, 20))
```

## 42.3 매개변수가 있는 데코레이터 만들기
- 이번에는 매개변수가 있는 데코레이터를 만들어보자. 
- 데코레이터는 값을 지정해 동작을 바꿀 수 있다. 


```python
# 함수의 반환값이 특정 수의 배수인지 확인하는 데코레이터 
def is_multiple(x):              # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):    # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):       # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b)       # func를 호출하고 반환값을 변수에 저장
            if r % x == 0:       # func의 반환값이 x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r             # func의 반환값을 반환 
        return wrapper           # wrapper 함수 반환
    return real_decorator        # real_decorator 함수 반환
 
@is_multiple(3)     # @데코레이터(인수)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add(2, 5))
```

> <b>참고 > 원래 함수 이름이 안나온다면?</b>
> - 함수의 원래 이름을 출력하고 싶다면 functools 모듈의  wraps 데코레이터를 사용해야 한다.
> - @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정해준다. 
> - @functools.wraps 는 원래 함수의 정보를 유지시켜준다. 
> - 따라서 디버깅할 때 유용하므로 데코레이터를 만들때 @functools.wraps를 사용하는 것이 좋다.


```python
import functools
 
def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)    # @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator
 
@is_multiple(3)
@is_multiple(7)
def add(a, b):
    return a + b
 
add(10, 20)
```

## 42.4 클래스로 데코레이터 만들기
- 이번에는 클래스로 데코레이터를 만드는 방법에 대해 알아보자
- 클래스를 활용할 때는 인스턴스를 함수처럼 호출하게 해주는 \_\_call__메서드를 구현해야 한다.


```python
# 함수의 시작과 끝을 출력하는 데코레이터 
class Trace:
    def __init__(self, func):    # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func         # 호출할 함수를 속성 func에 저장
 
    def __call__(self):
        print(self.func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        self.func()                               # 속성 func에 저장된 함수를 호출
        print(self.func.__name__, '함수 끝')
 
@Trace    # @데코레이터
def hello():
    print('hello')
 
hello()    # 함수를 그대로 호출
```

- 데코레이터를 만들 때는 먼저 \_\_init__ 메서드를 만들고 호출할 함수를 초깃값으로 받는다.
- 그리고 매개변수로 받은 함수를 속성으로 저장한다.
- 인스턴스를 호출할 수 있도록 \_\_call__메서드를 만든다.
-  \_\_call메서드에 함수의 시작을 알리는 문자열을 출력하고, 속성 func에 저장된 함수를 호출한다. 그리고 끝을 알리는 문자열을 출력한다.
- 데코레이터를 사용하는 방법은 클로저 형태의 데코레이터와 같다.
- 호출할 함수위에 @를 붙이고 데코레이터를 지정하면 된다. 

- 참고로 클래스로 만든 데코레이터는 @을 지정하지 않고, 데코레이터의 반환값을 호출하는 방식으로도 사용 가능
- 데코레이터레 호출할 함수를 넣어서 인스턴스를 생성한 뒤 인스턴스를 호출해 준다.
- 즉, 클래스에 \_\_call__ 메서드를 정의했으므로 함수처럼 괄호()를 붙여서 호출할 수 있다.


```python
# @데코레이터를 지정하지 않음
def hello():    
    print('hello')
 
trace_hello = Trace(hello)    # 데코레이터에 호출할 함수를 넣어서 인스턴스 생성
trace_hello()                 # 인스턴스를 호출. __call__ 메서드가 호출됨
```

## 42.5 클래스로 매개변수와 반환값을 처리하는 데코레이터 만들기
- 클래스로 만든 데코레이터도 매개변수와 반환값을 처리 할 수 있다.


```python
class Trace:
    def __init__(self, func):    # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func         # 호출할 함수를 속성 func에 저장
 
    def __call__(self, *args, **kwargs):    # 호출할 함수의 매개변수를 처리
        r = self.func(*args, **kwargs) # self.func에 매개변수를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
                                            # 매개변수와 반환값 출력
        return r                            # self.func의 반환값을 반환
 
@Trace    # @데코레이터
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add(a=10, b=20))
```

- 클래스로 매개변수와 반환값을 처리하는 데코레이터를 만들때는 \_\_call__ 메서드에 매개변수를 지정한다. 
- self.func에 매개변수를 넣어서 호출한 뒤에 반환값을 반환해 준다. 
- 여기서 매개변수를 *args, *\*kwargs로 지정했으므로 self.func에 넣을 때는 언패킹한다. 
- 고정된 매개변수를 사용할 때는 def \_\_call__(self, a, b) : 처럼 만들어도 된다.

### 42.5.1 클래스로 매개변수가 있는 데코레이터 만들기
- 매개변수가 있는 데코레이터를 만들어보자


```python
# 함수의 반환값이 특정 수의 배수인지 확인하는 데코레이터 
class IsMultiple:
    def __init__(self, x):         # 데코레이터가 사용할 매개변수를 초깃값으로 받음
        self.x = x                 # 매개변수를 속성 x에 저장
 
    def __call__(self, func):      # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):         # 호출할 함수의 매개변수와 똑같이 지정(가변 인수로 작성해도 됨)
            r = func(a, b)         # func를 호출하고 반환값을 변수에 저장
            if r % self.x == 0:    # func의 반환값이 self.x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r               # func의 반환값을 반환
        return wrapper             # wrapper 함수 반환
 
@IsMultiple(3)    # 데코레이터(인수)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add(2, 5))

```

- \_\_init__메서드에서 데코레이터가 사용할 매개별수를 초깃값으로 받는다.
- 그리고 매개변수를 \_\_call__메서드에 사용할 수 있도록 속성에 저장한다. 
- 지금까지 \_\_init__에서 호출할 함수를 매개변수로 받았는데, 여기서는 **데코레이터가 사용할 매개변수**를 받는다는 점.
- \_\_call__메서드에서 호출할 함수를 매개변수로 받는다. 
- 그리고 \_\_call_-메서드 안에 wrapper함수를 만들어 준다. 이때 wrapper함수의 매개변수는 호출할 함수의 매개변수와 똑같이 지정한다.
- wrapper함수안에서는 func의 반환값이 데코레이터 매개변수 x의 배수인지 확인한다.
- 이때, 데코레이터 매개변수 x 는 속성에 저장되어 있으므로 self.x로 사용해야 한다.
- 배수확인이 끝났으면 func의 반환값을 반환한다. 
- 마지막으로 wrapper함수를 다 만들었으면 return값으로 wrapper함수를 반환한다.

- 데코레이터는 기존 함수를 수정하지 않으면서 추가 기능을 구현할 때 사용한다. 
- 보통 데코레이터는 프로그램의 버그를 찾는 디버깅, 함수의 성능 측정, 함수 실행 전에 데이터를 확인하는 등에 활용

## 42.6 퀴즈


```python
# 1. 다음 중 함수 sub에 데코레이터 trace를 지정하는 방식으로 올바른 것을 고르세요. (d)

a) 
def sub(a, b): @trace
    return a - b

b) 
def sub(a, b): trace
    return a - b

c)
@sub
def trace(a, b):
    return a - b

d)
@trace
def sub(a, b):
    return a - b

e)
def sub(trace, a, b):
    return a - b
```


```python
2. 클래스로 데코레이터를 만들 때 구현해야 하는 메서드는 무엇인가요? (메서드 뒤의 괄호는 생략하고 메서드 이름만 입력)
__call__
```

## 42.7 연습문제
> 데코레이터로 매개변수의 자료형 검사하기 

- 데코레이터 type_check를 작성하세요.
- type_check는 함수의 매개변수가 지정된 자료형(클래스)이면 함수를 정상적으로 호출하고, 
- 지정된 자료형과 다르면 RuntimeError 예외를 발생시키면서 '자료형이 다릅니다.' 에러메시지를 출력해야 합니다.
- 여기서 type_check에 지정된 첫번째 int는 호출할 함수에서 첫번째 매개변수의 자료형을 뜻하고 
- 두번째 int는 호출할 함수에서 두번째 매개변수의 자료형을 뜻합니다. 


```python
def type_check(type_a, type_b):
    def real_decorator(func):
        def wrapper(a, b):
            if isinstance(a, type_a) and isinstance(b, type_b):
                return func(a, b)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
    return real_decorator

@type_check(int, int)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add('hello', 'world'))
```

## 42.8 심사문제
> HTML 태그 데코레이션 만들기

- 표준입력으로 HTML 태그 이름 두개가 입력된다.
- 다음 소스 코드에서 함수의 반환값을 HTML 태그로 감싸는 데코레이터를 만들기
- HTML태그는 웹 페이지에 사용하는 문법이며 \<span> 문자열 \</span>, \<p> 문자열 \</p> 처럼
- <태그이름>으로 시작하며 </태그이름>으로 끝난다


```python
# 메서드로 데코레이터 만들기
def html_tag(tag) :
    def real_decorator(func) :
        
        @functools.wraps(func)
        def wrapper() : 
            return f'<{tag}>{func()}</{tag}>' # '<{0}>{1}</{0}>'.format(tag, func()) #
        return wrapper 
    return real_decorator
                     
a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello() :
    return 'Hello, world!'

print(hello())
```

- return을 사용한 이유 : 
- print()를 사용하면 안되는 이유 : 띄어쓰기, 순서가 뒤바뀜


```python
# 클래스로 데코레이터 만들기
class html_tag : 
    def __init__(self, tag) : 
        self.tag = tag
        
    def __call__(self, func) :
        def wrapper() : 
            return f'<{self.tag}>{func()}</{self.tag}>'
        return wrapper 
    
a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello() :
    return 'Hello, world!'

print(hello())
```
