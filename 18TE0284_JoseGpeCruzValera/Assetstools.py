import time

def cargando():
    if input('Cargando...' + '\n' + 'Presiona enter para continuar') == '':
        print('\n')
        x= 3
        for i in range(x):
            print("...")
            time.sleep(1)
        time.sleep(0.5)
    print(' 1 nueva notificacion')

def cargando2():
    print("\nGracias por usar el programa")
    print('Cerrando  ⏱️')
    x= 3
    for i in range(x):
        print("...",x-i)
        time.sleep(1)

def cargando3():
    x= 3
    for i in range(x):
        print("...")
        time.sleep(1)

def cargandoN(seg):
    print('Cargando...')
    seg = seg
    for i in range(seg):
        print("...")
        time.sleep(1)

def descargar():
    time.sleep(1)
    print('Descargado...')
    time.sleep(3)
    x= 3
    for i in range(x):
        print("...",round((x+i)*(50/3),2),'%')
        time.sleep(1)
    print(100,'%')
    print("Archivo Guardado revisar archivo csv")


#testeo de Asssetstools
# cargando()
# cargando2()
# cargando3()
# cargandoN(5)