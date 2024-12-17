USE_REAL_INPUT = True

IP = 0

A = "A"
B = "B"
C = "C"

register = {
    A: 0,
    B: 0,
    C: 0,
}

combo = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 0,
    5: 0,
    6: 0
}

output = []

class Instructions:
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7


def execute(opcode, operand):
    global IP, register, output

    match opcode:
        case Instructions.adv:
            numerator = register[A]
            denominator = pow(2, combo[operand])
            register[A] = numerator // denominator
            combo[4] = register[A]
            IP += 2
        case Instructions.bxl:
            a = register[B]
            b = operand
            register[B] = a ^ b
            combo[5] = register[B]
            IP += 2
        case Instructions.bst:
            register[B] = combo[operand] % 8
            combo[5] = register[B]
            IP += 2
        case Instructions.jnz:
            if register[A] != 0:
                IP = operand
            else:
                IP += 2
        case Instructions.bxc:
            register[B] = register[B] ^ register[C]
            combo[5] = register[B]
            IP += 2
        case Instructions.out:
            output.append(combo[operand] % 8)
            IP += 2
        case Instructions.bdv:
            numerator = register[A]
            denominator = pow(2, combo[operand])
            register[B] = numerator // denominator
            combo[5] = register[B]
            IP += 2
        case Instructions.cdv:
            numerator = register[A]
            denominator = pow(2, combo[operand])
            register[C] = numerator // denominator
            combo[6] = register[B]
            IP += 2
        case _:
            print(f"Invalid opcode: {opcode}")
            exit(271828)

def run():
    global IP, register, combo

    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        registers, program = f.read().split("\n\n")
        registers = [int(register.split(": ")[1]) for register in registers.split("\n")]
        program = [int(opcode) for opcode in program.split(": ")[1].split(",")]

    register[A] = registers[0]
    register[B] = registers[1]
    register[C] = registers[2]
    combo[4] = register[A]
    combo[5] = register[B]
    combo[6] = register[C]
    
    while IP + 1 < len(program):
        opcode = program[IP]
        operand = program[IP + 1]
        execute(opcode, operand)
    
    res = ",".join(map(str, output))
    print(f"Output: {res}")


if __name__ == "__main__":
    run()
