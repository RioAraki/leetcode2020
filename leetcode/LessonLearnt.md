一般考虑回答以下几个问题：
  1. 有没有什么子操作卡住了（意味着语言的标准库，基本api不熟）
  2. 有没有什么概念不确定 （比如 Life scope，某一 function return 什么不确定）
  3. 如果看了别人的答案，有没有学到什么（简洁的写法，骚操作，不知道的库 / api）
  4. 如果题目卡住了，为什么？犯了哪些错误。如果我的答案不高效，哪里的问题？为什么别人的更高效？

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


问：为什么 function in class 要有 self parameter，没有会怎么样？

问：如果 create a class instance 不带括号意味着什么？