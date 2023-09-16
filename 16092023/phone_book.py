# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
import os
import shutil
def Vvod_imeni ():
    return input('Введите имя: ').capitalize
def Vvod_familii ():
    return input('Введите фамилию: ').capitalize
def Vvod_otchestva ():
    return input('Введите отчество: ').capitalize
def Vvod_telephona ():
    return input('Введите номер телефона: ').capitalize
def Vvod_adressa ():
    return input('Введите номер адрес: ').capitalize
def input_data ():
    name = Vvod_imeni
    patronymic = Vvod_otchestva
    surname = Vvod_familii
    phone = Vvod_telephona
    address = Vvod_adressa

    with open('phone_book.csv', 'a', encoding='utf-8') as file:
        print(file)
        file.write(f'{name} {patronymic} {surname}: {phone} \n {address}\n\n')

def print_data():
    with open('phone_book.csv', 'r', encoding='utf-8') as file:
        print(file.read())

def search_line ():
    search = input('Введите данные для поиска: ').capitalize
    with open('phone_book.csv', 'r', encoding='utf-8') as file:
        data = file.read().split('\n\n')[:-1]
        print(data)
        for line in data:
            if search in line:
                print(line)

input_data()