from utils import timeit, digitize

@timeit
def solution():
    MAX = 100
    maxsum = 0
    for a in range(1, MAX):
        for b in range(1, MAX):
            maxsum = max(maxsum, sum(digitize(a ** b)))
    return maxsum

################################################################
#
################################################################
if __name__ == "__main__":
    print '\nsolution:', solution()
