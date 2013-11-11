'''
    XOR Decryption (Problem 59)

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''

from utils import timeit
from itertools import permutations
import re

################################################################
#
################################################################

# downcased versions of the top 10 most common words
COMMON_WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i']

def compute_score(text):
    '''
     simple scoring function that counts the number of common words in the text

     we will use the top 10 from here:
      http://en.wikipedia.org/wiki/Most_common_words_in_English
    '''

    count = 0
    # split on possible word boundaries, lower case the whole thing
    words = re.findall(r"[\w']+", text.lower())
    for word in words:
        if word in COMMON_WORDS:
            count += 1
    return count

@timeit
def solution1():
    '''
     initial solution to the problem
    '''
    # read the file into an array of integers
    encrypted = [int(x) for x in open('cipher1.txt').read().split(',')]

    # look for the best scoring text
    best_score = -1
    best_text = None

    # for each key
    for key in permutations('abcdefghijklmnopqrstuvwxyz', 3):
        # decrypt the file into an array of characters
        decrypted = [chr(encrypted[i] ^ ord(key[i % 3])) for i in range(len(encrypted))]

        # make the array into a string
        text = ''.join(decrypted)

        # score the string, remember the best one
        score = compute_score(text)
        if score > best_score:
            best_score = score
            best_text = text

    # now compute the sum of the ascii values
    return sum([ord(x) for x in best_text])

if __name__ == "__main__":
    print '\solution #1:', solution1()
