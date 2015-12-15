##################################################
#
# write code to check if a string is palindrome or
# not
#
##################################################
import sys

def check_if_palindrom(s):
    if (len(s)%2) != 0:
        return False
    for k in range(len(s)):
        if s[k] != s[len(s)-k-1]:
            return False
    return True


def main():
    
    if check_if_palindrom(sys.argv[1]):
        print('String {0} is palindrome'.format(sys.argv[1]))
    else:
        print('String {0} is not a palindrome'.format(sys.argv[1]))    

if __name__ == '__main__':
    main()