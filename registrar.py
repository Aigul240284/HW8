from data_input import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: 1й или 2й"))

    while var != 1 and var != 2:
        print('Неверно!')
        var = int(input("Введите номер варианта - 1й или 2й: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас данные из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('Вывожу данные для Вас данные из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла 1й или 2й: '))

    while number_file != 1 and number_file != 2:
        print('Неверно! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла,1й или 2й: '))

    if number_file == 1:  
        print("Кого именно Вы хотите изменить?")
        name1=input("Введите имя из спрвочника, данные котрого будут изменены: ")
        surname1=input("Введите фамилию из спрвочника, данные котрого будут изменены: ")
        for i in range(len(data_first)):
            if name1 and surname1 in data_first[i]:
                number_journal = i        
        print(f'Изменить данную запись\n{data_first[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                     data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
        print_data
    else:
        print("Кого именно Вы хотите изменить?")
        name1=input("Введите имя из спрвочника, данные котрого будут изменены: ")
        surname1=input("Введите фамилию из спрвочника, данные котрого будут изменены: ")
        for i in range(len(data_second)):
            if name1 and surname1 in data_second[i]:
                number_journal = i        
        print(f'Изменить данную запись\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address}\n'] + \
                      data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')
        print_data()


def delete_data():
    print('Из какого файла Вы хотите удалить данные, из 1го или 2го?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла 1й или 2й: '))

    while number_file != 1 and number_file != 2:
        print('Неверно!')
        number_file = int(input('Введите номер файла, 1й или 2й: '))

    if number_file == 1:  
        print("Кого именно вы хотите удалить из списка? ")
        name1=input("Введите имя: ")
        surname1=input("Введите фамилию: ")
        for i in range(len(data_first)):
            if name1 and surname1 in data_first[i]:
                number_journal = i
                print(f'Удалить данную запись\n{data_first[number_journal]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
        print_data()
    else:
        print("Кого именно вы хотите удалить из списка? ")
        name2=input("Введите имя: ")
        surname2=input("Введите фамилию: ")
        for i in range(len(data_second)):
            if name2 and surname2 in data_second[i]:
                number_journal = i
                print(f'Удалить данную запись\n{data_second[number_journal]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  
        print_data()
