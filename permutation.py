# import sys

# items = sys.argv[1:]

# if not items:
  # sys.exit('The OP is a faggot')
# elif len(items) == 1:
  # sys.exit(items)

# def recurse(items, permutations, picks = None):
  # if not picks:
    # picks = []

  # if len(items) > 2:
    # for i in range(len(items)):
      # recurse(items[:i] + items[i + 1:], permutations, picks + [items[i]])
  # else:
    # permutations.append(picks + items)
    # permutations.append(picks + items[::-1])

# permutations = []
# recurse(items, permutations)

# for permutation in permutations:
  # print permutation
#--------------------------------------------------
string = 'the quick brown fox jumps over the lazy dog'
import itertools

def permutations(array):
    if len(array) == 1:
        return [array]

    perms = []
    for i in range(len(array)):
        for p in permutations(array[:i] + array[i+1:]):
            perms.append([array[i]] + p)

    return perms

for p in permutations(string.split()):
    print(p)
#--------------------------------------------------
# def permutations(seq):
    # def _permuterec(subseq, i):
        # if (i >= len(subseq) - 1):
            # yield list(subseq)
        # else:
            # yield from _permuterec(subseq, i + 1)
            # for j in range(i + 1, len(subseq)):
                # a, b = subseq[i], subseq[j]
                # subseq[i], subseq[j] = b, a
                # yield from _permuterec(subseq, i + 1)
                # subseq[i], subseq[j] = a, b
    # subseq = list(seq)
    # yield from _permuterec(subseq, 0)
# s = ['j', 'a', 'y', 'j', 'a', 'n']
# permutations(s)
