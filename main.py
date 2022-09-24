import tkinter
from tkinter import *
from tkinter import messagebox
import random


root = Tk()
root.title("Alarm")

ticker, parameter, current_price, alarm_price = '', '', '', ''
after_id1, after_id2 = '', ''


#Getting the value of current price, for example, a random value.

def get_current_price(ticker):

    if ticker == 'BTC':
        return str(random.randint(20000, 22000))
    elif ticker == 'ETH':
        return str(random.randint(1300, 1500))
    elif ticker == 'ETC':
        return str(random.randint(30, 40))


#Comapare current price with alarm price

def price_compare(parameter, current_price, alarm_price):

    result = False
    if parameter == '>':
        if current_price > alarm_price:
            result = True
    else:
        if current_price < alarm_price:
            result = True
    return result


#Updating the current price

def update_current_price():

    global current_price, after_id1
    after_id1 = root.after(1000, update_current_price)

    ticker = ticker_variable.get()
    current_price = get_current_price(ticker)
    label_current_price.configure(text=current_price)


#Activate the price monitoring

def start():

    global ticker, parameter, alarm_price, after_id2
    ticker = ticker_variable.get()
    parameter = parameter_variable.get()
    alarm_price = price_input.get()
    result = price_compare(parameter, current_price, alarm_price)

    if result == True:
        show_message()
    after_id2 = root.after(500, start)

    btn_start.grid_forget()
    btn_stop.grid(row=4, columnspan=2, sticky='ew')


#Stop the price monitoring

def stop():

    root.after_cancel(after_id2)
    btn_stop.grid_forget()
    btn_start.grid(row=4, columnspan=2, sticky='ew')


#Функция вывода уведомления

def show_message():

    message = messagebox.showwarning('Внимание!', f'{ticker} достиг цены {alarm_price}')


#GUI

#Ticker selection

ticker_variable = tkinter.StringVar()
tickers_list = ['BTC', 'ETH', 'ETC']

label_ticker_text = Label(root, height=1, font=("Arial",30), bg='#116466', text='Тикер:', anchor='center', relief=GROOVE)
label_ticker_text.grid(row=0, column=0, sticky='ew')

ticker_menu = OptionMenu(root, ticker_variable, *tickers_list)
ticker_menu.config(font=("Arial",25), justify='center', relief=GROOVE)
ticker_menu.grid(row=0, column=1, sticky='ew')


#Parameter selection

parameter_variable = tkinter.StringVar(root)
parameters_list = ['<', '>']

label_parameter_text = Label(root, height=1, font=("Arial",30), bg='#D9B08C', text='Параметр:', justify='left', relief=GROOVE)
label_parameter_text.grid(row=1, column=0, sticky='ew')

parameters_menu = OptionMenu(root, parameter_variable, *parameters_list)
parameters_menu.config(font=("Arial",25), justify='center', relief=GROOVE)
parameters_menu.grid(row=1, column=1, sticky='ew')

label_current_price_text = Label(root, height=1, font=("Arial",30), bg='#FFCB9A', text='Текущая цена:', justify='left', relief=GROOVE)
label_current_price_text.grid(row=2, column=0, sticky='ew')

label_current_price = Label(root, height=1, font=("Arial",30), bg='white', text='0', textvariable=current_price, relief=GROOVE)
label_current_price.grid(pady=2,row=2, column=1, sticky='ew')


#Alarm price input

price_input_text = Label(root, height=1, font=("Arial",30), bg='#D1E8E2', text='Целевая цена:', justify='left', relief=GROOVE)
price_input_text.grid(row=3, column=0, sticky='ew')

price_input = Entry(root, font=("Arial", 30), textvariable=alarm_price, justify='center', relief=GROOVE)
price_input.grid(pady=3,row=3, column=1, sticky='ew')


#Start-Stop buttons

btn_start = Button(root, text='Старт', font=("Arial", 40), bg='#AFD275', command=start)
btn_start.grid(row=4, column=0, columnspan=2, sticky='ew')

btn_stop = Button(root, text='Стоп', font=("Arial", 40), bg='#E7717D', command=stop)


def main():

    update_current_price()
    root.mainloop()

if __name__ == '__main__':

    main()





