weekly_planner = { 'Monday': 'hair appointment' , 
'Tuesday': 'pick up groceries', 
'Wednesday': 'baseball practice', 
'Thursday': 'wash car', 
'Saturday': 'dinner', 
'Friday': 'dog grooming appointment'}

print(weekly_planner['Monday'])
print(weekly_planner['Friday'])

if weekly_planner['Monday'] != '':
    print('You need to clear your schedule')
else:
    print('You are good to go')

if weekly_planner['Friday'] != '':
    print('You need to clear your schedule')
else:
    print('You are good to go')

del weekly_planner['Monday']
del weekly_planner['Friday']

weekly_planner.update({'Tuesday': 'pick up groceries, hair appointment','Sunday':'dog grooming appointment'})


print(weekly_planner)
