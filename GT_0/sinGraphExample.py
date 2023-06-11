import tkinter as tk

def goGraph():

    window = None
    def initWindow():
        window = tk.Tk()
        window.geometry("500x500")
        window.title("построение графиков")
        window.mainloop()

    initWindow()



goGraph()