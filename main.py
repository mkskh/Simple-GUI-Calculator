import tkinter as tk


calculation = ''


def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    screen.delete(1.0, 'end')
    screen.insert(1.0, calculation)


def get_result():
    try:
        global calculation
        calculation = str(eval(calculation))
        screen.delete(1.0, 'end')
        screen.insert(1.0, calculation)
    except:
        remove_field()
        screen.insert(1.0, 'Error')


def remove_field():
    global calculation
    screen.delete(1.0, 'end')
    calculation = ''

window = tk.Tk()
window.geometry('315x255')
window.title('Calculator')

screen = tk.Text(window, height=2, width=17, font=('Arial', 24))
screen.grid(columnspan=5)

btn1 = tk.Button(window, text='1', width='5', font=('Arial', 14), command= lambda: add_to_calc(1))
btn1.grid(row=2, column=1)
btn2 = tk.Button(window, text='2', width='5', font=('Arial', 14), command= lambda: add_to_calc(2))
btn2.grid(row=2, column=2)
btn3 = tk.Button(window, text='3', width='5', font=('Arial', 14), command= lambda: add_to_calc(3))
btn3.grid(row=2, column=3)
btn4 = tk.Button(window, text='4', width='5', font=('Arial', 14), command= lambda: add_to_calc(4))
btn4.grid(row=3, column=1)
btn5 = tk.Button(window, text='5', width='5', font=('Arial', 14), command= lambda: add_to_calc(5))
btn5.grid(row=3, column=2)
btn6 = tk.Button(window, text='6', width='5', font=('Arial', 14), command= lambda: add_to_calc(6))
btn6.grid(row=3, column=3)
btn7 = tk.Button(window, text='7', width='5', font=('Arial', 14), command= lambda: add_to_calc(7))
btn7.grid(row=4, column=1)
btn8 = tk.Button(window, text='8', width='5', font=('Arial', 14), command= lambda: add_to_calc(8))
btn8.grid(row=4, column=2)
btn9 = tk.Button(window, text='9', width='5', font=('Arial', 14), command= lambda: add_to_calc(9))
btn9.grid(row=4, column=3)
btn0 = tk.Button(window, text='0', width='5', font=('Arial', 14), command= lambda: add_to_calc(0))
btn0.grid(row=5, column=2)
btn_open = tk.Button(window, text='(', width='5', font=('Arial', 14), command= lambda: add_to_calc('('))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(window, text=')', width='5', font=('Arial', 14), command= lambda: add_to_calc(')'))
btn_close.grid(row=5, column=3)
btn_div = tk.Button(window, text='/', width='5', font=('Arial', 14), command= lambda: add_to_calc('/'))
btn_div.grid(row=2, column=4)
btn_mul = tk.Button(window, text='*', width='5', font=('Arial', 14), command= lambda: add_to_calc('*'))
btn_mul.grid(row=3, column=4)
btn_minus = tk.Button(window, text='-', width='5', font=('Arial', 14), command= lambda: add_to_calc('-'))
btn_minus.grid(row=4, column=4)
btn_plus = tk.Button(window, text='+', width='5', font=('Arial', 14), command= lambda: add_to_calc('+'))
btn_plus.grid(row=5, column=4)
btn_delete = tk.Button(window, text='C', width='13', font=('Arial', 14), command=remove_field )
btn_delete.grid(row=6, column=1, columnspan=2)
btn_equals = tk.Button(window, text='=', width='13', font=('Arial', 14), command=get_result)
btn_equals.grid(row=6, column=3, columnspan=2)


window.mainloop()