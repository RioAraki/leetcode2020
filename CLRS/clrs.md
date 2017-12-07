
# CLRS Notes
一些阅读笔记，因为已经上了很多算法课，很多基础的内容会十分简略，纯粹写给自己看的，不一定有参考价值，重在查漏补缺和所有pseudocode的实例化（python）。

## Chapter 1 Foundations

### **1. Role of algorithms**

#### 1.1/1.2

大概综述一下算法的定义和历史

### **2. Getting Started**

#### 2.1 Insertion sort

**实现一个 insertion sort**:

```
def insertion_sort(lst):
    for idx in range(1, len(lst)):
        position = idx
        value = lst[idx]
        while position > 0 and lst[position-1] > value:
            lst[position] = lst[position-1]
            position -= 1
        lst[position] = value 
    return lst
```
引出概念：**loop invariant**，在不断loop的过程中（严谨的说，从 loop 开始前直到 loop 结束后）始终保持不变的一个 statement。在这个例子里则是 list 中
lst[position-1[ 的部分始终是 sorte d的。loop invariant 有**三个重要的组成部分**：initialization, maintainance, termination。**initialization** 表示 loop invariant 在每次 loop 开始前是成立的，**maintainence** 表示 loop invariant 在进行了本次 loop 后依然是成立的，**termination** 表示所有 loop 结束后 loop invariant 依然是成立的。其推理过程其实很像数学归纳法

**2.1 exercise**

2.1-3 值得一看，让你写 linear search 的算法，找到其 loop invariant 并证明你的算法是正确的，关键在于 loop invariant 的提出和严谨的证明过程。我在这个 [repository](https://github.com/gzc/CLRS/blob/master/C02-Getting-Started/2.1.md) 里写了我的答案，可以参考。

#### 2.2 Analyzing algorithms

从现实角度阐述了一些 analyze的基本原则，并强调了 input size 和 running time 的概念。以刚刚 insertion sort 为例，逐行分析了其 cost 和 run times，并用数学公式算了下，发现复杂度是 quadratic 的。随后引入了 worst-case 和 avg-case analysis 和 order of growth 的概念

**2.2 exercise**

2.2-2: **实现一个 selection sort**:
```
def selection_sort(lst):
    for idx in range(len(lst)-1):
        min = idx
        for j in range(idx+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[idx], lst[min] = lst[min], lst[idx]
    return lst
```

#### 2.3 Designing algorithms

以 divide and conquer 为切入教大家设计算法。

##### 2.3.1 The divide-and-conquer approach

Divide and conquer 的思路： **Divide** problems into numbers of smaller subproblems, **Conquer** each subproblems recursively, **Combine** solutions of subproblems into original problem. 以 merge sort为例：
```
def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L,R = [],[]
    for i in range(n1):
        L.append(A[p+i])
    for j in range(n2):
        R.append(A[q+j+1])
    L.append(float("inf"))
    R.append(float("inf"))
    i, j = 0, 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A
```
注意这里的 merge 算法只有在 A[p:q] 和 A[q:r] 本身就是 sorted 的情况下才有效。有了 merge 这一 function 之后就可以用 divide-and-conquer 思想实现 merge sort 了：
```
def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    return A
```
写这种 recursion 的逻辑时要有一定的抽象性思维，能想象其 base case，并让逻辑最终引导向 base case。不然很容易造成无限 recursion 的情况。比如在这里，不断地 merge-sort 后 p 一定等于 r，这种时候便停止 recursion 直接 return A。

##### 2.3.2 Analyzing divide-and-conquer algorithms

Describe recursive running time -> **recurrence equation**. 熟悉 recurrence equation 的表现形式，能用等比数列求和算出最终 T(n) 等于一个具体的值

### **3. Growth of functions**

顺成上一章中提到的 order of growth 的概念，只有清楚的掌握各种情况随 input size 增加算法复杂度的不同增长速率才能更好地判断算法的 efficiency。

#### 3.1 Asymptotic notation

提出 **θ (theta)-notation**: asymptotic tight bound/ **O-notation:** asymptotic upper bound/ **Ω (omega)-notation**: asymptotic lower bound 的概念。要理解每一项的严谨数学定义。还有两个小概念 0-notation 和 ω-notation(小写)，因为Big-O 和 Big-Ω 表示的 bound 不一定是 tight 的，而我们**用small o 和 ω 表示其不是 asymptotic tight 的情况** (例：2n = o(n^2), 2n^2 != o(n^2)，因为在所有情况下2n的增长速度都小于 cn^2，但在某些情况下2n^2 增长速度大于 cn^2，比如当 c = 1 时)，总的来说 o/ω 比 O/Ω 来的更严格。

#### 3.2 Standard notations and common functions

Monotocity/ Floors and ceilings/ modular arithemtic/ polynomials (**x**^c)/ exponentials (c^**x**)/ logarithms/ factorials

大多是高中数学概念，不展开了。

### **4. Divide-and-Conquer**

进一步讨论 divide-and-conquer，提出 recurrsive case/ base case。三种计算 recurrence 的方法： 
* **substitution method**: guess a bound then use mathematical induction to prove our guess correct
* **recursion-tree method**: convert recursion into a tree whose nodes represent the costs incurred at various levels of recursion.Use techniques for bounding summations to solve recurrence.
* **master method**

**Technicalities in recurrences**

Omit floor/ ceiling/ boundary conditions，这些内容从宏观层面来说对判断算法复杂度无关紧要，故舍弃。

#### 4.1 The maximum-subarray problem

用 divide-and-conquer 思路解答这个问题：maximum-subarray 一定存在于这个 array 的左半边/ 右半边/ 横穿两边。考虑这三种情况，在左半边/ 右半边的情况就是 recursive case 了，因为你要做的事情是一样的，只不过 array 本身长度变成了一半。而位于中间时则是一个不同的问题，从中间的点开始不断朝左右延展找到最大的差值。最后比较三种情况，并取其最大者作为答案。

```
def find_max_crossing_subarray(A, low, mid, high):
    left_sum, right_sum = -float("inf"), -float("inf")
    sum_ = 0
    for i in reversed(range(low, mid+1)):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i
    sum_ = 0
    for j in range(mid+1, high+1):
        sum_ += A[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j
    return (max_left, max_right, left_sum + right_sum)
```
在 python 里 range(0:4) 只包含 [0,1,2,3]，非常容易搞错。无论如何以上实现了从中间一点查找两边的 max subarray的情况。接下来则是 recursion 部分：
```
def find_maximum_subarray(A,low,high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = math.floor((low+high)/2)
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
    if right_sum > left_sum and right_sum > cross_sum:
        return (right_low, right_high, right_sum)
    elif left_sum > right_sum and left_sum > cross_sum:
        return (left_low, left_high, left_sum)
    else:
        return (cross_low, cross_high, cross_sum)
```

**Analyzing the divide-and-conquer algorithm**

逐行分析需要的 runtime，由于每次 subcase 会变成原来长度的一半，所以 T(n) = 2T(n/2) + θ(n)。最终结果是 T(n) = θ(nlogn)，比需要 n^2 的 brutal force 情况好上不少。











































