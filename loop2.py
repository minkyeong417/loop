largest = None
smallest = None
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try :
        fval = float(sval)

    except :
        print('Invalid input')
        continue

    if largest is None:
        largest = fval
        smallest = fval
    elif largest < fval:
        largest = fval
    elif smallest > fval:
        smallest = fval

print('Maximum is',largest)
print('Minimum is',smallest)
