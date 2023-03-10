from tkinter import *
from tkinter import filedialog
import customtkinter
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader

# x - lados
# y - baixo cima


class AppMain():
    def __init__(self):
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        self.app.geometry("400x200")
        self.app.title("Juntar PDF")

        lb_name = customtkinter.CTkLabel(master=self.app, text="Juntar PDF",font=('Arial', 30, 'bold'))
        lb_name.pack(padx=1, pady=2)
        btn_open = customtkinter.CTkButton(master=self.app, text="Adicionar e Juntar", command=open_folder)
        btn_open.place(x=120,y=100)


        self.app.mainloop()


def open_folder():

    merger = PdfWriter()
    
    arquivos = filedialog.askopenfilenames(
        title="Selecione os arquivos de pdf",
        filetypes=(("Arquivos pdf", "*.pdf"), ("Todos os arquivos", "*.*"))
    )
    
    for pdf in arquivos:
        merger.append(pdf)

    output = open("./arquivo_junto.pdf", "wb")
    merger.write(output)
    merger.close()

    messagebox.showinfo(title="Ok", message="Concluido!")
    
def main():
    AppMain()
    


if __name__=="__main__":
    main()