import sys
from utils import timeit, digitize, numberize

################################################################
#
################################################################

def is_palindrome(digits):
    if len(digits) < 2:
        return True
    if digits[0] != digits[-1]:
        return False
    return is_palindrome(digits[1:-1])

def reverse(N):
    return numberize([x for x in reversed(digitize(N))])

@timeit
def solution(MAX):
    normal = set()
    lychrel = set()
    for original in range(0,MAX):
        current = set()
        A = original
        found = False
        for j in range(51):
            B = reverse(A)
            C = A + B
            current |= set([A])
            if A in lychrel:
                break
            if is_palindrome(digitize(C)) or A in normal:
                # optimization: all of the numbers in the current set are now normal
                normal |= current
                found = True
                break
            A = C
        if not found:
            lychrel |= current

    return len([x for x in lychrel if x < MAX])

################################################################
#
################################################################

if __name__ == "__main__":
    print '\n', solution(10000)
