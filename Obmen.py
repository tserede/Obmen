import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    code=entry.get()
    if code:
        try:
            responce=requests.get("http://open.er-api.com/v6/latest/USD")
            responce.raise_for_status()
            data=responce.json()
            if code.lower() in data["rates"]:
                exchange_rates=data["rates"][f"{code}"]
                mb.showinfo("Курс обмена",f"Курс:{exchange_rates}{code} за 1 доллар ")
            else:
                mb.showerror("Ошибка", f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror("Ошибка", f'Ошибка: {e}. ')
    else:
        mb.showwarning("Внимание", f'Введите {code} валюты')

window=Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10,pady=10)

entry=Entry()
entry.pack(padx=10,pady=10)
Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10,pady=10)

window.mainloop()


