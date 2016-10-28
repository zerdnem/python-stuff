import sys

def count_names():
    names = {}
    for name in sys.stdin.readlines():
        name = name.strip()

        if name in names:
            names[name] += 1
        else:
            names[name] = 1
            
    for name, count in names.items():
        sys.stdout.write("{0}\t{1}\n".format(name, count))

if __name__ == "__main__":
    count_names()
