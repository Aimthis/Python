# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
import os
import shutil
clear = lambda: os.system('cls')
clear()

def Vvod_imeni():
    return input("Введите имя: ").capitalize()


def Vvod_familii():
    return input("Введите фамилию: ").capitalize()


def Vvod_otchestva():
    return input("Введите отчество: ").capitalize()


def Vvod_telephona():
    return input("Введите номер телефона: ")


def Vvod_adressa():
    return input("Введите адрес: ").capitalize()

def input_data():
    surname = Vvod_familii()
    name = Vvod_imeni()
    patronymic = Vvod_otchestva()
    phone = Vvod_telephona()
    address = Vvod_adressa()

    with open("phone_book.csv", "a", encoding="utf-8") as file:
        file.write(f"{surname} {name} {patronymic}: {phone} \n {address}\n\n")

def print_data():
    with open("phone_book.csv", "r", encoding="utf-8") as file:
        print(file.read())

def search_line():
    search = input("Введите данные для поиска: ").capitalize()
    with open("phone_book.csv", "r", encoding="utf-8") as file:
        data = file.read().split("\n\n")[:-1]
        for line in data:
            if search in line:
                print(line + '\n')

def user_interface():
    choice = 0
    while choice != 4:
        clear()
        print('''Выберите действие:
                    1 - Запись данных
                    2 - Вывод данных
                    3 - Поиск данных
                    4 - Выход''')
        choice = int(input('номер операции: '))
        match(choice):
            case 1:
                clear()
                input_data()
                choice = input('Данные внесены. Для продолжения нажмите любую кнопку.')
            case 2: 
                clear()
                print_data()
                choice = input('Для продолжения нажмите любую кнопку.')
            case 3: 
                clear()
                search_line()
                choice = input('Для продолжения нажмите любую кнопку.')
            case 4:
                clear()
                print('Досвидания.')
user_interface()