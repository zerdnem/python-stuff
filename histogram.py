# BIRD = """
# def histogram(sequence):
    # return sorted([(element,sequence.count(element)) for element in set(sequence)],key=lambda e:e[1],reverse=True)

# print(histogram(['y','o','u','g','u','n','n','a','g','e','t','s','t','a','b','b','e','d','m','a','t','e']))
# """

# exec(BIRD)

list = [ 1, 2, 3, 4, 5, 6, 1, 1, 2, 3, 3, 3 ]

dict = {}
for item in list:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

print(dict)
