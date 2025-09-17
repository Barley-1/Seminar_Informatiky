#!/usr/bin/env python3
# David Zacek
filename = 'tabulka.csv'

def view():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    print(content)

def edit():
    name = input('Zadej jmeno:')
    surname = input('Zadej prijmeni:')
    yob = input('Zadej datum narozeni:')
    line = f'\n{name},{surname},{yob}'
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(line)

if __name__ == '__main__':
    print('Co bys chtel delat?')
    print('1 pro otevreni tabulky')
    print('2 pro pridani do tabulky')
    action = input('>>')
    print(action)
    if action == '1':
        view()
    elif action == '2':
        edit()
    else:
        print('\n Spatne, cau')
        exit()