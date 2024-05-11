from tkinter import *

root = Tk()


def adicionar_tarefa():
    import components.screen.add_task
    root.withdraw()


def remover_tarefa():
    import components.screen.edit_task
    root.withdraw()


def editar_tarefa():
    import components.screen.remove_task
    root.withdraw()


def mostrar_tarefas():
    import components.screen.show_task
    root.withdraw()


class Application:
    def __init__(self):
        self.root = root
        self.display()
        self.main_frame()
        self.image()
        self.buttons()
        root.mainloop()

    def display(self):
        self.root.title("TaskHub - Gerenciador de Tarefas")
        self.root.configure(bg="#2684FF")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=550, height=450)

    def main_frame(self):
        self.frame = Frame(self.root, bg="#fff", bd=4)
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def image(self):
        self.img = PhotoImage(file="./assets/logo.png")
        self.img_label = Label(self.frame, image=self.img, bg="#fff")
        self.img_label.place(relx=0.01, rely=0.01,
                             relwidth=0.96, relheight=0.3)

    def buttons(self):
        # botão Adicionar
        self.bt_add = Button(self.frame, text="Adicionar", bd=2,
                             bg="#2684FF", fg="#fff", font=("Arial", 12, "bold"), command=adicionar_tarefa)
        self.bt_add.place(relx=0.31, rely=0.4, relwidth=0.4, relheight=0.12)
        # botão Editar
        self.bt_edit = Button(self.frame, text="Editar", bd=2,
                              bg="#2684FF", fg="#fff", font=("Arial", 12, "bold"), command=editar_tarefa)
        self.bt_edit.place(relx=0.31, rely=0.53, relwidth=0.4, relheight=0.12)
        # botão Remover
        self.bt_remove = Button(self.frame, text="Remover", bd=2,
                                bg="#2684FF", fg="#fff", font=("Arial", 12, "bold"), command=remover_tarefa)
        self.bt_remove.place(relx=0.31, rely=0.66,
                             relwidth=0.4, relheight=0.12)
        # botão Mostrar
        self.bt_show = Button(self.frame, text="Mostrar", bd=2,
                              bg="#2684FF", fg="#fff", font=("Arial", 12, "bold"), command=mostrar_tarefas)
        self.bt_show.place(relx=0.31, rely=0.79, relwidth=0.4, relheight=0.12)


Application()
