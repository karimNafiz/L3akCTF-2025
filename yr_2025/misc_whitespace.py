# plan
# read the file
# u know the number of rows
# you know the column
# we need to account for a space so column is no_column + no_of space 
# range of ascii characters 33 to 126 includsive

import numpy as np

rows = 5
columns = 3
len_seperator = 1
file_name = 'input.txt' # relative path 

ascii_range_start = 33
ascii_range_end = 126



def read_file(file_path): # should return a 2d grid
    # this grid will hold all the characters read from the file
    # grid will be of dimension (row_number , (rows + len_seperator)* no_of_characters)
    grid = []
    with open(file_path , 'r') as f:
        for line in f:
            grid.append(line)
    return grid 

def parse_grid(grid ,column_count, len_seperator, ascii_start, ascii_end ):
    dict = {}
    for i in range(ascii_start , ascii_end + 1 , 1):
        # need to normalize
        z = i - ascii_start
        dict[chr(i)] = grid[:][z * (column_count + len_seperator) : (column_count + len_seperator)]
    return dict 


def main():
    grid = read_file(file_name)
    # create a numpy array from python ass manual list
    np_grid = np.array(grid)
    dict = parse_grid(np_grid, columns , len_seperator , ascii_range_start , ascii_range_end)
    print(dict['c'])


if __name__ == "__main__":
    main()