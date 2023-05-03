from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

res=[0]
result = []
total = 0
def select_1():
    global total
    if q_1.get() == answers[0]:
        total += 5
    elif q_1.get() == answers[0]:
        total += 0
    elif q_1.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_1.get())
    
def select_2():
    global total
    if q_2.get() == answers[1]:
        total += 5
    elif q_2.get() == answers[1]:
        total += 0
    elif q_2.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_2.get())
    
def select_3():
    global total
    if q_3.get() == answers[2]:
        total += 5
    elif q_3.get() == answers[2]:
        total += 0
    elif q_3.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_3.get())
        
def select_4():
    global total
    if q_4.get() == answers[3]:
        total += 5
    elif q_4.get() == answers[3]:
        total += 0
    elif q_4.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_4.get())
    
def select_5():
    global total
    if q_5.get() == answers[4]:
        total += 5
    elif q_5.get() == answers[4]:
        total += 0
    elif q_5.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_5.get())
    
def select_6():
    global total
    if q_6.get() == answers[5]:
        total += 5
    elif q_6.get() == answers[5]:
        total += 0
    elif q_6.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_6.get())
    
def select_7():
    global total
    if q_7.get() == answers[6]:
        total += 5
    elif q_7.get() == answers[6]:
        total += 0
    elif q_7.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_7.get())
    
def select_8():
    global total
    if q_8.get() == answers[7]:
        total += 5
    elif q_8.get() == answers[7]:
        total += 0
    elif q_8.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_8.get())
    
def select_9():
    global total
    if q_9.get() == answers[8]:
        total += 5
    elif q_9.get() == answers[8]:
        total += 0
    elif q_9.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_9.get())
    
def select_10():
    global total
    if q_10.get() == answers[9]:
        total += 5
    elif q_10.get() == answers[9]:
        total += 0
    elif q_10.get() == 'Не знаю':
        total -= 5
    res.append(total)
    result.append(q_10.get())
    
def select_all():
    global total
    txt = name.get()
    messagebox.showinfo('Результат', f'''Поздравляю,{txt}! Ваш результат {total} баллов!\n
Ваши ответы: {result}\n
Правильные ответы: {answers}\n''')

def graph():
    global res
    quest = [int(i) for i in range(len(res))]
    plt.plot(quest, res)
    plt.title('Результаты опроса')
    plt.xlabel('Номер вопроса')
    plt.ylabel('Оценка')
    plt.grid()

    plt.scatter(quest, res)

    z = np.polyfit(quest, res, 2)
    p = np.poly1d(z)
    plt.plot(quest, p(quest))
    
    plt.show()
    

