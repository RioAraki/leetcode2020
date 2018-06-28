import heapq

def nthSuperUglyNumber(n, primes):
    uglies = [1]
    def gen(prime):
        for ugly in uglies:
            yield ugly * prime
            print
    merged = heapq.merge(*map(gen, primes))
    print (merged)
    # while len(uglies) < n:
    #     ugly = next(merged)
    #     if ugly != uglies[-1]:
    #         uglies.append(ugly)
    # return uglies[-1]

if __name__ == "__main__":
    nthSuperUglyNumber(4, [2,3,7,13])