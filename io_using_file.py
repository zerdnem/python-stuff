with open('backup.py') as f:
    with open('backup.txt', 'w') as f1:
        for line in f:
            f1.write(line)

with open('backup.txt') as f:
    for line in f:
        print line
