def fold(lst, f, base):
	i = 0
	while i < len(lst):
		base = f(base, lst[i])
		i += 1

	return base
a = [1, 2, 3, 4, 5, 6]
print(fold(a, lambda x, y: x + float(y), 0) / len(a))
#or
#reduce(lambda x, y: x + float(y), [1, 2, 3, 4, 5, 6]) / 6
