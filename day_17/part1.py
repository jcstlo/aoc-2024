def parse_file():
    # returns a list of initial register values and the program in list[int] form
    reg_a, reg_b, reg_c, program = 0, 0, 0, []
    with open("day_17/input.txt", "r") as f:
        for line in f:
            if "Register A: " in line:
                reg_a = int(line.replace("Register A: ", "").strip())
            if "Register B: " in line:
                reg_b = int(line.replace("Register B: ", "").strip())
            if "Register C: " in line:
                reg_c = int(line.replace("Register C: ", "").strip())
            if "Program: " in line:
                program_string = line.replace("Program: ", "").strip()
                program = program_string.split(",")
                program = [int(x) for x in program]
        return [reg_a, reg_b, reg_c, program]


def determine_instruction(opcode: int) -> str:
    """
    returns instruction in string format
    """
    if opcode == 0:
        return "adv"
    elif opcode == 1:
        return "bxl"
    elif opcode == 2:
        return "bst"
    elif opcode == 3:
        return "jnz"
    elif opcode == 4:
        return "bxc"
    elif opcode == 5:
        return "out"
    elif opcode == 6:
        return "bdv"
    elif opcode == 7:
        return "cdv"
    else:
        return Exception("Invalid instruction")


def adv(reg_a, combo_operand) -> int:
    """
    returns the result of the operation, to be written to reg_a
    """
    return int(reg_a / (2**combo_operand))


def bxl(reg_b, literal_operand) -> int:
    """
    returns the result of the operation, to be written to reg_b
    """
    return reg_b ^ literal_operand


def bst(combo_operand) -> int:
    """
    returns the result of the operation, to be written to reg_b
    """
    return combo_operand % 8


def jnz(reg_a) -> bool:
    """
    returns True (perform jump) if reg_a == 0
    """
    return reg_a != 0


def bxc(reg_b, reg_c) -> int:
    """
    returns the result of the operation, to be written to reg_b
    """
    return reg_b ^ reg_c


def out(combo_operand) -> int:
    """
    returns the result of the operation, to be written to output
    """
    return combo_operand % 8


def bdv(reg_a, combo_operand) -> int:
    """
    returns the result of the operation, to be written to reg_b
    """
    return int(reg_a / (2**combo_operand))


def cdv(reg_a, combo_operand) -> int:
    """
    returns the result of the operation, to be written to reg_c
    """
    return int(reg_a / (2**combo_operand))


def run_program(reg_a, reg_b, reg_c, program):
    """
    returns the output in list[int] form
    """
    output = []

    def determine_combo_operand(val) -> int:
        if val <= 3:
            return val
        if val == 4:
            return reg_a
        if val == 5:
            return reg_b
        if val == 6:
            return reg_c
        else:
            raise Exception("Invalid combo operand")

    instr_ptr = 0
    while instr_ptr < len(program):
        instruction = determine_instruction(program[instr_ptr])
        literal_operand = program[instr_ptr + 1]
        combo_operand = determine_combo_operand(literal_operand)

        if instruction == "adv":
            reg_a = adv(reg_a, combo_operand)
        elif instruction == "bxl":
            reg_b = bxl(reg_b, literal_operand)
        elif instruction == "bst":
            reg_b = bst(combo_operand)
        elif instruction == "jnz":
            if jnz(reg_a):
                instr_ptr = literal_operand
                continue
        elif instruction == "bxc":
            reg_b = bxc(reg_b, reg_c)
        elif instruction == "out":
            output.append(out(combo_operand))
        elif instruction == "bdv":
            reg_b = bdv(reg_a, combo_operand)
        elif instruction == "cdv":
            reg_c = cdv(reg_a, combo_operand)
        else:
            raise Exception("Invalid instruction")

        instr_ptr += 2

    return output


reg_a, reg_b, reg_c, program = parse_file()
print(f"Register A = {reg_a}")
print(f"Register B = {reg_b}")
print(f"Register C = {reg_c}")
print(f"Program = {program}")

output = run_program(reg_a, reg_b, reg_c, program)

output_formatted = ""
for idx, num in enumerate(output):
    output_formatted += str(num)
    if idx != len(output) - 1:
        output_formatted += ","

print(f"Output: {output_formatted}")
