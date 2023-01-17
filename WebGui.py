import math
import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation# make the calculation function global
    calculation += str(symbol)
    text_result.delete(1.0, "end")# how we delete all the result fields
    text_result.insert(1.0, calculation)



    

def evaluate_calculation():
    global calculation
    try:

       calculation = str(eval(calculation))
       text_result.delete(1.0, "end")
       text_result.insert(1.0, calculation)

    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global  calculation
    calculation = ""
    text_result.delete(1.0, "end")



root = tk.Tk()#endpoints
root.geometry("400x375")

text_result = tk.Text(root, height=2, width=24, font=("Arial", 24))
text_result.grid(columnspan=9)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial") )
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial") )
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial") )
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial") )
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial") )
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial") )
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial") )
btn_7.grid(row=4, column=1)


btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial") )
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial") )
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial") )
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial") )
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial") )
btn_minus.grid(row=3, column=4)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial") )
btn_mul.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial") )
btn_div.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial") )
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial") )
btn_close.grid(row=5, column=3)

btn_sqrt = tk.Button(root, text="^", command= lambda:  add_to_calculation ("^"), width=5, font=("Arial") )
btn_sqrt.grid(row=6, column=4)

btn_log = tk.Button(root, text="log", command= lambda: add_to_calculation("log"), width=5, font=("Arial") )
btn_log.grid(row=6, column=1)

btn_cos = tk.Button(root, text="cos", command= lambda : add_to_calculation(math.cos(num)), width=5, font=("Arial") )
btn_cos.grid(row=6, column=2)

btn_sin = tk.Button(root, text="sin", command= lambda : add_to_calculation("sin"), width=5, font=("Arial") )
btn_sin.grid(row=6, column=3)

btn_clear = tk.Button(root, text="C", command= clear_field, width=12, font=("Arial") )
btn_clear.grid(row=7, column=1, columnspan=2)



btn_equals = tk.Button(root, text="=", command= evaluate_calculation, width=12, font=("Arial") )
btn_equals.grid(row=7, column=3, columnspan=3)




root.mainloop()

