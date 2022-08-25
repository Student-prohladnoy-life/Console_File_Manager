import os
import os.path
import shutil
import datetime
import random
import sys
import pickle


def info_platform():

    print('Данные системы', sys.platform, '(', os.name, ')')


def info_developer():
    print("Student-prohladnoy-life")


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('файл с таким именем уже есть')


def get_list(foldres_only=False):
    TEXT_FILE = 'Listdir.txt'
    listdir = []

    if os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, 'r') as f:
            for order in f:
                listdir.append(order.replace('\n', ''))

    # if os.path.exists(TEXT_FILE):
    #     with open(TEXT_FILE, 'rb') as f:
    #         listdir = pickle.load(f)

    while True:

        print('1. Каталог')
        print('2. Папки')
        print('3. Файлы')
        print('4. Выход')

        path = 'D:/Python_project/Console_File_Manager'
        choice = input('Выберети пунк меню: ')
        if choice == '1':

            for dirs, folder, files in os.walk(path):
                print('Выбранный каталог: ', dirs)
                listdir.append(f'Каталог: {dirs}')
                break

        elif choice == '2':
            for dirs, folder, files in os.walk(path):
                print(f'Папки: {folder}')
                listdir.append(f'Папки: {folder}')
                break

        elif choice == '3':
            for dirs, folder, files in os.walk(path):
                print(f'Файлы: {files}')
                listdir.append(f'Файлы: {files}')
                break

        elif choice == '4':
            with open(TEXT_FILE, 'w') as f:
                for listdir in listdir:
                    f.write(f'{listdir}\n')
            break
        #
        #     with open(TEXT_FILE, 'wb') as f:
        #         pickle.dump(listdir, f)
        #     break

        else:
            print(F"{'>-<' * 5}Неверный пункт меню{'>-<' * 5}")

    f.close()

        # directory = os.walk(path)
        # print(next(directory))


    # result = os.listdir()
    # if foldres_only:
    #     result = [f for f in result if os.path.isdir(f)]
    # print(result)
    # print("Текущая деректория:", os.getcwd())

def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка с этим именем уже есть ')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def victory():

    months = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря',
    }

    days = {
        '01': 'первое',
        '02': 'второе',
        '03': 'третье',
        '04': 'четвертое',
        '05': 'пятое',
        '06': 'шестое',
        '07': 'седьмое',
        '08': 'восьмое',
        '09': 'девятое',
        '10': 'десятое',
        '11': 'одиннадцатое',
        '12': 'двенадцатое',
        '13': 'тринадцатое',
        '14': 'четырнадцатое',
        '15': 'пятнадцатое',
        '16': 'шестнадцатое',
        '17': 'семнадцатое',
        '18': 'восемнадцатое',
        '19': 'девятнадцатое',
        '20': 'дватцатое',
        '21': 'дватцать первое',
        '22': 'дватцать второе',
        '23': 'дватцать третье',
        '24': 'дватцать четвертое',
        '25': 'дватцать пятое',
        '26': 'дватцать шестое',
        '27': 'дватцать седьмое',
        '28': 'дватцать восьмое',
        '29': 'дватцать девятое',
        '30': 'тридцатое',
        '31': 'тридцать первое',
    }

    question_virtory = [
        ['Дата рождения, Достоевского Федора Михайловича: ', '11.11.1821'],
        ['Дата рождения, Булгакова Михаила Афанасьевича: ', '15.05.1891'],
        ['Дата рождения, Лермонтова Михаила Юрьевича: ', '15.10.1814'],
        ['Дата рождения, Некрасова Николая Алексеевича: ', '10.12.1821'],
        ['Дата рождения, Пушкина Александра Сергеевича: ', '06.06.1799'],
        ['Дата рождения, Толстого Льва Николаевича: ', '09.09.1828'],
        ['Дата рождения, Фета Афанасия Афанасьевича: ', '05.12.1820'],
        ['Дата рождения, Цветаевой Марины Ивановны: ', '08.10.1892'],
        ['Дата рождения, Чехова Антона Павловича: ', '29.01.1860'],
        ['Дата рождения, Шолохова Михаила Александровича: ', '24.05.1905']
    ]

    score = 0

    sample = random.sample(question_virtory, 5)

    print(F'{"<" * 9} Добро пожаловать на викторину {">" * 9}')

    while True:
        print(F'{"<" * 20} НАЧНЁМ! {">" * 20}')

        for i, j in sample:
            print(i)

            question = input("Ваш ответ! ")

            if question == j:
                print("Верно!")
                score += 1

            else:
                print("Не верный ответ!")
                data = j
                day, month, year = data.split('.')
                print(days[day], months[month], year, 'года')
        print("Вы ответили верно на", score, "из 5")

        answer = str(input("Проити викторину ещё раз? (да/нет) ")).lower()
        if answer == "да":
            print("Отлично!")

        elif answer == "нет":
            break

    print("До свидания!")

def wallet():

    FILE_NAME = 'orders.txt'
    orders = []
    bull_sum = 0

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'rb') as f:
            orders = pickle.load(f)
            bull_sum = pickle.load(f)

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f"На вашем счёте: {bull_sum}", " Руб")

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            cost = int(input("Введите сумму: "))
            bull_sum += cost

            if bull_sum <= 0:
                print(f'{"*" * 10} Введите сумму для зачисления! {"*" * 10}')

            elif bull_sum >= 0:
                orders.append(f'{bull_sum}')
                print(f'{"*" * 10} Зачисленно! {"*" * 10}')

        elif choice == '2':
            cost = int(input("Введите сумму покупки: "))
            if cost > bull_sum:
                print(f'{"*" * 10} Недостаточно средств! {"*" * 10}')
            else:
                bull_sum -= cost
                name = input("Введите название покупки: ")
                orders.append((name, cost))
                print(f'{"*" * 10} Приобритено! {"*" * 10}')
                print(f"На вашем счёте: {bull_sum}", " Руб")

        elif choice == '3':
            for order in orders:
                print(order)

        elif choice == '4':
            with open(FILE_NAME, 'wb') as f:
                pickle.dump(orders, f)
                pickle.dump(bull_sum, f)
            break

        else:
            print(F"{'>-<' * 5}Неверный пункт меню{'>-<' * 5}")

    f.close()

def exit():
    answer = input('Заврешаем работу? (да/нет)? ')
    if answer == "да":
        print("До свидания!")
        sys.exit()

    elif answer == 'нет':
        print("Хорошо, продолжаем!")
        return


if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'Получается....''\n' 'Пока что =)')
    create_folder('new_folder1')
    get_list()
    get_list(True)
    delete_file('new_folder1')
    delete_file('text.dat')
    copy_file('new_folder', ' new2')
    create_file('text.dat')
    copy_file('text.dat', 'text2.dat')
    save_info('начало и конец')
    wallet()
    victory()
    exit()