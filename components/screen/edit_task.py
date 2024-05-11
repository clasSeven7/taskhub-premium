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
        self.root.title("TaskHub - Editar Tarefas")
        self.root.configure(bg="#2684FF")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=550, height=450)

    def frames(self):
        self.frame_1 = Frame(self.root, bg="#fff", bd=4)
        self.frame_1.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.60)

        self.frame_2 = Frame(self.root, bg="#fff", bd=4)
        self.frame_2.place(relx=0.02, rely=0.66, relwidth=0.96, relheight=0.31)

    def widgets_frame_1(self):
        # Label Título
        self.lb_title = Label(
            self.frame_1, text="Editar Tarefa", bg="#fff", font=("Arial", 20), fg="#2684FF")
        self.lb_title.place(relx=0.33, rely=0.01)

        # Label Índice
        self.lb_index = Label(
            self.frame_1, text="Índice:", bg="#fff", font=("Arial", 12, "bold"), fg="#2684FF")
        self.lb_index.place(relx=0.01, rely=0.16)
        self.input_index = Entry(self.frame_1)
        self.input_index.place(relx=0.01, rely=0.24, relwidth=0.1)

        # Label Descrição
        self.lb_description = Label(
            self.frame_1, text="Descrição da tarefa:", bg="#fff", font=("Arial", 12, "bold"), fg="#2684FF")
        self.lb_description.place(relx=0.13, rely=0.16)
        self.input_description = Entry(self.frame_1)
        self.input_description.place(relx=0.13, rely=0.24, relwidth=0.85)

        # Botão Limpar
        self.bt_clear = Button(self.frame_1, text="Limpar",
                               bg="#2684FF", fg="#fff", font=("Arial", 12))
        self.bt_clear.place(relx=0.13, rely=0.80, relwidth=0.3, relheight=0.14)

        # Botão Adicionar
        self.bt_add = Button(self.frame_1, text="Editar",
                             bg="#2684FF", fg="#fff", font=("Arial", 12))
        self.bt_add.place(relx=0.55, rely=0.80, relwidth=0.3, relheight=0.14)


Application()
