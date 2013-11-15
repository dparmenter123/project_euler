'''
 ....word
 ...w.ord
 ..w..ord
 .w...ord
 w....ord
 w...o.rd
 w...or.d
 ....word
'''

WORD = 'WORD'
SPACES = 4

def recurse(spaces, letter, result):
    # if we've processed all the input, we have a unique result, return it
    if spaces == 0 and letter == len(WORD):
        print ''.join(result)
        return
    # we still have work to do
    if spaces > 0:
        # recurse on the space
        recurse(spaces - 1, letter, result + ['.'])
    if letter < len(WORD):
        # recurse on the letter
        recurse(spaces, letter + 1, result + [WORD[letter:letter+1]])

def recursive_solution():
    result = []
    recurse(4, 0, result)

recursive_solution()
