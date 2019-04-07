# find binary in a recursive way

def base2(self, N):
    if N == 0 or N == 1: return str(N)
    return self.base2(N >> 1) + str(N & 1)

def baseNeg2(self, N):
	if N == 0 or N == 1: return str(N)
    return self.base2(-(N >> 1)) + str(N & 1)