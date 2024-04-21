import pandas
print('trying to see if this will work or not')

menus=[
    ['Alu Bhaji', 'Porota','Shemai'],
    ['Kachchi', 'Tehari'],
    ['Mach Bhat','Shak Bhaji','Korolla Bhaji']

]

for items in menus:
    for item in items:
        print(item)


#Dictionary example

menus={
    'breakfast':     ['Alu Bhaji', 'Porota','Shemai'],
    'lunch':['Kachchi', 'Tehari'],
    'dinner':['Mach Bhat','Shak Bhaji','Korolla Bhaji']

}

print(menus['lunch'])

for name, menu in menus.items():
    print(name, ":", menu)
