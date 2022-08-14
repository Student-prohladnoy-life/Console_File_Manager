import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, wallet, victory, exit, info_platform, info_developer

save_info('Старт')

command = sys.argv[1]

if command == 'list':
    get_list()

elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)

elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название папки')
    else:
        create_folder(name)

elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название удаляемой папки или файла')
    else:
        delete_file(name)

elif command == 'copy':
    name = sys.argv[2]
    new_name = sys.argv[3]
    copy_file(name, new_name)

elif command == 'info_platform':
    info_platform()

elif command == 'info_developer':
    info_developer()

elif command == 'victory':
    victory()

elif command == 'wallet':
    wallet()


elif command == 'help':
    print('info_developer - информация о разработчике')
    print('info_platform - информация о системе')
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создаание папки')
    print('delete - удаление файла или папки')
    print('copy_file -  копирование файла или папки')
    print('victory - игра викторина')
    print('wallet - банковский счёт')
    print('exit - выход из программы')


elif command == 'exit':
    exit()

save_info('Конец')