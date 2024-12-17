USE_REAL_INPUT = True


class Instructions:
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7


def run_program(program, a, b=0, c=0):
    output = []
    register = {"A": a, "B": b, "C": c}
    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: register["A"],
        5: register["B"],
        6: register["C"],
    }

    IP = 0
    while IP + 1 < len(program):
        opcode = program[IP]
        operand = program[IP + 1]
        match opcode:
            case Instructions.adv:
                numerator = register["A"]
                denominator = pow(2, combo[operand])
                register["A"] = numerator // denominator
                combo[4] = register["A"]
                IP += 2
            case Instructions.bxl:
                a = register["B"]
                b = operand
                register["B"] = a ^ b
                combo[5] = register["B"]
                IP += 2
            case Instructions.bst:
                register["B"] = combo[operand] % 8
                combo[5] = register["B"]
                IP += 2
            case Instructions.jnz:
                if register["A"] != 0:
                    IP = operand
                else:
                    IP += 2
            case Instructions.bxc:
                register["B"] ^= register["C"]
                combo[5] = register["B"]
                IP += 2
            case Instructions.out:
                output.append(combo[operand] % 8)
                IP += 2
            case Instructions.bdv:
                numerator = register["A"]
                denominator = pow(2, combo[operand])
                register["B"] = numerator // denominator
                combo[5] = register["B"]
                IP += 2
            case Instructions.cdv:
                numerator = register["A"]
                denominator = pow(2, combo[operand])
                register["C"] = numerator // denominator
                combo[6] = register["B"]
                IP += 2
            case _:
                print(f"Invalid opcode: {opcode}")
                exit(271828)

    return output


def run():
    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        registers, program = f.read().split("\n\n")
        registers = [int(register.split(": ")[1]) for register in registers.split("\n")]
        program = [int(opcode) for opcode in program.split(": ")[1].split(",")]

    out = run_program(program, registers[0], registers[1], registers[2])
    part1 = ",".join(map(str, out))
    print(f"Part 1: {part1}")

    """
    Decompiled program:

        B = A % 8
        B = B ^ 2
        C = A // 2^B
        B = B ^ C
        A = A // (2 ** 3)
        B = B ^ 7
        return B % 8

        We notice that A is >> by 3 every iteration of the program.
    
    Strategy:

        Note that we always start with 'B = A % 8'.
        If we're working in base 8, then B is set to the last 3 bits of A.
        This is similar to doing e.g. N mod 1000 in base 10 to retrieve the last 3 digits.

        With that said, we notice that only the last 3 bits of A have an influence on what is returned each iteration. We can use this property to solve our problem.

        Say we have some program = ..., 5,5,3,0.
        We can start with finding a 3 bit number that generates the last 0.
        When found, that 3 bit number becomes part of our solution.
        We shift those bits << by 3, and repeat the process, but now looking for
        a 3 bit number that generates the next digit (3 in this case). Do that until
        we've found a 3 bit number for each of the digits in the program.

        In the end, we'll have a big number whose 3 LSBs will generate the first digit
        of our program, the next 3 bits will generate the second digit, and so on.

        Thus, we will have found a number that generates the program itself.
    """

    possible_as = [0]
    for i in range(len(program)):
        discovered = []
        for potential_a in possible_as:
            for tbn in range(8):
                A = (potential_a << 3) | tbn
                res = run_program(program, A)
                if res == program[-i - 1 :]:
                    discovered.append(A)
        possible_as = discovered

    part2 = min(possible_as)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
