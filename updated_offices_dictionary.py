office_numbers = {'Frank Pietro': 204, 'Jennifer Moth': 103, 'Tasha Wilson': 245, 'Mark Opengher': 215, 'Ron Choi': 335, 'Amina Hakim': 207, 'Joseph Malakian': 130, 'Maria Hernandez': 167, 'Georgia Thompson': 307}

office_updates = {215: 370, 207: 304, 245: 325, 204: 399} 


for k in office_numbers :
        print(k, office_numbers[k])

# Frank, Tasha, Mark, Amina, will get new offices

office_numbers.update({
'Frank Pietro':370,
'Tasha Wilson':304,
'Mark Opengher':325,
'Amina Hakim':399 })


print(office_numbers.values())

for k in office_numbers :
        print(k, office_numbers[k])

print(office_numbers)