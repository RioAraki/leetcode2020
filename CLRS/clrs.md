
# CLRS Notes
一些阅读笔记，因为已经上了很多算法课，很多基础的内容会十分简略，纯粹写给自己看的，不一定有参考价值，重在查漏补缺和所有pseudocode的实例化（python）。

## Chapter 1 Foundations
***
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

逐行分析需要的 runtime，由于每次 subcase 会变成原来长度的一半，所以 T(n) = 2T(n/2) + θ(n)。最终结果是 T(n) = θ(nlogn)，比需要 n^2 的 brutal force 情况好上不少，不写详细了。


#### 4.2 Strassen's algorithm for matrix multiplication

如何计算两个方形矩阵相乘，按照矩阵相乘的数学原理来看：
```
def square_matrix_multiplicy(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
```
以上是从数学角度计算，可以看出有三个 for loop 嵌套，整体 runtime 应该在 n^3，并不高效。这里介绍了一种用 divide-and-conquer 的方法，见图：

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/41c6337190684aff7b69f124226d6e62d79ebca5)

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/480fbf677c5973cedb5218c69501a41e1b325a1a)

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8d91fa79d27697a5c6551698c1a83a3d5837c57b)

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/a08bea24eec9422cda82e6e04af1d96fc6822038)

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/7adffe97db091ce8ba231352b3721bbe261985ca)

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b40ed74cf54465d8e54d09b8492e50689928313)

按照这个思路，我们可以写出：

```

def matrix_add(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def square_matrix_multiply_recursive(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    if n == 1:
        C[0][0] = A[0][0]*B[0][0]
    else:
        half = len(A/2)
        C[:half][:half] = matrix_add(square_matrix_multiply_recursive(A[:half][:half], B[:half][:half]),
                                     square_matrix_multiply_recursive(A[:half][half:], B[half:][:half]))
        C[:half][half:] = matrix_add(square_matrix_multiply_recursive(A[:half][:half], B[:half][half:]),
                                     square_matrix_multiply_recursive(A[:half][half:], B[half:][half:]))
        C[half:][:half] = matrix_add(square_matrix_multiply_recursive(A[half:][:half], B[:half][:half]),
                                     square_matrix_multiply_recursive(A[half:][half:], B[half:][:half]))
        C[half:][half:] = matrix_add(square_matrix_multiply_recursive(A[half:][:half], B[:half][half:]),
                                     square_matrix_multiply_recursive(A[:half][:half], B[half:][half:]))
    return C
```
而 runtime是 T(n) = 8T(n/2) + θ(n^2)，每次的 subcase size 都是原本的一半 （**？这里对书存个疑，如果是两个矩阵相乘的情况，当两个矩阵长宽都是之前的一半时整体input size不应该是之前的 1/16 嘛，为什么是一半呢？**），其实复杂度还是 θ(n^3)，并没有什么改善。

**Strassen's method**

核心: instead of performing **8** recursive n/2 * n/2 multiplications, perform only **7**

