inputs = []
new_input = input()
while new_input != r"\end":
    inputs.append(new_input)
    new_input = input()
maxlen = 0
for line in inputs:
    line = line.rstrip(' ')
    if len(line) > maxlen:
        maxlen = len(line) 
outputs = [''] * maxlen
index_out = 0
for line in inputs:
    print(line)
    index_in = 0
    for c in line:
        outputs[index_in] += c
        index_in += 1
    while (index_in < maxlen):
        outputs[index_in] += ' '
        index_in += 1
    index_out += 1
for line in outputs:
    print(line)
