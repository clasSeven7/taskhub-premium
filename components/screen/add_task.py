from tkinter import *
from tkinter import ttk

root = Tk()


class Funcs:
    def clean_screen(self):
        self.input_description.delete(0, END)
        self.input_priority.delete(0, END)
        self.input_status.delete(0, END)


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.display()
        self.frames()
        self.widgets_frame_1()
        self.list_frame_2()
        root.mainloop()

    def display(self):
        self.root.title("TaskHub - Adicionar Tarefas")
        self.root.configure(bg="#2684FF")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=550, height=450)

    def frames(self):
        self.frame_1 = Frame(self.root, bg="#fff", bd=4)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bg="#fff", bd=4)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.47)

    def widgets_frame_1(self):
        # Label Título
        self.lb_title = Label(
            self.frame_1, text="Adicionar Tarefa", bg="#fff", font=("Arial", 20), fg="#2684FF")
        self.lb_title.place(relx=0.33, rely=0.01)

        # Label Descrição
        self.lb_description = Label(
            self.frame_1, text="Descrição da tarefa:", bg="#fff", font=("Arial", 12, "bold"), fg="#2684FF")
        self.lb_description.place(relx=0.01, rely=0.2)
        self.input_description = Entry(self.frame_1)
        self.input_description.place(relx=0.01, rely=0.32, relwidth=0.98)

        # Label Prioridade
        self.lb_priority = Label(
            self.frame_1, text="Prioridade (alta, média, baixa):", bg="#fff", font=("Arial", 12, "bold"), fg="#2684FF")
        self.lb_priority.place(relx=0.01, rely=0.50)
        self.input_priority = Entry(self.frame_1)
        self.input_priority.place(relx=0.01, rely=0.62, relwidth=0.40)

        # Label Status
        self.lb_status = Label(
            self.frame_1, text="Status (pendente, em andamento, concluída):", bg="#fff", font=("Arial", 12, "bold"), fg="#2684FF")
        self.lb_status.place(relx=0.43, rely=0.50)
        self.input_status = Entry(self.frame_1)
        self.input_status.place(relx=0.43, rely=0.62, relwidth=0.56)

        # Botão Limpar
        self.bt_clear = Button(self.frame_1, text="Limpar",
                               bg="#2684FF", fg="#fff", font=("Arial", 12), command=self.clean_screen)
        self.bt_clear.place(relx=0.16, rely=0.78,
                            relwidth=0.33, relheight=0.16)

        # Botão Adicionar
        self.bt_add = Button(self.frame_1, text="Adicionar",
                             bg="#2684FF", fg="#fff", font=("Arial", 12))
        self.bt_add.place(relx=0.50, rely=0.78, relwidth=0.33, relheight=0.16)

    def list_frame_2(self):
        self.listCLi = ttk.Treeview(
            self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listCLi.heading("#0", text="")
        self.listCLi.heading("#1", text="Índice")
        self.listCLi.heading("#2", text="Descrição")
        self.listCLi.heading("#3", text="Prioridade")
        self.listCLi.heading("#4", text="Status")

        self.listCLi.column("#0", width=1)
        self.listCLi.column("#1", width=50)
        self.listCLi.column("#2", width=200)
        self.listCLi.column("#3", width=100)
        self.listCLi.column("#4", width=100)

        self.listCLi.place(relx=0.01, rely=0.01,
                           relwidth=0.95, relheight=0.98)

        self.scrool_list = Scrollbar(self.frame_2, orient="vertical")
        self.listCLi.configure(yscroll=self.scrool_list.set)
        self.scrool_list.place(relx=0.96, rely=0.01,
                               relwidth=0.03, relheight=0.98)


Application()
