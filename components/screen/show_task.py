from tkinter import *

root = Tk()


class Application:
    def __init__(self):
        self.root = root
        self.display()
        self.frames()
        self.widgets_frame_1()
        root.mainloop()

    def display(self):
        self.root.title("TaskHub - Adicionar Tarefas")
        self.root.configure(bg="#2684FF")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

    def frames(self):
        self.frame_1 = Frame(self.root, bg="#fff", bd=4)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bg="#fff", bd=4)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame_1(self):
        # Botão Limpar
        self.bt_clear = Button(self.frame_1, text="Limpar",
                               bg="#2684FF", fg="#fff", font=("Arial", 12))
        self.bt_clear.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # botão Buscar
        self.bt_search = Button(self.frame_1, text="Buscar",
                                bg="#2684FF", fg="#fff", font=("Arial", 12))
        self.bt_search.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # botão Adicionar
        self.bt_add = Button(self.frame_1, text="Adicionar",
                             bg="#2684FF", fg="#fff", font=("Arial", 12))
        self.bt_add.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        # botão Editar
        self.bt_edit = Button(self.frame_1, text="Editar",
                              bg="#2684FF", fg="#fff", font=("Arial", 12))
        self.bt_edit.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)
        # botão Remover
        self.bt_remove = Button(self.frame_1, text="Remover",
                                bg="#2684FF", fg="#fff", font=("Arial", 12))
        self.bt_remove.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # botão Mostrar
        self.bt_show = Button(self.frame_1, text="Mostrar",
                              bg="#2684FF", fg="#fff", font=("Arial", 12))
        self.bt_show.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)


Application()
