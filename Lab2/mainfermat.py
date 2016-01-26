#!/usr/bin/python3

from classes.fermat import Fermat

def main():
    fermat = Fermat()

    a = fermat.getInput('a')
    b = fermat.getInput('b')
    c = fermat.getInput('c')
    n = fermat.getInput('n')

    print(fermat.check_fermat(a, b, c, n))


if __name__ == "__main__":
    main()