具体过程其实也十分有意思，但太数学了，可以看 wiki [相关页面](https://en.wikipedia.org/wiki/Strassen_algorithm)。

**4.2 Exercise**

4.2-2 是说 strassen's algorithm 的算法实现，如下：
```
def matrix_add(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrix_sub(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C


    return

def strassen_algo(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        half = len(A)/2
        A11 = A[:half][:half]
        A12 = A[:half][half:]
        A21 = A[half:][:half]
        A22 = A[half:][half:]
        B11 = B[:half][:half]
        B12 = B[:half][half:]
        B21 = B[half:][:half]
        B22 = B[half:][half:]

        M1 = strassen_algo(matrix_add(A11, A22), matrix_add(B11, B22))
        M2 = strassen_algo(matrix_add(A21, A22), B11)
        M3 = strassen_algo(A11, matrix_sub(B12, B22))
        M4 = strassen_algo(A22, matrix_sub(B21, B11))
        M5 = strassen_algo(matrix_add(A11, A12), B22)
        M6 = strassen_algo(matrix_sub(A21, A11), matrix_add(B11, B12))
        M7 = strassen_algo(matrix_sub(A12, A22), matrix_add(B21, B22))

        C[:half][:half] = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
        C[:half][half:] = matrix_add(M3, M5)
        C[half:][:half] = matrix_add(M2, M4)
        C[half:][half:] = matrix_add(matrix_add(matrix_sub(M1, M2), M3), M6)
    return C

```

#### 4.3 The substitution method for solving recurrences

用 substitution method 来计算 recurrence 的 runtime, 包含两步：
1. Guess the form of the solution
2. Use mathematical induction to find the constants and show that the solution works

由于这个方法先要靠猜测一个答案再验证的方法来实践，非常不系统，暂时跳过。


#### 4.4 The recursion-tree method for solving recurrences


把 recursion 的过程用 tree 的形式分成不同阶层表达出来。总结每一个阶层的 runtime，并最后加到一起做成等式，再化简。找出 tree 的规律不难，难点在于用数学的方法把最后找出的等式化简。


#### 4.5 The master method for solving recurrences

只限于 T(n) = aT(n/b) + f(n) 的形式。用 [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) 对号入座。


### **5. Probabilistic Analysis and Randomized Algorithms**

Probabilitistic analysis and randomized algorithms，需要有概率学基础。


#### 5.1 The hiring problem

See question [here](https://en.wikipedia.org/wiki/Secretary_problem), 最基础的算法实现：

```
# assume n is a list of numbers, the larger the number the better the people would be
def hire_assistant(n):
    best = -1
    for i in range(len(n)):
        # interview i
        if n[i] > best:
            best = i
            # hire i

```
比起分析代码的 runtime 更在意代码的的 cost，设 cost of interviewing = i, cost of hiring = h, total people = n, total people hired = m, 那我们的 runtime 是 O(C<sub>i</sub> m + C<sub>h</sub>m).

**Worst-case analysis**

每一个人都比前一个人更好，雇佣了所有人： O(C<sub>i</sub>n + C<sub>h</sub>n)

**Probabilistic analysis**

但最坏的雇用所有人的情况其实很难出现，我们更应该假设每天前来得人的素质是随机的 ( uniform random permutation) ，而基于这个假设我们能给出算法的 average-case runtime.

**Randomized algorithms**

为了进行 probabilstic analysis, 我们起码要对 input 有所了解，甚至有时即便我们知道 input distribution，我们依然无法根据 input 建模从而进一步分析。在 hiring problem 中，我们希望能对 input 有更多的控制，所以我们改为**每天随机抽取一些候选人进行面试 （而不是面试所有人）**。

We call an algorithm **randomized** if its behavior is determined not only by its input but also by values produced by a random-number generator. 当分析这种 randomized algorithm 时，他的 runtime 和 random number generator 提供的 input value 是息息相关的。

#### 5.2 Indicator random variables

总的来说 indicator random variables 是某一事件发生一种情况的概率？ *（其实这里不是很理解这个东西和单纯的 pr(x) 有什么区别）* 总的来说应该只是一种比较方便的表达方式

*Lemma 5.1: Given a smaple space S and an event A in the sample space S, let X<sub>A</sub> = I{A}, then E[X<sub>A</sub>] = Pr{A}*

**Analysis of the hiring problem using indicator random variables**

对于 hiring problem，可以假设雇佣的次数为 X，而 X<sub>1</sub>,<sub>2</sub>,<sub>3</sub>,<sub>4...</sub> 表示具体雇佣某个人的 indicator random variable，而因为每个人的质量是随机的，所以第一个人被雇佣的概率为 1（第一个人没人和他抢，必定被雇佣），第二个人为 1/2（一半几率比第一人好，一半几率比第一人差），第三个为 1/3，以此类推。最终总雇佣的次数 X = X<sub>1</sub> + X<sub>2</sub> + ... + X<sub>n</sub> = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n ，可以看出这就是一个 [harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics))，而 harmonic series 求和答案为 ln(n)。

*lemma 5.2: Assuming that the candidtaare presented in a random order, algorithm hire-assistant has an average case total hiring cost of O(c<sub>h</sub> ln n)*

#### 5.3 Randomized algorithms

首先要强调的是，**probabilistic analysis 和 randomized algorithms 是连个完全不同的概念。** 具体来说，在我们做 probabilistic analysis 时，我们会先把 input 做随机处理，而算法本身是稳定的，所以在 input 不变的前提下，算法得出的结果也是不变的，。而 randomized algorithm 则强调在算法**内部**去做random，而不是把 input 先 random 好再输入给算法。所以我们每次 run 这个算法时，得到的结果可能都是不一样的。以 hiring problem 为例，我们先在算法中随机排列所有的候选人，然后再进行挑选。书中提供了两种随机排列所有候选人的方法，并作出了十分详细的证明，这里只给出代码示例：
```
def permute_by_sorting(A):
    n = len(A)
    P = [0 for x in range(n)]
    dict = {}
    for i in range(n):
        P[i] = random.randint(i, n**3) # **3 just because its unlikely there are two same P[i]
        dict[str(A[i])] =  P[i]

    return sorted(dict, key=dict.get)
    
def randomize_in_place(A):
    n = len(A)
    for i in range(n):
        ran = random.randint(i, n)
        A[i], A[ran] = A[ran], A[i]
    return A
```
有了这两种方法后，我们可以真正实现 randomized algorithm:
```
def randomized_hire_assistant(n):
    n = randomize_in_place(n)
    # or:
    # n = permute_by_sorting(n)
    best = -1
    for i in range(len(n)):
        # interview i
        if n[i] > best:
            best = i
            # hire i
```

#### 5.4 Probabilistic analysis and further uses of indicator random variables

##### 5.4.1 The birthday paradox

##### 5.4.2 Balls and bins

##### 5.4.3 Streaks

##### 5.4.4 The on-line hiring problem


## Chapter 2 Sorting and Order Statistics
***
再提供几种 sorting algorithm 的思路，之前介绍了 insertion sort 和 merge sort，本大章会再介绍两种 sorting algorithm （heap sort 和 quick sort）和一些别的。
![sort runtime](http://www2.hawaii.edu/~nodari/teaching/f15/Notes/Topic-10/comparing-sorts.jpg)

### 6. Heapsort

heap sort 有着 O（n log n）的 running time，并且使用名为 heap 的数据结构。

#### 6.1 Heaps

Heap: heap 的实质就是一个 array，但可以以二叉树的形式的去理解它。二叉树的每一个 node 都对应 array 相同 index 的那个 element。heap 有两个性质： length 和 size， length 为其二叉树形式的高度， size 为其一共有的元素数。
![heap](http://dotnetlovers.com/images/coolnikhilj22fe9593ef-2e15-46e5-9799-f0965d2bb668.png?2/8/2016%2011:33:06%20PM)

还有一个算是性质的是，作为二叉树我们可以很轻松的算出 parent node 和 left/ right child 之间 index 的关系，从上面的图也是可以轻易看出来的:

```
left_child = parent*2
right_child = parent*2+1
```

Heap 分为 max/min heap 两种，分别满足 **max/min heap property：for all nodes i other than the root, A[parent(i)] >= (or <=) A[i]**

#### 6.2 Maintaining the heap property

让一个 array 中的某一个特定 index 的 element 满足 max heap property，保证把这个 index 的 element 放到 array 中正确的位置上:

```
# A -> a list of number
# i -> index i 
def max_heapify(A, i):
    l = i*2
    r = i*2+1
    if l <= len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
```

runtime 分析，这是一个典型的 recursion，用 master theorem 可得 T(n) = O(logn)

#### 6.3 Build a heap

之前的 max-heapify 算法保证针对某一个 element 可以把它调整到 array 中正确的位置，那如果对所有 element 施行 max-heapify 就可以保证整个 array 都满足 max heap property 了。而实际上，并不需要对**所有** element 进行 max-heapify 也能达到 整个 array 满足 max heap property 的效果， 因为所有的 leaves 没有 children node，所以自动满足 max heap property （记得 max heap property 的定义是 parent node >= child node，而 leaf 是没有 child node 的）。那只需要对所有非 leaf 的 node 进行 max-heapify 就行了，代码如下：

```
# A -> list of number
def build_max_heap(A):
    size = len(A)
    for i in range(size//2-1)[::-1]:
        max_heapify(A, i)
```

Running time 是 O(n)，书上有详细的证明

#### 6.4 The heapsort algorithm

首先不能搞混的是，满足 max (min) heap property 的 array 不一定是 sorted 的，只有root是最大的这一点可以肯定。所以哪怕我们有了一个 max/min heap，依然要对其进行 sort，只不过这个过程简单了不少，因为我们知道 root永远是最大的，只要把 root 和末尾 exchange，把末尾排除出 heap，再对第一位进行 max-heapify 就能保证新的 heap 的 root 又是最大的，再将其排除。如此反复，便得到一个由小到大排列的 array 了。代码如下:

```
# A -> list of number
def heapsort(A):
    build_max_heap(A)
    len = len(A)
    for i in range(1, len-1)[::-1]:
        A[0], A[i] = A[i], A[0]
        len -= 1
        max_heapify(A,0)
```

heap sort 的 runtime 是 O(n log n)。

#### 6.5 Priority queues

heap 作为一种 data structure 在很多地方可以用到，比如作为 priority queue.
**A priority queue is a data structure for maintaining a set S of elements, each with an associated value called a key.** 正常来说一个 priority queue 需要支持一下操作：

  - insert(S,x): 把 element x insert 到 set S 里，runtime 为 O (logn)
```
def max_heap_insert(A, key):
    A.append(-float("inf"))
    heap_increase_key(A, len(A)-1, key)
```
  - maximum(S): return largest key in S，runtime 为 O (1)

```
def heap_maximum(A):
    return A[0]
```

  - extract-max(S): 把拥有最大 key 的 element 抽出来并保证剩下部分的 list 还是 max heap，runtime 为 O (logn)

```
def heap_extract_max(A):
    if len(A) < 1:
        return False
    max = A[0]
    A[0] = A[-1]
    A = A[:-1]
    max_heapify(A, 0)
    return max
```

  - increase-key(S, x, k): increase the value of element x's key to a new value k，runtime 为 O (logn)

```
def heap_increase_key(A,i,key):
    if key < A[i]:
        return False
    A[i] = key
    while i > 0 and A[i//2] < A[i]:
        A[i], A[i//2] = A[i//2], A[i]
        i = i//2
```

### 7. Quicksort

worst case 的 runtime 只有 O(n<sup>2</sup>)，但在实践中往往是最好的，有着 avg runtime O(n log n)。由于他不占用额外空间 (sort in place) 所以在虚拟内存的环境下也很优秀。

#### 7.1 Description of quicksort

也用 divide and conquer，具体步骤：

  * divide: 把 array A[p .. r] 分成两个 subarray A[p .. **q-1**] 所有 element 小于 A[q], A[**q+1** .. r] 所有 element 大于 A[q].
```
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1  # A[i] > x before swapping
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1
```
可以看到 partition 默认把最后一位作为pivot，使 A 分成比 A[r] 大或小的两个 subarray，但如果 A[r] 正好是array中最大/最小的结果则不如人意。

  * conquer: recursively sort two subarrays by quick sort

  * combine: 两个 subarray 已处于 sorted 状态，所以整个 array 也是 sorted 的。
```
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
```

#### 7.2 Performance of quicksort

如之前所说，performance 严重取决 partition 的过程是否 balanced。在 worst case 下， running time 为 θ(n<sup>2</sup>) （相当于做了一个 insertion sort）。在 best case 下，running time 为 O(nlogn) （相当于做了一个 merge sort）。

在 avg case 下的情况是需要着重讨论的：先说结论，其 performance 为 O(n log n)，十分接近 best case。很多人可能不解，这里书上做了一个假设，说每次 partition 都很不巧，分出来的连个 subarray size 都是 1:9，已经是比较unbalance的极端情况了。而在这种情况下，recurrence 为：

**T(n) = T(9n/10) + T(n/10) + cn**

并有如下 recursion tree:

![quick_sort_recurrence_tree](https://www2.hawaii.edu/~janst/311/Notes/Topic-10/Fig-7-4-quicksort-1-9-recursion-tree.jpg)

对于每次都分得 9/10 大小的 subarray 来说，这种情况一共会持续 log<sub>9/10</sub>n 次 （例：n = 100，每次分成 9:1，则第一次分割成 90:10，长度为 90 的 subarray 又分成 9:1，第二次分割成 81:9，之后可能为 73:8，依次类推，直到大的那端接近 1 无法再分割），这是最大 subarray 的情况。在这种情况下的 runtime 可概括为： T(9n/10) = log<sub>9/10</sub>n = θ(logn)，而每次分割又有 cost cn (相当于 parition 的runtime)，所以总体可概括为 θ(nlogn)，asymptotically speaking 和 merge sort 是一致的。这一点的确比较难理解，比较反直觉。用我自己通俗的话来讲，每次 partition 的过程都是把问题大小指数级降低的过程，哪怕分割的非常不平均。假设 input size 是**无限大**的话，分成 5:5 和分成 9:1 甚至 99:1 都是没有本质差别的。需要用 Asymptotic analysis 的思想去理解这个问题。

#### 7.3 A randomized version of quicksort

和之前 5.3 一样的思想，之前的 quicksort 有一个问题在于一直取最后一位作为 pivot 可能会一直处于 unbalanced 的状态，为了避免这一情况，我们随机取 array 里的一个数并和最后一位交换，再作为 pivot 做 partition 操作。
```
def random_partition(A, p, r):
    i = random.randint(p,r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)
 
 
 def random_quicksort(A, p, r):
    if p < r:
        q = random_partition(A, p, r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)   
```

#### 7.4 Analysis of quicksort

总之 worst case 是 θ(n<sup>2</sup>)，而 avg running time 是 θ(n log n)


# III  Data Structures

Fundamental data structure -> dynamic sets, could be more complicated like dictionary, min-priority queues. Remember the data structure and the required operations.


#### Elements of a dynamic set

key/ value (satellite data)/ attributes that are manipulated by set operations/ etc…

#### Operations on dynamic sets

Search/ insert/ delete/ minimum/ maximum/ successor (may be the next larger element)/ predecessor (next smaller)

## Chapter 10 Elementary Data Structures

### 10.1 Stacks and queues

They are dynamic sets. Stack: LIFO. Queue: FIFO

#### Stacks

(main) Operation supported: Insert -> called PUSH, delete -> called POP.
Implement by keep track of the top element (most recently added element). When stack empty, S.top = 0; underflow -> when we attempt to pop an empty stack; overflow -> when S.top exceeds the size.

Detailed code implementation please check: Stack's implementation in C++

#### Queues

(main) Operation supported: insert -> called enqueue, delete -> called dequeue.
Queue has a head and a tail. Enqueue takes place in tail, dequeue takes place in head.

Detailed code implementation please check: Queue's implementation in C++

### 10.2 Linked lists

Objects are arranged in a linear order. linear order is determined by the array indices, the order in a linked list is determined by a pointer in each object. Linked list provide a simple, flexiable representation for dynamic sets.

Object has attribute: key/ prev/ next, the object may also contain satellite data. head ->, points to first element; tail -> points to last element; head, tail equals null when the linked list is empty.

Linked list could be singly linked or doubly linked, even cirular list (prev pointer of the head points to tail, vice versa). We omit prev pointer in each element for singly linked list. We assume the ordinary linked list is doubly and unsorted.

Operations supported: 
	- `list-search(k)` : find first element with key k by a simple linear search, returning pointer to this element
	- `list-insert(x)` : given element x whose key attribute has been set, list-insert insert x onto the front of the linked list.
	- `list-delete(x)` : given element x from a linked list L, splices x out of list by updating pointers. If we want to delete an element with a given key, we must first call `list-search` to retrieve a pointer to the element.
	
Detailed code implementation please check: Queue's implementation in C++

10.3 Implementing pointers and objects

Ways to implement pointers and objects in language that do not provide them

#### A multiple-array representation of objects

Three dimensional array to keep track of linked list, one array for next/  one array for key/ one array for prev. (in fact we can have one more array for satellite data)

#### A single-array representation of objects

In many programming languages, an object occupies a contiguous set of locations in the computer memory. A pointer is simple the address of the first memory locaiton of the object, add offset get location of other object. So to keep linked list in a single-array, every three slots form an element with key/prev/next.

#### Allocating and freeing objects

To insert a key means we must put it in a currently unused space, so we need to manage the storage of element. In some systems, a garbage collector is reponsible for determining which objects are unused.

Suppose we have multiple-array representation linked list, and we keep free objects in a singly linked list (free list). We can use the 'next' array spot from unused objects to form out free list

Don't see it too meaningful to implement, so skip the implementation part.

### 10.4 Representing rooted trees

#### Binary trees 

Attributes: p/ left/ right to store points to parent left child and right child of each node.

#### Rooted trees with unbounded branching

Replace pointer left and right to child 1 2 3 … . But what if we do not know how many children are there (unbounded)?  We have left-child, right-sibling representation: 
	- x.left_child always points to leftmost child of node x.
	- x.right_sibling points to sibling of x immediately to its right.

#### Other tree representations

Represented as a heap/ a single array plus index of the last node in the heap, a lot of possible ways

Detailed implementation would be done in Binary search tree section.

## Chapter 11 Hash Tables

Dynamic set that supports only dictionary operations like `insert`, `search`, `delete`. Hash table is an effective data structure implmenting dictionaries. In practice search for an element in hash tbale is O(1) with worst case theta(n).

### 11.1 Direct-address tables

Works well when the universe U of keys is reasonably small. Let's say we need a dynamic set which each element has a key drawn from the universe U = {0,1,…,m-1}, m not too large. No two element has the same key. -> We use array, or direct-address table, in which each slot correspond a key.

![direct_address_table]()

The direct-address table itself can hold the elements in the dynamic set (save space), so we don’t need object external to the direct-address table.

### 11.2 Hash tables

If the universe U is large, storing a table T of size U may be impractical. Furthermore, we don’t want to keep so many slots as the keys used would be so small relative to the universe.

We use hash table to resolve this. Instead of save key k in slot k, we hash k and store in h(k). There might be collision (two keys same spot) since we want to limit the number of spots and there might be many keys. Do our best to make the hash result random and average. 

##### Collision resolution by chaining and some analysis.

In chaining, we place all elements that hash to the same slot into same linked list. An unsuccessful search takes avreage 1+length of chain to find the result, assume the hash is simple and uniform.

Dynamic set that supports only dictionary operations like `insert`, `search`, `delete`. Hash table is an effective data structure implmenting dictionaries. In practice search for an element in hash tbale is O(1) with worst case theta(n).

### 11.1 Direct-address tables

