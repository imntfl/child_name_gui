from bs4 import BeautifulSoup
import requests as req
import random
import tkinter as tk


url = 'https://my-calend.ru/names/russian'
page = req.get(url)
soup = BeautifulSoup(page.text, 'lxml')
z = []

for x in soup.find_all('a', href=True):
    y = x.get_text()
    z.append(y)

m = random.choice(z[113:168])
w = random.choice(z[57:112])

class App(tk.Tk):
    def __init__(a):
        super().__init__()
        a.btn = tk.Button(a, text="Узнать имена",fg="white",bg="#34A2FE",width=40,height=4, command=clicked)
        a.btn.pack(padx=22, pady=22)
        a.text_box = tk.Text()
        a.text_box.pack()

def clicked():
    a.btn.configure(text='Использовано')
    a.text_box.insert(tk.END,'\n'+m+'\n\n'+w+'\n\n\n\n\n\n\n\n\n\n\n\n')

if __name__ == "__main__":
    a = App()
    a.title('Программа:  Имена ваших детей v1.0')
    a.geometry("400x250")

a.mainloop()
























