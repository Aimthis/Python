# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
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
def Vvod_dannyh ():
    name = Vvod_imeni
    patronymic = Vvod_otchestva
    surname = Vvod_familii
    phone = Vvod_telephona
    address = Vvod_adressa

    with open('phone_book.csv', 'a', encoding='utf-8') as file:
        print(file)
        file.write(f'{name} {patronymic} {surname}: {phone} \n {address}\n\n')

def search ():
    with open