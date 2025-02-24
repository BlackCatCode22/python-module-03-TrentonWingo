num = 0.0
count = 0

while True:

    givenum = input('Give me a number ')

    try:
        if givenum == 'done':
            print(num, count, ave)
            break

        givenum = float(givenum)

        count = count + 1
        num = float(num + givenum)

        ave = num / count
        print(num, count, ave)

        continue


    except:
        print('invalid input')
        continue