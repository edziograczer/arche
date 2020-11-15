import os
a = input("co chcesz zrobić? (de/kom): ")
if a == 'de':
    print('listowanie plików archiwizacyjnych: ')
    os.system('ls |grep -e ".zip"')
    os.system('ls |grep -e ".tar"')
    os.system('ls |grep -e ".7z"')
    os.system('ls |grep -e ".rar"')
    b =  input('podaj archiwum do dekompresji: ')
    if '.zip' in b:
        os.system(f'unzip {b}')
    if '.rar' in b:
        os.system(f'unrar x {b}')
    if '.7z' in b:
        os.system(f'7z x {b}')
    if '.tar' in b:
        os.system(f'tar -xf {b}')
if a == 'kom':
    print('listowanie plików: ')
    os.system('ls')
    c = input('pliki jakie chcesz spakować: ')
    d = input('nazwa archiwum: ')
    if '.zip' in d:
        os.system(f'zip -r {c} {d}')
    if '.rar' in d:
        os.system(f'rar a {d} {c}')
    if '.7z' in d:
        os.system(f'7z a {d} {c}')
    if '.tar' in d:
        os.system(f'tar cf {d} {c}')