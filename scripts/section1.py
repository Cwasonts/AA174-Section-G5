#!/usr/bin/env python3

# add import and helper functions here

import numpy as np


def main():

    print("Hello World!")
    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))

    C = A@B
    print (C)

if __name__ == "__main__":
    # code goes here

    main()
