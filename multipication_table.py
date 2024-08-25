original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for originals in original_numbers:
    for copies in copy_numbers:
        print(originals , str('times') , copies, str('is') , (originals*copies) )
