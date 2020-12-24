from tkinter import *
import pymysql
import subprocess
class tkinter(object):
    def connect(self):
        try:
            self.y = pymysql.connect(
                host = "localhost",
                user="kali",
                password="root",
                db="principal",
            )
            self.cursor = self.y.cursor()
            print("Conexion exitosa")
        except pymysql.Error as e:
            print("Ha ocurrido un error", e)
        self.sql = "SHOW DATABASES;"
        print(self.sql)
        try:
            self.cursor.execute(self.sql)
            self.output = self.cursor.fetchall()
            for self.dbs in self.output:
                """
                self.look = Label(self.ventana, command= lambda: print(self.dbs))
                self.look.pack()
                """
                print("Resultado", self.dbs)

        except Exception as e:
            raise
#    @classmethod
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Mysql conector")
        self.ventana.geometry("800x600")
        self.photo = PhotoImage(file="mysql.png")
        self.my_label = Label(self.ventana, image=self.photo)
        self.my_label.pack()
        self.boton = Button(self.ventana, text="Enviar comando", command=self.init)
        self.entry_text = Entry(self.ventana, font="Helvetica 30")
        self.entry_text.pack()
        self.boton.pack()
        self.ventana.mainloop()
#    def conector(self):
#        self.conector = conector
#        self.mysql = mysql
"""
        try:
            self.y = pymysql.connect(
                host = "localhost",
                user="kali",
                password="root",
                db="principal",
            )
            self.cursor = self.y.cursor()
            print("Conexion exitosa")
        except pymysql.Error as e:
            print("Ha ocurrido un error", e)
        self.sql = "SHOW DATABASES;"
        print(self.sql)
        try:
            self.cursor.execute(self.sql)
            self.output = self.cursor.fetchall()
            for self.dbs in self.output:
                self.look = Label(self.ventana, command= lambda: print(self.dbs))
                self.look.pack()
                print("Resultado", self.dbs)

        except Exception as e:
            raise
    def text(self):
        self.texto = self.boton.get()
        print(self.texto)
"""
main = tkinter()






