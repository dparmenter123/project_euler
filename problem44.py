def generate_pentagonals():
    '''
     return the next pentagonal in the form of a triple:
      (ordinal, distance to prev, pentagonal)
    '''
    n = 1
    delta = 1
    current = 1

    while True:
        next = current + delta + 3
        yield n+1, next
        delta = 3 * n + 1
        n += 1
        current += delta

def abs(x):
    if x < 0:
        return x * -1
    return x

def main():

    # we keep a list of pentagonals, and a list of candidates for the A part of A+B
    # for ordered lookup
    pentagonal_array = [1] 
    # for speedy lookup
    pentagonal_set = set([1])   
    # deltas is a set of differences from this pentagonal to all previous
    deltas = []                
    for n, P in generate_pentagonals():
        pentagonal_array.append(P)
        pentagonal_set.add(P)
        for i in range(len(deltas)):
            deltas[i] += 3 * (i+1)
            if deltas[i] in pentagonal_set:
                B = deltas[i]
                A = pentagonal_array[-1 * i - 2]
                # A + B is pentagonal
                if abs(A-B) in pentagonal_set:
                    # and the inverse! Hope this is the right one.
                    return abs(A-B)
        deltas.append(P-1)
    
print main()
