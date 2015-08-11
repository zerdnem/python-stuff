#!/usr/bin/python
import re
import sys

expressions = {
    'Visa': '^4[0-9]{12}(?:[0-9]{3})?$',
    'MasterCard': '^5[1-5][0-9]{14}$',
    'American Express': '^3[47][0-9]{13}$',
    'Diners Club': '^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
    'Discover': '^6(?:011|5[0-9]{2})[0-9]{12}$',
    'JCB': '^(?:2131|1800|35\d{3})\d{11}$'
}

def Validate(card):
    for key, value in expressions.iteritems():
        if re.match(value, card):
            return key
    return 'Unknown/Invalid Type'

def main():
    print Validate(sys.argv[1])

if __name__ == '__main__':
    main()

