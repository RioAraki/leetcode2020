def profitableSchemes(G, P, group, profit):
    """
    :type G: int
    :type P: int
    :type group: List[int]
    :type profit: List[int]
    :rtype: int
    """
    # find all combinations of sum profit > p
    # check if there are enough people for each combiantion

    from itertools import chain, combinations
    import functools

    def powerset(iterable):
        "list(powerset([1,2,3])) --> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

    gp = list(map(lambda x, y: (x, y), group, profit))
    print(gp)
    power = list(powerset(gp))
    for i in range(len(power)):
        subset = power[i]
        for i in subset:
            if len(power[i]):
                print(functools.reduce(lambda x,y: x+y,power[i]))
if __name__ == "__main__":
    print(profitableSchemes(10, 5, [2,3,5], [7,6,8]))