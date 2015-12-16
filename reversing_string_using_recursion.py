##################################################
#
# reversing String using recursion.py
#
##################################################
import sys

def reverse_string_recursively(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse_string_recursively(s[0:-1])


def main():
    print('Original list: {0}'.format(sys.argv[1]))
    print('Reversed list: {0}'.format(reverse_string_recursively(sys.argv[1])))

if __name__ == '__main__':
    main()