from __future__ import print_function


def main(n):
    '''Prints all integers from 1 to n (inclusive) without any separators'''
    for i in range(int(n)):
        print(str(i+1), end='')


if __name__ == '__main__':
    main(input())

# https://www.hackerrank.com/challenges/python-print/problem
