一般考虑回答以下几个问题：
  1. 有没有什么子操作卡住了（意味着语言的标准库，基本api不熟）
  2. 有没有什么概念不确定 （比如 Life scope，某一 function return 什么不确定）
  3. 如果看了别人的答案，有没有学到什么（简洁的写法，骚操作，不知道的库 / api）
  4. 如果题目卡住了，为什么？犯了哪些错误。如果我的答案不高效，哪里的问题？为什么别人的更高效？

Q888. Uncommon words from two sentences

sub-operation: make a dictionary from a list which key is all non duplicate element from list and value is number of times key appears

Python collections library -> counter

The better solution has a better understanding on "uncommon words", eliminate comparison between two lists.
======================================= 

Q889. Spiral Matrix III

之前学到的 turn 的简单实现：
```
self.d = (0,1)

def turnLeft(self):
    self.d = (-self.d[1], self.d[0])

def turnRight(self):
    self.d = (self.d[1], -self.d[0])
```

对于spiral理解有误，每次有效移动的距离要比之前+1，如果遇到 out of border 的情况，距离不变，切换方向。

问： 不确定 class 的 variable，里面的function能否直接看到并修改？

这个问题可以拆成两个相关方面 
	1. class 和 variable
	2. variable in different scope 

1. 有关 class 和 variable

OOP 中 variable可以有 class level, instance level.

Class variables -> class level, variable consistent across instances.

```
class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5
```

Defined within class construction, they are owned by class itself, sharted by all instances of the class.

Instance variables -> may change significantly across instances.

```
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

2. Python scoping rules
LEGB Rule.

https://stackoverflow.com/questions/291978/short-description-of-the-scoping-rules

L, Local — Names assigned in any way within a function (def or lambda)), and not declared global in that function.

E, Enclosing-function locals — Name in the local scope of any and all statically enclosing functions (def or lambda), from inner to outer.

G, Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def within the file.

B, Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...

例：
```
code1
class Foo:
   code2
   def spam.....
      code3
      for code4..:
       code5
       x()
```
In what order would x() found?
	The for loop does not have its own namespace.

	L : local, in def spam (in code3, code 4, code5).

	E : Enclosed function, any enclosing functions (if the whole example were in another def)

	G : Global. Were there any x declared globally in the module (code1)?

	B : Any builtin x in Python.

**x will never be found in code2**

Beyond the 4 basic scope LEGB, there is a special scope the **class body**, which does not comprise an enclosing scope for methods defined within the class. Any assignments within the class body make the variable from there on be bound in the class body.

Especially, no block statement, besides def and class, create a variable scope. In Python 2 the list comprehension does not create a variable scope, however in Python 3 the **loop variable** is created in a new scope.

```
x = 0
class X(object):
    y = x
    x = x + 1 # x is now a variable 
    z = x

    def method(self):
        print(self.x) # -> 1
        print(x)      # -> 0, the global x
        print(y)      # -> NameError: global name 'y' is not defined

inst = X()
print(inst.x, inst.y, inst.z, x) # -> (1, 0, 1, 0)
```

If a name is ever assigned to in the current scope (except in the class scope), it will be considered belonging to that scope, otherwise it will be considered to belonging to any enclosing scope that assigns to the variable (it might not be assigned yet, or not at all), or finally the global scope. If the variable is considered local, but it is not set yet, or has been deleted, reading the variable value will result in UnboundLocalError, which is a subclass of NameError.

```
x = 5
def foobar():
    print(x)  # causes UnboundLocalError!
    x += 1    # because assignment here makes x a local variable within the function, no error if without x+=1

# call the function
foobar()
```

In python 2 there is no easy way to modify the value in the enclosing scope; usually this is simulated by having a mutable value, such as a list with length of 1:

```
def make_closure():
    value = [0]
    def get_next_value():
        value[0] += 1
        return value[0]

    return get_next_value

get_next = make_closure()
print(get_next()) # -> 1
print(get_next()) # -> 2
```

In python3, we have **nonlocal**

```
def make_closure():
    value = 0
    def get_next_value():
        nonlocal value
        value += 1
        return value
    return get_next_value

get_next = make_closure() # identical behavior to the previous example.

```

问：为什么 function in class 要有 self parameter，没有会怎么样？

问：如果 create a class instance 不带括号意味着什么？
