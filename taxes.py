income = int(input('What is your yearly income?: '))

if income < 9700:
    print('Tax Due: ')
    print(income * 0.1)

elif income < 39475 :
    print('Tax Due: ')
    print((income - 970)* 0.12)

…    print((income - 32748.50)*.32)

elif income < 510300:
    print('Tax Due: ')
    print((income - 46628.50)*.35)

else:
    print('Tax Due: ')
    print((income - 153798.50)*.37)
    