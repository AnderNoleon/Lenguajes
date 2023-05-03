from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QFrame
from PyQt5 import uic
import os
import os.path
import sys
import re


class MainView(QMainWindow):
    def __init__(self) -> None:
        super(MainView, self).__init__()

        # Load Ui
        uic.loadUi('views/designs/controlador.ui', self)

        self.busca_btn.clicked.connect(self.buscar_archivo_txt)
        # ver los simbolos dobles, y ver palabras
        self.ingresa_btn_2.clicked.connect(self.contar_palabra)
        self.ingresa_btn_4.clicked.connect(self.contar_numeros)
        self.ingresa_btn_2.clicked.connect(self.contar_ABC)
        # botones
        self.ingresa_btn_2.clicked.connect(self.ver_suma)
        self.ingresa_btn_2.clicked.connect(self.ver_menos)
        self.ingresa_btn_2.clicked.connect(self.ver_multi)
        self.ingresa_btn_2.clicked.connect(self.ver_igual)
        self.ingresa_btn_2.clicked.connect(self.ver_porcentaje)
        # conjunto de todo
        self.ingresa_btn_2.clicked.connect(self.ver_signos)
        # para palabras
        self.ingresa_btn_2.clicked.connect(self.ver_pa)

        # guardar
        self.ingresa_btn_5.clicked.connect(self.guardar_archivo)

        # error de signos
        self.ingresa_btn_2.clicked.connect(self.error_signos)
        self.ingresa_btn_2.clicked.connect(self.check_booleano_structure)
        self.ingresa_btn_2.clicked.connect(self.check_booleanoo_structure)
        self.ingresa_btn_2.clicked.connect(self.hacer)
        self.ingresa_btn_2.clicked.connect(self.check_if_structure)

    def buscar_archivo_txt(self) -> None:
        fname =QFileDialog.getOpenFileName(self, 'Open file', 'E:\Anderson')
        self.filename.setText(fname[0])

    # operadores / palabras
    def contar_palabra(self) -> None:
        filename = self.filename_2.text()
        try:
            with open(filename) as f_obj:
                contents = f_obj.read()
                print(contents)
        except FileNotFoundError:
            msg = "mm aparece el archivo " + filename + "no existe"
            self.textEdit.setText(" " + str(msg))
        else:
            words = contents.split()
            num_words = len(words)
            print("EL ARCHIVO " + filename + " contiene " + str(num_words))
            self.textEdit_3.setText(str(contents))

            #division = words.count('/')
            igualigual = words.count('==')
            mayorigual = words.count('>=')
            menorigual = words.count('<=')

            # palabras
            # self.division.setText(str(division))
            self.op1_7.setText(str(igualigual))
            self.op1_10.setText(str(mayorigual))
            self.op1_11.setText(str(menorigual))

    def contar_numeros(self) -> None:
        ruta_de_archivo = self.filename_2.text()
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer contenido del archivo
            contenido = archivo.read()

        # Inicializar contador de dígitos
        num_digitos = 0

        # Recorrer contenido del archivo
        for caracter in contenido:
            # Verificar si el caracter es un dígito
            if caracter.isdigit():
                num_digitos += 1

        # Imprimir resultado
        self.tx_numero.setText(f" Numeros:  {str(num_digitos)}")
        print('El archivo contiene', num_digitos, 'dígitos.')

    def contar_ABC(self) -> None:
        ruta_de_archivo = self.filename_2.text()
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer contenido del archivo
            contenido = archivo.read()

        # Inicializar contador de signos
        num_signos = 0

        # Recorrer contenido del archivo
        for caracter in contenido:
            # Verificar si el caracter es un signo y no es un espacio
            if caracter.isalnum() and not caracter.isspace():
                num_signos += 1

        # Imprimir resultado
        print('El archivo contiene', num_signos, 'signos (sin contar los espacios).')
        self.indicardor.setText(f" El archivo contiene letras'  {str(num_signos)}")

    # aqui

    def ver_signos(self) -> None:
        # ----------------------------------------

        signos = ['<']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.menor.setText(str(contador))
        # ----------------------------------------


        signos = ['>']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.mayor.setText(str(contador))
        # ----------------------------------------

        signos = ['<']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.menor.setText(str(contador))
        # ----------------------------------------

        signos = ['(']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.parentesis_iz.setText(str(contador))
        # ----------------------------------------

        signos = [')']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.parentesis_de.setText(str(contador))
        # ----------------------------------------

        signos = ['{']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.llave_iz.setText(str(contador))
        # ----------------------------------------

        signos = ['}']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.llave_de.setText(str(contador))
        # ----------------------------------------

        signos = ['"']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.comillas.setText(str(contador))
        # ----------------------------------------

        signos = [';']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.punto_coma.setText(str(contador))

    def ver_suma(self) -> None:
        signos = ['+']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.op1.setText(str(contador))

    def ver_menos(self) -> None:
        signos = ['-']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.op1_2.setText(str(contador))

    def ver_multi(self) -> None:
        signos = ['*']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador_1 = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador_1 += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador_1} signos en el archivo.")
        self.op1_3.setText(str(contador_1))

    def ver_igual(self) -> None:
        signos = ['=']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador} signos en el archivo.")
        self.igual.setText(str(contador))

    def ver_porcentaje(self) -> None:
        signos = ['%']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Inicializar contador
            contador_2 = 0

            # Iterar sobre cada carácter del contenido
            for caracter in contenido:
                # Si el carácter es un signo y no un espacio
                if caracter in signos and caracter != ' ' and not caracter.isspace():
                    # Incrementar el contador
                    contador_2 += 1

        # Imprimir la cantidad de signos encontrados
        print(f"Se encontraron {contador_2} signos en el archivo.")
        self.porcentaje.setText(str(contador_2))

    def ver_pa(self) -> None:

        palabras = ["entero"]

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Inicializar contador
            contador = 0

            # Iterar sobre cada línea del archivo
            for linea in archivo:
                # Separar la línea en palabras
                palabras_linea = linea.strip().split()

                # Iterar sobre cada palabra de la línea
                for palabra in palabras_linea:
                    # Si la palabra está en la lista de palabras buscadas
                    if palabra in palabras:
                        # Incrementar el contador
                        contador += 1
        # Definir la palabra que deseas contar

        # (f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        print(f"Se encontraron {contador} veces las palabras {', '.join(palabras)} en el archivo.")
        self.entero.setText(str(contador))

        palabra = "decimal"

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Separar el contenido en palabras
            palabras = contenido.split()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada palabra
            for p in palabras:
                # Si la palabra es igual a la palabra buscada
                if p == palabra:
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de palabras encontradas
        print(f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        self.op1_20.setText(str(contador))

        palabra = "booleano"

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Separar el contenido en palabras
            palabras = contenido.split()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada palabra
            for p in palabras:
                # Si la palabra es igual a la palabra buscada
                if p == palabra:
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de palabras encontradas
        print(f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        self.op1_21.setText(str(contador))

        palabra = "cadena"

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Separar el contenido en palabras
            palabras = contenido.split()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada palabra
            for p in palabras:
                # Si la palabra es igual a la palabra buscada
                if p == palabra:
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de palabras encontradas
        print(f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        self.op1_22.setText(str(contador))

        palabra = "si"

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Separar el contenido en palabras
            palabras = contenido.split()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada palabra
            for p in palabras:
                # Si la palabra es igual a la palabra buscada
                if p == palabra:
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de palabras encontradas
        print(f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        self.op1_23.setText(str(contador))

        palabra = "sino"

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Separar el contenido en palabras
            palabras = contenido.split()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada palabra
            for p in palabras:
                # Si la palabra es igual a la palabra buscada
                if p == palabra:
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de palabras encontradas
        print(f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        self.op1_24.setText(str(contador))

        palabra = "falso"

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Separar el contenido en palabras
            palabras = contenido.split()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada palabra
            for p in palabras:
                # Si la palabra es igual a la palabra buscada
                if p == palabra:
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de palabras encontradas
        print(f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        self.op1_28.setText(str(contador))

        palabra = "verdadero"

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Separar el contenido en palabras
            palabras = contenido.split()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada palabra
            for p in palabras:
                # Si la palabra es igual a la palabra buscada
                if p == palabra:
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de palabras encontradas
        print(f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        self.op1_27.setText(str(contador))

        palabra = "hacer"

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Separar el contenido en palabras
            palabras = contenido.split()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada palabra
            for p in palabras:
                # Si la palabra es igual a la palabra buscada
                if p == palabra:
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de palabras encontradas
        print(f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        self.op1_26.setText(str(contador))

        palabra = "mientras"

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Separar el contenido en palabras
            palabras = contenido.split()

            # Inicializar contador
            contador = 0

            # Iterar sobre cada palabra
            for p in palabras:
                # Si la palabra es igual a la palabra buscada
                if p == palabra:
                    # Incrementar el contador
                    contador += 1

        # Imprimir la cantidad de palabras encontradas
        print(f"Se encontraron {contador} veces la palabra '{palabra}' en el archivo.")
        self.op1_25.setText(str(contador))

    def guardar_archivo(self):
        # Abrir el diálogo de selección de archivo
        ruta_de_archivo = self.filename_2.text()
        # Si se seleccionó un archivo
        if ruta_de_archivo:
            # Abrir el archivo en modo escritura
            with open(ruta_de_archivo, 'w') as archivo:
                # Escribir el contenido del QTextEdit en el archivo
                archivo.write(self.textEdit_3.toPlainText())

            # Mostrar un mensaje de confirmación
            print("La información ha sido guardada en el archivo correctamente.")

    def error_signos(self) -> None:
        signos = ['?', '!', '^', '#', '@', '&']

        # Definir la ruta del archivo de texto
        ruta_de_archivo = self.filename_2.text()

        # Abrir el archivo en modo lectura
        with open(ruta_de_archivo, 'r') as archivo:
            # Inicializar contador y línea
            contador = 0
            linea = 0

            # Iterar sobre cada línea del archivo
            for texto_linea in archivo:
                # Incrementar contador de línea
                linea += 1

                # Iterar sobre cada carácter de la línea
                for caracter in texto_linea:
                    # Si el carácter es un signo y no un espacio
                    if caracter in signos and caracter != ' ':
                        # Incrementar el contador
                        contador += 1
                        # Imprimir la línea y el carácter encontrado
                        print(f"Se encontró el signo '{caracter}' en la línea {linea}: {texto_linea}")
                        msg = f"Se encontró el signo '{caracter}' en la línea {linea}: {texto_linea}"
                        QMessageBox.critical(self, 'Error', msg)

        # Imprimir la cantidad de signos encontrados

    def check_for_strucature(self) -> None:
        ruta_de_archivo = self.filename_2.text()

        with open(ruta_de_archivo, 'r') as f:
            lines = f.readlines()

        for line in lines:
            if 'for' in line:
                if '(' in line and ')' in line:
                    if ';' in line:
                        # si la línea contiene ";" después de la condición del for, entonces la estructura es incorrecta
                        QMessageBox.critical(self, 'Error',
                                             'La estructura del for es incorrecta en el archivo "{}"'.format(
                                                 ruta_de_archivo),
                                             QMessageBox.Ok)
                        return False
                    else:
                        # si la línea no contiene ";", entonces verificamos que haya dos puntos (:) después de la condición del for
                        if ':' in line:
                            return True
                        else:
                            QMessageBox.critical(self, 'Error',
                                                 'La estructura del for es incorrecta en el archivo "{}"'.format(
                                                     ruta_de_archivo),
                                                 QMessageBox.Ok)
                            return False

        # si no se encuentra ninguna línea "for", entonces se considera que la estructura es incorrecta
        QMessageBox.critical(self, 'Error',
                             'La estructura del for es incorrecta en el archivo "{}"'.format(
                                 ruta_de_archivo),
                             QMessageBox.Ok)
        return False

    def check_for_structure(self) -> None:
        ruta_de_archivo = self.filename_2.text()

        with open(ruta_de_archivo, 'r') as f:
            lines = f.readlines()

        for line in lines:
            if 'for' in line:
                if '(' in line and ')' in line:
                    if ';' in line:
                        # si la línea contiene ";" después de la condición del for, entonces la estructura es incorrecta
                        QMessageBox.critical(self, 'Error',
                                             'La estructura del for es incorrecta en el archivo "{}"'.format(
                                                 ruta_de_archivo),
                                             QMessageBox.Ok)
                        return False
                    else:
                        # si la línea no contiene ";", entonces verificamos que haya dos puntos (:) después de la condición del for
                        if ':' in line:
                            # si la línea comienza con "for" y hay algo más después de los dos puntos (:) entonces la estructura es incorrecta
                            if line.strip().startswith('for') and len(line.split(':', 1)[1].strip()) > 0:
                                QMessageBox.critical(self, 'Error',
                                                     'La estructura del for es incorrecta en el archivo "{}"'.format(
                                                         ruta_de_archivo),
                                                     QMessageBox.Ok)
                                return False
                            else:
                                return True
                        else:
                            QMessageBox.critical(self, 'Error',
                                                 'La estructura del for es incorrecta en el archivo "{}"'.format(
                                                     ruta_de_archivo),
                                                 QMessageBox.Ok)
                            return False

        # si no se encuentra ninguna línea "for", entonces se considera que la estructura es incorrecta
        QMessageBox.critical(self, 'Error',
                             'La estructura del for es incorrecta en el archivo "{}"'.format(
                                 ruta_de_archivo),
                             QMessageBox.Ok)
        return False

    # E:/Anderson/Tareas/ciclo 5/Lenguajes/Examen.txt

    def check_if_structure(self) -> None:
        ruta_de_archivo = self.filename_2.text()

        with open(ruta_de_archivo, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if re.match(r'^\s*if', line):
                match = re.search(r'[><]=?=?\s*\d+|[a-zA-Z]+\s*:', line)
                if not match:
                    QMessageBox.critical(self, 'Error',
                                         f"Error en línea {i + 1}: la estructura no es válida",
                                         QMessageBox.Ok)
                    return False
            else:
                continue

        return True

    def check_booleano_structure(self) -> None:
        ruta_de_archivo = self.filename_2.text()

        with open(ruta_de_archivo, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if 'booleano = verdadero' in line:
                continue  # Si la línea es correcta, continuar con la siguiente
            elif 'booleano =' in line and 'verdadero' in line.lower():
                QMessageBox.critical(self, 'Error',
                                     f"Error en línea {i + 1}: la palabra 'verdadero' debe escribirse en minúscula",
                                     QMessageBox.Ok)
                return False

        return True

    def check_booleanoo_structure(self) -> None:
        ruta_de_archivo = self.filename_2.text()

        with open(ruta_de_archivo, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if 'booleano = falso' in line:
                continue  # Si la línea es correcta, continuar con la siguiente
            elif 'booleano =' in line and 'Falso' in line:
                QMessageBox.critical(self, 'Error',
                                     f"Error en línea {i + 1}: la palabra 'Falso' debe escribirse en mayúsculas",
                                     QMessageBox.Ok)
                return False

        return True

    def hacer(self) -> None:
        ruta_de_archivo = self.filename_2.text()

        with open(ruta_de_archivo, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if re.match(r'^\s*mientras', line):
                match = re.search(r'[><]=?\s*\d+\s*hacer', line)
                if not match:
                    QMessageBox.critical(self, 'Error',
                                         f"Error en línea {i + 1}: la estructura no es válida",
                                         QMessageBox.Ok)
                    return False
            else:
                continue

        return True