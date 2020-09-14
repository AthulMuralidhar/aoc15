instructions = open('inp.txt').read().splitlines()

result = {}

for i in instructions:

    # import ipdb; ipdb.set_trace()

    # ['turn', 'on', '887,9', 'through', '959,629']
    # print(i)
    temp_i = i
    try:
        # turn on turn off case
        row_col_instruction = [temp_i.split()[2], temp_i.split()[4]]
    except IndexError:
        # toggle case
        row_col_instruction = [temp_i.split()[1], temp_i.split()[3]]
    # ['887,9', '959,629']
    row_col_instruction = [i.split(",") for i in row_col_instruction]
    # [['887', '9'], ['959', '629']]


    # print(row_col_instruction)

    row_iterator = int(row_col_instruction[0][0])
    col_iterator = int(row_col_instruction[0][1])

    while row_iterator <= int(row_col_instruction[1][0]):
        while col_iterator <= int(row_col_instruction[1][1]):
            
            # import ipdb; ipdb.set_trace()
            
            if 'turn on' in temp_i:
                result[row_iterator, col_iterator] = 1
            if 'turn off' in temp_i:
                result[row_iterator, col_iterator] = 0
            if 'toggle' in temp_i:
                try:
                    # in case of second time visit
                    result[row_iterator, col_iterator] = 1 - result[row_iterator, col_iterator]
                except KeyError:
                    # in case of first time visit
                    result[row_iterator, col_iterator] = 1

            col_iterator += 1
        row_iterator += 1

# print(result)
final_answer = 0
for i in result.keys():
    if result[i] == 1:
        final_answer +=1


print(final_answer)

# That's not the right answer; your answer is too low. If you're stuck, make sure you're using the full input data
# there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 50952.)[Return to Day 6]
