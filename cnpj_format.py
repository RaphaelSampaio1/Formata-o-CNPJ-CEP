import tkinter as tk
from tkinter import messagebox

def format():
    cnpj = cnpj_entry.get().strip()
    formated_cnpj = ''.join(filter(str.isdigit, cnpj))
    result_label.config(text=formated_cnpj)

    result_label.delete(0, tk.END)
    result_label.insert(0, formated_cnpj)

root = tk.Tk()
root.geometry('150x170')
root.title('CNPJ FORMAT')

tk.Label(root,text='Insert Cnpj').grid(row=0, column=0, padx=10, pady=10)
cnpj_entry = tk.Entry(root, width=20)
cnpj_entry.grid(row=1, column=0, padx=10, pady=10)

tk.Label(root, text='Formated CNPJ: ').grid(row=2, column=0, pady=10, padx=10)
result_label = tk.Entry(root, width=20)
result_label.grid(row=2, column=0, padx=10, pady=10)

format_button = tk.Button(root, text='Format', command=format)
format_button.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()



