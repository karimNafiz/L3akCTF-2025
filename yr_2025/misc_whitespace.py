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

def convert_2d_array_str(np_arr):
    lines = [''.join(row) for row in np_arr]
    return '\n'.join(lines)
# stupid approach
def concat_two_tokens(token1 , token2, column_count , row_count):
    x = 0
    column_count += 1 # need to account for the backslash n
    current_row = 0
    crr_token_ptr = 0
    final_str = ""
    tokens = [list(token1) , list(token2)]
    len_token = len(tokens)
    # this while loop is why I hate python 
    while True:
        print(f'final string {final_str}')
        # worst piece of code I have written in a while 
        try:
            z = tokens[crr_token_ptr][column_count * current_row + x]
            print(tokens[crr_token_ptr])
            print(z)
        except:
            break


        if tokens[crr_token_ptr][column_count * current_row + x] == "":
            x += 1
            continue
        # check if we have reached the end for the current row
        if tokens[crr_token_ptr][column_count * current_row + x] == "\n":
            # if we are at the end of the row for the last token we need to add a new line in our new string
            if(crr_token_ptr == len_token - 1):
                final_str += '\n'
                current_row += 1
            
            crr_token_ptr += 1
            crr_token_ptr = crr_token_ptr %  (len_token)
            x = 0 
            continue
        final_str += tokens[crr_token_ptr][column_count * current_row + x]
        x += 1
    return final_str
        
def concat_two_tokens_from_np_arr(np_arr1 , np_arr2):
    final_str = ''
    for row1 , row2 in zip(np_arr1 , np_arr2):
        for x in row1:
            if x == ' ':
                continue
            final_str += x
        for y in row2:
            if y == ' ':
                continue
            final_str += y
        final_str += '\n'
    return final_str



def main():

    grid = read_file(file_name)
    np_grid = np.array(grid)
    #print(np_grid[0])
    dict = parse_grid(np_grid, columns, len_separator, ascii_start, ascii_end)
    # dict_string = {}
    # for key , value in dict.items():
    # #     dict_string[key] = convert_2d_array_str(value)
    # print(concat_two_tokens(dict_string['L'] , dict_string['3'] , 3 , 5))
    print(dict['L'])
    print(dict['3'])
    print(concat_two_tokens_from_np_arr(dict['L'] , dict['3']))

if __name__ == "__main__":
    main()
