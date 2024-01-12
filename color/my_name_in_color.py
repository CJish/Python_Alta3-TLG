#!/usr/bin/env python3
""" Author CJish"""

import crayons


def main():
    # print 'red string' in red
    print(crayons.red('CJ'))

    # Red White and Blue text
    print(f"{crayons.red(' ')} C {crayons.blue('J')} ")  # f-string (newest version of str templating)

    crayons.disable() # disables the crayons package

# this condition is only true if our script is run directly
# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()

