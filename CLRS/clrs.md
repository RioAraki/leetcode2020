# CLRS Notes
一些阅读笔记，因为已经上了很多算法课，很多基础的内容会十分简略，重在查漏补缺和所有pseudocode的实例化（python）。

## Chapter 1 Foundations

### 1. Role of algorithms

#### 1.1/1.2

大概综述一下算法的定义和历史

### 2. Getting Started

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




