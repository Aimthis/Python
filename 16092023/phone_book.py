# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
import os, shutil, subprocess

clear = lambda: os.system("cls")
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
    string_of_data = f"{surname} {name} {patronymic}: {phone} \n {address}\n\n"
    return string_of_data

def adding_to_pb():
    with open("phone_book.csv", "a", encoding="utf-8") as file:
        file.write(input_data())


def print_data():
    with open("phone_book.csv", "r", encoding="utf-8") as file:
        print(file.read())


def edit_data():
    clear()
    print("Введите в поиск заменяемые данные")
    old_data = search_line()
    choice = 0
    while choice != 1:
        print(old_data)
        print('Для продолжения нажмите 1, для отмены 5')
        choice = int(input('Хотите изменить эти данные?'))
        if choice == 5: return
    if choice == 5: return
    print("Введите новые данные")
    new_data = input_data()
    print(new_data)
    choice = input('')
    with open("phone_book.csv", "r", encoding="utf-8") as file:
        old_total_data = file.read().split("\n\n")[:-1]
        for line in old_total_data:
            if line == old_data:
                new_total_data =+ new_data
            else:
                new_total_data =+ line

    with open ('test.txt', 'w') as file:
        file.write(new_total_data)


def search_line():
    choice = 0
    search = input("Введите данные для поиска: ").capitalize()
    result = 'Нет подходящих записей'
    with open("phone_book.csv", "r", encoding="utf-8") as file:
        data = file.read().split("\n\n")[:-1]
        for line in data:
            if search in line:
                print(f'Найдена следующая запись:\n {line}')
                while choice != 1:
                    result = line
                    choice = int(input('Вы искали эти данные? Нажмите "1" чтобы продолжить поиск или "5" чтобы закончить: '))
                    if choice == 5:
                        return result
                    if choice == 1:
                        result = 'Нет подходящих записей'
    clear()
    return result


def user_interface():
    choice = 0
    while choice != 5:
        clear()
        print(
            """Выберите действие:
                    1 - Запись данных
                    2 - Вывод данных
                    3 - Поиск данных
                    4 - Изменение данных
                    5 - Выход"""
        )
        choice = int(input("номер операции: "))
        match (choice):
            case 1:
                clear()
                adding_to_pb()
                choice = input("Данные внесены. Для продолжения нажмите ввод.")
            case 2:
                clear()
                print_data()
                choice = input("Для продолжения нажмите ввод.")
            case 3:
                clear()
                print(search_line() + "\n")
                choice = input("Для продолжения нажмите ввод.")
            case 4:
                clear()
                edit_data()
            case 5:
                clear()
                print("Досвидания.")


user_interface()
