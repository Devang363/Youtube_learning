
def get_longest_line(filename):
    large_line = ''
    large_line_len = 0

    with open(filename, 'r') as f:
        for line in f:
            if len(line) > large_line_len:
                large_line_len = len(line)
                large_line = line

    return large_line

filename = input('Enter text file Name: ')
print (get_longest_line(filename+".txt"))