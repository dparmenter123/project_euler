from utils import timeit


def factorial_factory(N):
    result = {}
    total = 1
    for i in range(N):
        if i == 0:
            result[i] = 1
        else:
            total *= i
            result[i] = total
    return result
        
@timeit
def solution():
    factorials = factorial_factory(101)
    count = 0
    for n in range(101):
        for r in range(1, n, 1):
            if factorials[n] / (factorials[r] * factorials[n-r]) > 1000000:
                count += 1            
    return count

################################################################
#
################################################################
if __name__ == "__main__":
    print '\nsolution:', solution()
