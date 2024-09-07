import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from  tkinter import ttk


def exchange():
    code=combobox.get()
    if code:
        try:
            responce=requests.get("http://open.er-api.com/v6/latest/USD")
            responce.raise_for_status()
            data=responce.json()
            if code in data["rates"]:
                exchange_rates=data["rates"][code]
                mb.showinfo("Курс обмена",f"Курс:{exchange_rates:.2f} {code} за 1 доллар ")
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
cur=["RUB","EUR","GBP","JPY","CNY","KZT","UZS","AED","CHF","CAD"]
combobox=ttk.Combobox(values=cur)
combobox.pack(padx=10,pady=10)

# entry=Entry()
# entry.pack(padx=10,pady=10)
Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10,pady=10)

window.mainloop()


