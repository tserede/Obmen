from idlelib.editor import keynames

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
}
def update_c_label(event):
    code=combobox.get()
    name=cur[code]
    c_label.config(text=name)

def exchange():
    code=combobox.get()
    if code:
        try:
            responce=requests.get("http://open.er-api.com/v6/latest/USD")
            responce.raise_for_status()
            data=responce.json()
            if code in data["rates"]:
                exchange_rates=data["rates"][code]
                c_name=cur[code]
                mb.showinfo("Курс обмена",f"Курс:{exchange_rates:.2f} {c_name} за 1 доллар ")
            else:
                mb.showerror("Ошибка", f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror("Ошибка", f'Ошибка: {e}. ')
    else:
        mb.showwarning("Внимание", f'Введите {code} валюты')

window=Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Выберите код валюты").pack(padx=10,pady=10)

combobox=ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10,pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label=ttk.Label()
c_label.pack(padx=10,pady=10)

# entry=Entry()
# entry.pack(padx=10,pady=10)
Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10,pady=10)

window.mainloop()


