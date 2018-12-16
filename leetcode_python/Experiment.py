def exp():
    num1 = 1
    lst1 = [1,2,3]
    lst2 = [1,2,3]
    def exp2():
        num2 = num1
        lst1.append(1)
        lst2[0] = 0
    exp2()

    print(lst1)
    print(lst2)

exp()