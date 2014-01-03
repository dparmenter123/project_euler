from utils import digitize, numberize

from itertools import permutations, combinations
from collections import defaultdict

checked = set()

def digits():
    '''
    :returns a trailing digit, and a list containing all the interstitial
    digits for that trailing digit. Ordered by length.
    '''
    d = defaultdict(list)
    # for each trailing digit
    # and each leading digit
    # gather the total number of digits implied
    for digit in range(10):
        for multiple in [1,2,3,4,5,6]:
            leading = multiple
            if leading not in d[digit]:
                d[digit].append(leading)
            trailing = digit * multiple % 10
            if leading != trailing:
                if trailing not in d[digit]:
                    d[digit].append(trailing)
            else:
                if d[digit].count(leading) < 2:
                    d[digit].append(leading)

    keys = sorted(d.items(), key=lambda x: len(x[1]))
    return [(key[0], sorted(d[key[0]])) for key in keys]



def test(leading, trailing, possibles):
    if tuple([leading]+[trailing] + possibles) in checked:
        return 0
    checked.add(tuple([leading]+[trailing] + possibles))
    if ((leading + trailing + sum(possibles)) % 3) != 0:
        return 0
#    print [leading] + sorted(possibles) + [trailing]

    for perm in permutations(possibles):
        candidate = [1] + list(perm) + [trailing]
        c = numberize(candidate)
        base = sorted(candidate)
        found = 0
        for factor in [6,5,4,3,2]:
            z = c*factor
#            print c, z, base, sorted(digitize(z))
            if sorted(digitize(z)) != base:
                if found > 2:
                    print 'almost', c, factor
                break
            else:
                found += 1
        else:
            print '**!!!', c
            return c
    return 0

def solution():
    length = 1
    while True:
        print '***', length
        candidates = []
        for trailing, possibles in digits():
            if length >= len(possibles):
                max_padding = length - len(possibles)
                leading = 1 # always
                possibles.remove(leading)
                possibles.remove(trailing)
                for padding in range(max_padding + 1):
                    for pad in combinations(range(10), padding):
                        candidate = test(leading, trailing, possibles + list(pad))
                        if candidate > 0:
                            candidates.append(candidate)

        if len(candidates) > 0:
            return sorted(candidates)[0]
        length += 1
    return 0

################################################################
#
################################################################
if __name__ == "__main__":
    print '\nsolution:', solution()
