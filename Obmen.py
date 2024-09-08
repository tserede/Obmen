from idlelib.editor import keynames
from sys import builtin_module_names

import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from  tkinter import ttk


cur={"RUB": "Российский рубль",
     "EUR": "Евро",
     "GBP":"Британский фунт стерлингов",
"JPY":"Японская йена",
"CNY":"Китайский юань",
"KZT":"Казахский тенге",
"UZS":"Узбекский сум",
"AED":"Дирхам ОАЭ",
"CHF":"Швейцарский франк",
"CAD":"Канадский доллар",
"USD":"Американский доллар"
}
def update_t_label(event):
    t_code=t_combobox.get()
    t_name=cur[t_code]
    t_label.config(text=t_name)

def update_b_label(event):
    b_code = b_combobox.get()
    b_name = cur[b_code]
    b_label.config(text=b_name)

def exchange():
    t_code=t_combobox.get()
    b_code=b_combobox.get()
    if t_code and b_code:
        try:

            responce=requests.get(f"http://open.er-api.com/v6/latest/{b_code}")
            responce.raise_for_status()
            data=responce.json()
            if t_code in data["rates"]:
                exchange_rates=data["rates"][t_code]
                t_name=cur[t_code]
                b_name=cur[b_code]
                mb.showinfo("Курс обмена",f"Курс:{exchange_rates:.2f} {t_name} за 1 {b_name} ")
            else:
                mb.showerror("Ошибка", f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror("Ошибка", f'Ошибка: {e}. ')
    else:
        mb.showwarning("Внимание", f'Введите {code} валюты')

window=Tk()
window.title("Курсы обмена валют")
window.geometry("360x300")

Label(text="Базовая валюта").pack(padx=10,pady=10)

b_combobox=ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10,pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label=ttk.Label()
b_label.pack(padx=10,pady=10)

Label(text="Целевая валюта").pack(padx=10,pady=10)

t_combobox=ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10,pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label=ttk.Label()
t_label.pack(padx=10,pady=10)

# entry=Entry()
# entry.pack(padx=10,pady=10)
Button(text="Получить курс обмена", command=exchange).pack(padx=10,pady=10)

window.mainloop()


