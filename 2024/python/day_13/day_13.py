import numpy as np
from numpy import linalg
from sympy import symbols, Eq, solve, Integers
a, b = symbols('a b', integer=True)

USE_REAL_INPUT = True

def CosmoKramer(A, B, P):
    
    a11, a12, b1 = A[0], B[0], P[0]
    a21, a22, b2 = A[1], B[1], P[1]

    det = a11 * a22 - a12 * a21
    if det == 0:
        # no solution
        return (0, 0)

    # Cramer's rule (and they said Linear Algebra was not worth taking...)
    # actually, nobody said that. LA is amazing.
    a = (b1 * a22 - b2 * a12) / det
    b = (a11 * b2 - a21 * b1) / det

    # only want integer solutions, is_integer() to the resuce...
    if a.is_integer() and b.is_integer():
        return (int(a), int(b))

    # no solution
    return (0, 0)


def run():
    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        machines = []
        entry = []
        i = 0
        while (line := f.readline()):
            if line == "\n":
                machines.append(entry)
                entry = []
                continue
            splitter = "=" if i == 2 else "+"
            x, y = line.split(": ")[1].split(", ")
            entry.append((int(x.split(splitter)[1]), int(y.split(splitter)[1])))
            i = (i + 1) % 3
        machines.append(entry)
        
        part1 = 0
        part2 = 0
        for A, B, P in machines:
            na, nb = CosmoKramer(A, B, P)
            part1 += 3 * na + nb

            na2, nb2 = CosmoKramer(A, B, (P[0] + 10000000000000, P[1] + 10000000000000))
            part2 += 3 * na2 + nb2
        
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
