from tkinter import *
from tkinter import messagebox
import math as mt

p=1.23 # ПЛОТНОСТЬ ВОЗДУХА В ТРОПОСФЕРЕ НА УРОВНЕ МОРЯ

def ForceGauge():
    global p
    G=float(weight_la.get())
    S=float(wing_area.get())
    Cx=float(coeff_resist.get())
    res = mt.sqrt(2*G/Cx*p*S)
        
    h_p = res / 75
    Wt = h_p * 735.5
    r_Wt = round(Wt / 1000, 2)
    messagebox.showinfo('Результат', f'''Потребная тяга силовой установки: {round(res)} kg/sec

ИЗМЕНЕНИЕ ОТ ПОТРЕБНОЙ ТЯГИ СИЛОВОЙ УСТАНОВКИ ПРИ ЗАДАННОМ (Cx): {h_p} h/p

ИЗМЕНЕНИЕ ОТ ПОТРЕБНОЙ ТЯГИ СИЛОВОЙ УСТАНОВКИ ПРИ ЗАДАННОМ (Cx): {Wt} Wt

ИЗМЕНЕНИЕ ОТ ПОТРЕБНОЙ ТЯГИ СИЛОВОЙ УСТАНОВКИ ПРИ ЗАДАННОМ (Cx): {r_Wt} kWt''')
    
class Window:
    def __init__(self, width, height, title="АЭРОДИНАМИЧЕСКИЕ ХАРАКТЕРИСТИКИ БЛА", resizable=(False, False), icon=None):
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
    window = Window(500, 300)
    
    frame = Frame(padx=10, pady=10)
    frame.pack(expand=True)

    weight_la = Label(frame,text="УКАЖИТЕ ВЕС Л/А(gramm): ")
    weight_la.place(x = 127, y = 13, anchor = 'w')

    wing_area = Label(frame,text="УКАЖИТЕ ПЛОЩАДЬ КРЫЛА Л/А(dm2): ")
    wing_area.place(x = 60, y = 43, anchor = 'w')

    coeff_resist = Label(frame,text="УКАЖИТЕ КОЭФФИЦИЕНТ СОПРОТИВЛЕНИЯ (Cx): ")
    coeff_resist.grid(row=3, column=0)

    weight_la = Entry(frame, width=30)
    weight_la.grid(row=1, column=1, pady=5)
        
    wing_area = Entry(frame, width=30)
    wing_area.grid(row=2, column=1, pady=5)
        
    coeff_resist = Entry(frame, width=30)
    coeff_resist.grid(row=3, column=1, pady=5)
        

    cal_btn = Button(frame, text='Потребная тяга,\n(kg/sec)', command=ForceGauge)
    cal_btn.grid(row=5, column=1)
    
    window.run()


