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

def find_all_combination(dict_token):
    dict_all_combo = {}
    # here we go 
    for key1 , val1 in dict_token.items():
        for key2 , val2 in dict_token.items():
            dict_all_combo[key1 + key2] = concat_two_tokens_from_np_arr(val1 , val2)
    return dict_all_combo

def reverser_dict(dict):
    reversed_dict = {}
    for key , val in dict.items():
        reversed_dict[val] = key
    return reversed_dict

def read_flag_file_and_compare(flag_file_name, dict_all_combos , row_count):
    list_possible_combos = []
    with open(flag_file_name , 'r') as f:
        stripped_line = ""
        token_read = ""
        x = 0
        counter = 0
        for line in f:
            if x == row_count:
                # i will do this after testing the code 
                list_possible_combos.append(get_letter_combos_from_token(token_read , dict_all_combos))
                x = 0
                counter += 1
                # print(token_read , end="")
                token_read = ""
                # print('token break')
                continue

            stripped_line = line.lstrip(" ")
            #print(f'line - {stripped_line}' , end = "")
            token_read += stripped_line
            x += 1
    print(f'tokens read {counter}')
    return list_possible_combos


def get_letter_combos_from_token(token, dict_all_combos):
    # very inefficient process good luck
    combo_list = [] 
    for key , val in dict_all_combos.items():
        if token == val:
            combo_list.append(key)
    return combo_list






def main():

    grid = read_file(file_name)
    np_grid = np.array(grid)
    #print(np_grid[0])
    dict = parse_grid(np_grid, columns, len_separator, ascii_start, ascii_end)
    # dict_string = {}
    # for key , value in dict.items():
    # #     dict_string[key] = convert_2d_array_str(value)
    # print(concat_two_tokens(dict_string['L'] , dict_string['3'] , 3 , 5))
    # print(dict['L'])
    # print(dict['3'])
    # print(concat_two_tokens_from_np_arr(dict['L'] , dict['3']))
    dict_all_combos = find_all_combination(dict)
    # dict_all_combo_reverse = reverser_dict(dict_all_combo)
    # print(dict_all_combo_reverse[dict_all_combo['L3']])
    
    # print(dict_all_combo['L3'])
    # print(dict_all_combo['LE'])
    # comb_set = set()
    # for key , val in dict_all_combo.items():
    #     comb_set.add(val)
    

    # print(f'len of dict_all_combo {len(dict_all_combo)}')
    # print(f'len of the set of all combos {len(comb_set)}')

    list_possible_combos = read_flag_file_and_compare('flag_copy.txt', dict_all_combos , rows)
    print(len(list_possible_combos))
    k=1
    for x in list_possible_combos:
        k=k*len(x)
        print(x)
    print(k)
if __name__ == "__main__":
    main()
