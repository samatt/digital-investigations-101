def read_file(filename):
    with open(filename, "r") as infile:
        return infile.readlines()


def replace_don_quixote(lines, replacement_word):
    new_lines = []
    for line in lines:
        new_line = line.upper().replace("DON QUIXOTE", replacement_word)
        new_lines.append(new_line)
    return new_lines


def write_file(filename, updated_text):
    with open(filename, "w") as outfile:
        outfile.writelines(updated_text)


input_file = "dq.txt"
output_file = "dq_out_two.txt"

lines = read_file(input_file)
new_lines = replace_don_quixote(lines, "DON CORLEONE")
write_file(output_file, new_lines)
