import tkinter as tk
from tkinter import*
from tkinter import messagebox

BMI_CALCULATOR = tk.Tk()
BMI_CALCULATOR.title("BMI CALCULATOR")
BMI_CALCULATOR.minsize(400,300)
BMI_CALCULATOR.maxsize(400,300)

def BMI():
    height_data = int(BMI_HEİGHT_AREA.get())
    weight_data = int(BMI_WEİGHT_AREA.get())

    height_data /= 100

    BMI_İNFO = (weight_data)/(height_data*height_data)

    if  height_data < 0:
        msg = Tk()
        msg.withdraw()
        messagebox.showerror("ERROR","PLEASE ENTER THE NORMAL VALUE")
        return 0
    
    if  weight_data < 0:
        msg = Tk()
        msg.withdraw()
        messagebox.showerror("ERROR","PLEASE ENTER THE NORMAL VALUE")
        return 0 

    if BMI_İNFO <=  18.5:
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON","YOUR BMI ="+str(BMI_İNFO)+"\n("+"SEVERELY UNDERWEİGHT."+")")
        return 0 

    if 18.5 < BMI_İNFO < 24.9:
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON","YOUR BMI ="+str(BMI_İNFO)+"\n("+"NORMAL."+")")
        return 0 

    if 25 < BMI_İNFO < 29.9:
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON","YOUR BMI ="+str(BMI_İNFO)+"\n("+"OWERWEİGHT."+")")
        return 0
    
    if 30 < BMI_İNFO < 34.9:
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON","YOUR BMI ="+str(BMI_İNFO)+"\n("+"1. DEGREE OBESITY."+")")
        return 0
    
    if 35 < BMI_İNFO < 39.9:
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON","YOUR BMI ="+str(BMI_İNFO)+"\n("+"2. DEGREE OBESITY."+")")
        return 0
    
    if BMI_İNFO >= 40:
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON","YOUR BMI ="+str(BMI_İNFO)+"\n("+"3. DEGREE OBESITY."+")")
        return 0

BMI_HEİGHT_İNFO = tk.Label(BMI_CALCULATOR,text = "Height\n(cm):",fg = "black",bg = "lime",font = "Arial 23")
BMI_HEİGHT_İNFO.place(width = 100,height = 100,x = 0,y = 0)

BMI_WEİGHT_İNFO = tk.Label(BMI_CALCULATOR,text = "Weight\n(kg):",fg = "black",bg = "salmon",font = "Arial 23")
BMI_WEİGHT_İNFO.place(width = 100,height = 100,x = 0,y = 100)

BMI_HEİGHT_AREA = tk.Entry(BMI_CALCULATOR,fg = "black",bg = "lime",font = "Arial 45")
BMI_HEİGHT_AREA.place(width = 300,height = 100,x = 100,y = 0)

BMI_WEİGHT_AREA = tk.Entry(BMI_CALCULATOR,fg = "black",bg = "salmon",font = "Arial 45")
BMI_WEİGHT_AREA.place(width = 300,height = 100,x = 100,y = 100)

BMI_CALCULATOR = tk.Button(BMI_CALCULATOR,text = "CALCULATE",fg = "lime",bg = "black",activeforeground = "lime",activebackground = "black",font = "Arial 45",command = BMI)
BMI_CALCULATOR.place(width = 400,height = 100,x = 0,y = 200)

BMI_CALCULATOR.mainloop()
