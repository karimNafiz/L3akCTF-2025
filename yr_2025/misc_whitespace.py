import numpy as np

rows = 5
columns = 3
len_separator = 1
file_name = 'input (1).txt'

ascii_start = 33
ascii_end   = 126

def read_file(file_path):

    grid = []
    with open(file_path, 'r') as f:
        for line in f:
            # strip newline, then turn into list of chars
            grid.append(list(line.rstrip('\n')))
    return grid

def parse_grid(grid, column_count, len_separator, ascii_start, ascii_end):

    char_dict = {}
    width = column_count + len_separator
    

    for code in range(ascii_start, ascii_end + 1):
        z = code - ascii_start
        start = z * width
        end   = start + column_count

        # print(chr(code))
        # # # print(f'start {start}')
        # # # print(f'end {end}')
        # print(grid[: , start : end])
        char_dict[chr(code)] = grid[: , start : end ]
        
        


    return char_dict

def main():

    grid = read_file(file_name)
    np_grid = np.array(grid)
    #print(np_grid[0])
    dict = parse_grid(np_grid, columns, len_separator, ascii_start, ascii_end)

    print(dict['b'])

if __name__ == "__main__":
    main()
