def crear_carpeta(Direccion):
    import os
    import shutil
    print("Escriba el nombre de la carpeta")
    path = input('')
    path = os.path.join(Direccion, path)
    x = True
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        while x == True:
            print("La carpeta ya existe" + "\n" + "¿Desea sobreescribirla? (Y/N)")
            q = input()
            if q == 'y' or q == 'Y':
                shutil.rmtree(path)
                os.makedirs(path)
                print("La carpeta se sobrescribio")
                x = False
            if q == 'n' or q == 'N':
                print("La carpeta NO se sobrescribio")
                x = False
    result = path
    return result
