num_of_eggs = int(input('How many eggs do you have ?'))
filled_cartons = int(num_of_eggs / 12)
remaining_cartons = int(num_of_eggs % 12)
print('Number of filled cartons: ')
print(filled_cartons)

print('Number of eggs left over: ')
print(remaining_cartons)
