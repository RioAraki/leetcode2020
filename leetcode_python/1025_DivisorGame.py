def divisorGame(self, N: int) -> bool:
        
    def isPrime(N):
        for i in (2, N):
            if N % i == 0:
                return False
        return True
    
    return N % 2 == 0 and not isPrime(N)
        