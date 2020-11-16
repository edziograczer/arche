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
    e = input('chchcesz zabezpieczyć hasłem? (y/n): ')
    if '.zip' or '.rar' or '.tar' or '.tar.xz' or '.tar.gz' not in d:
        f = input('jakie hasło?: ')
    else:
        pass
    if '.zip' in d:
        if e == 'n':
            os.system(f'zip -r {d} {c}')
        if e == 'y':
            os.system(f'zip -re {d} {c}')
    if '.rar' in d:
        if e == 'y':
            os.system(f'rar a {d} {c}')
        if e == 'n':
            os.system(f'rar a -p {d} {c}')
    if '.7z' in d:
        if e == 'y':
            os.system(f'7z a {d} {c}')
        if e == 'n':
            os.system(f'7z a {d} {c} -p"{e}"')
    if '.tar' in d:
        os.system(f'tar cf {d} {c}')
    if '.tar.gz' or '.tar.xz' in d:
        os.system(f'tar -czfv {d} {c}')