class Window:
    def __init__(self, width, height, title="Тест", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)            
        photo = PhotoImage(file="airplane-fill.png")
        self.root.iconphoto(False,photo)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(800, 500)

    name = Label(text="УКАЖИТЕ ВАШЕ ИМЯ: ")
    name.grid(row=0, column=4, padx=5, pady=5)

    name = Entry(width=30)
    name.grid(row=1, column=4, padx=5, pady=5)

    questions = ['В 2014 году Аральское море полностью высохло', 'На самом деле Наполеон Бонапарт был ростом около 180 сантиметров', 'Политика самоизоляции началась в Японии в эпоху Эдо', 'К началу Первой мировой войны в Африке не было ни одного независимого государства', 'В 60–80-х годах курс доллара составлял меньше одного рубля', 'В 1935 году Нобелевской премией мира был награжден человек из Третьего рейха', 'Первым программистом в истории считается женщина', 'Рибосомы – это органеллы клетки, в которых образуется энергия, необходимая для существования организма', 'Российский город Дербент древнее египетского Каира', 'Период творчества Пабло Пикассо в Барселоне называется «розовым»']
    answers = ['Нет','Нет','Да', 'Нет','Да','Да', 'Да','Нет','Да', 'Нет']
    ln = max(list(map(lambda x: len(x), questions)))
    
    q_1 = StringVar()    
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=3, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[0], width=ln+3)
    label.grid(row=3, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_1, command=select_1)
    yes_btn.grid(row=3, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_1, command=select_1)
    no_btn.grid(row=3, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_1, command=select_1)
    unknown_btn.grid(row=3, column=5)
       
    q_2 = StringVar()
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=4, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[1], width=ln+3)
    label.grid(row=4, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_2, command=select_2)
    yes_btn.grid(row=4, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_2, command=select_2)
    no_btn.grid(row=4, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_2, command=select_2)
    unknown_btn.grid(row=4, column=5)

    q_3 = StringVar()
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=5, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[2], width=ln+3)
    label.grid(row=5, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_3, command=select_3)
    yes_btn.grid(row=5, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_3, command=select_3)
    no_btn.grid(row=5, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_3, command=select_3)
    unknown_btn.grid(row=5, column=5)

    q_4 = StringVar()
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=6, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[3], width=ln+3)
    label.grid(row=6, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_4, command=select_4)
    yes_btn.grid(row=6, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_4, command=select_4)
    no_btn.grid(row=6, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_4, command=select_4)
    unknown_btn.grid(row=6, column=5)

    q_5 = StringVar()
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=7, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[4], width=ln+3)
    label.grid(row=7, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_5, command=select_5)
    yes_btn.grid(row=7, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_5, command=select_5)
    no_btn.grid(row=7, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_5, command=select_5)
    unknown_btn.grid(row=7, column=5)

    q_6 = StringVar()
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=8, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[5], width=ln+3)
    label.grid(row=8, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_6, command=select_6)
    yes_btn.grid(row=8, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_6, command=select_6)
    no_btn.grid(row=8, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_6, command=select_6)
    unknown_btn.grid(row=8, column=5)

    q_7 = StringVar()
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=9, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[6], width=ln+3)
    label.grid(row=9, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_7, command=select_7)
    yes_btn.grid(row=9, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_7, command=select_7)
    no_btn.grid(row=9, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_7, command=select_7)
    unknown_btn.grid(row=9, column=5)

    q_8 = StringVar()
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=10, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[7], width=ln+3)
    label.grid(row=10, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_8, command=select_8)
    yes_btn.grid(row=10, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_8, command=select_8)
    no_btn.grid(row=10, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_8, command=select_8)
    unknown_btn.grid(row=10, column=5)


    q_9 = StringVar()
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=11, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[8], width=ln+3)
    label.grid(row=11, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_9, command=select_9)
    yes_btn.grid(row=11, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_9, command=select_9)
    no_btn.grid(row=11, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_9, command=select_9)
    unknown_btn.grid(row=11, column=5)


    q_10 = StringVar()
    position = {"padx":6, "pady":1, "anchor":NW}
    
    frame = Frame(borderwidth=1, relief=SOLID)
    frame.grid(row=12, column=1, columnspan = 8, rowspan = 1, padx=5, pady=5)
        
    label = ttk.Label(frame, text=questions[9], width=ln+3)
    label.grid(row=12, column=2)
        
    yes_btn = ttk.Radiobutton(frame, text='Да', value='Да', variable=q_10, command=select_10)
    yes_btn.grid(row=12, column=3)
          
    no_btn = ttk.Radiobutton(frame, text='Нет', value='Нет', variable=q_10, command=select_10)
    no_btn.grid(row=12, column=4)
         
    unknown_btn = ttk.Radiobutton(frame, text='Не знаю', value='Не знаю', variable=q_10, command=select_10)
    unknown_btn.grid(row=12, column=5)

    cal_btn = Button(text='Результат', command=select_all, background='red')
    cal_btn.grid(row=13, column=4)

    cal_btn = Button(text='График', command=graph, background='black', foreground='white')
    cal_btn.grid(row=14, column=4)
    

    window.run()
    

