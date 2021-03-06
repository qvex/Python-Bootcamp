birthdays = {'Alice' : 'Apr 1', 'Bob' : 'June 21', 'Carol' : 'Mar 4'}

while True:
    print('Enter a name: (Blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('Name not present in the database.')
        print('When is their birthday?')
        bday = input()
        print('Would you like to add this birth date to the database? Type "y" for yes and "n" for no')
        decision = input()
        if decision == 'y':
            birthdays[name] = bday
            print('Database updated successfully!')
        else:
            print('Have a good day.')
            break

