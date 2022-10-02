list = []

def a():
    with open('Опитування.csv', 'r') as file:
        for i in file:
            if 'Гугл' or 'Google' in i:
                list.append(i)
        print(list)

a()