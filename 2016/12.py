import sys, os

FILE_NAME = "2016/12.txt"
FILE_LENGTH = 23

MOVE_UP = "\033[F"
COL_RESET = "\033[0;0m"
COL_GREEN = "\033[0;32m"

instructions = []

f = open(FILE_NAME)
for line_number in range(FILE_LENGTH):
    instruction = f.readline().strip().split(" ")
    for i in range(len(instruction)):
        try:
            instruction[i] = int(instruction[i])
        except:
            pass
    instructions.append(instruction)

def print_instructions(index, cpu, last = False):
    to_print = ""
    for i in range(len(instructions)):
        if i == index:
            to_print += f"{COL_GREEN}> {" ".join(list(map(str, instructions[i])))}{COL_RESET}\n"
        else:
            to_print += f"  {" ".join(list(map(str, instructions[i])))}\n"
    to_print += f"\n"
    for i in cpu:
        to_print += f"  [{i}]: {cpu[i]}{10 * " "}\n"
    if not last:
        to_print += f"{MOVE_UP * (len(instructions) + 5)}"
    sys.stdout.write(to_print)

cpu = {"a" : 0, "b" : 0, "c" : 1, "d" : 0}
index = 0
os.system("cls")
while index < len(instructions):
    current_instruction = instructions[index]
    print_instructions(index, cpu)
    if current_instruction[0] == "cpy":
        if type(current_instruction[1]) is int:
            cpu[current_instruction[2]] = current_instruction[1]
        else:
            cpu[current_instruction[2]] = cpu[current_instruction[1]]
    elif current_instruction[0] == "inc":
        cpu[current_instruction[1]] += 1
    elif current_instruction[0] == "dec":
        cpu[current_instruction[1]] -= 1
    elif current_instruction[0] == "jnz":
        if current_instruction[1] == 1 or cpu[current_instruction[1]] != 0:
            index += current_instruction[2] - 1
    index += 1
print_instructions(index, cpu, True)