import tkinter as tk
from Application import Application


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.pack()
    root.geometry("1000x560+500+200")
    root.configure(bg='#AFEEEE')
    root.resizable(False, False)
    root.title("Морской бой")
    root.config(menu=app.mainMenu)
    app.fileMenu.add_command(label='Выход', command=root.destroy)
    root.mainloop() 