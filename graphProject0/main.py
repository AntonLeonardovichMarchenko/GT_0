print('Hello! this is python...')
# This is a sample Python graph script.
import tkinter as tk

def goWindow():
    window = tk.Tk()
    window.geometry('450x450')
    window.title('примеры построения графиков')

    window.mainloop()

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    goWindow()


if __name__ == '__main__':
    print_hi('PyCharm graph script')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
