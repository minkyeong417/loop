s_input = None
total = 0
count = 0
while s_input != 'done' :
    s_input = input('Enter a number: ')
    if s_input == 'done' :
        break
    try:
        i_input = int(s_input)
        total = total + i_input
        count = count + 1
    except:
        print('Invalid input')
print(total, count, total/count)
