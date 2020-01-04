
total = 0
count = 0
while True :
    s_input = input('Enter a number: ')
    if s_input == 'done' :
        break
    try:
        i_input = int(s_input)

    except:
        print('Invalid input')
        continue

    total = total + i_input
    count = count + 1

print(total, count, total/count)
