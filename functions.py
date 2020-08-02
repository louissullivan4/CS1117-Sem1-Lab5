# ScriptName: functions.py
# Author: Louis Sullivan 119363083

# defining the while loop with a max_number of 10
def while_loop(max_number=10, even = False):
    # making a list
    max_list = []
    # accumlator
    accum = 0
    # starting at 1
    i = 1
    # if max number is greater than 0
    if max_number > 0:
        # while i is less than or equal to max number
        while i <= max_number:
            # if the number is less than -12 break
            if max_number > 12:
                break
            while even == True:
                if i % 2 == 0:
                 continue
            # add the number to the list
            max_list.append(i)
            # increase i by one
            i += 1
            accum += i
    else:
        # while i is greater than or equal to max number
        while i >= max_number:
            # if the number is less than -12 break
            if max_number < 12:
                break
            # add the number to the list
            max_list.append(i)
            # decrease i by one
            i -= 1

    print(max_list, accum)

