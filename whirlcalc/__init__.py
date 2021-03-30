import os
import math
import pathlib

def make_penguin():
    import tkinter
    window = tkinter.Tk()
    window.geometry("1600x1200")
    canvas = tkinter.Canvas(window, width = 1600, height = 1200)      
    canvas.pack()      
    img = tkinter.PhotoImage(file="penguin.png")
    canvas.create_image(20,20, anchor=tkinter.NW, image=img)   
    txt = tkinter.Label(window, text="Look at these penguin.. and now.. you are also cute! Go use my module!", font=[("Segoe"),(15)])
    txt.place(x = 0,y =0)
    window.mainloop()
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def evaluate(command):
        if command.lower() == "cls" or command.lower() == "clear":
            os.system("cls")
        else:
            if "factorial(" in command:
                com = command.lower()
                fac_num_st = com.find("factorial(") + len("factorial(")
                fac_num_ed = com.find(")")
                fac_cmd_st = com.find("factorial(")
                fac_cmd_ed = com.find(")")
                fac_cmd = com[fac_cmd_st:fac_cmd_ed]
                fac_num = com[fac_num_st:fac_num_ed]        
                fac = factorial(int(fac_num))
                command.replace(fac_cmd,str(fac))
            if "fac(" in command:
                com = command.lower()
                fac_num_st = com.find("fac(") + len("fac(")
                fac_num_ed = com.find(")")
                fac_cmd_st = com.find("fac(")
                fac_cmd_ed = com.find(")")
                fac_cmd = com[fac_cmd_st:fac_cmd_ed]
                fac_num = com[fac_num_st:fac_num_ed]        
                fac = factorial(int(fac_num))
                command.replace(fac_cmd,str(fac))
            if "pi" in command.lower():
                command  = command.replace("pi", str(3.141592653589793))
            
            return eval(command)

#python setup.py sdist
#python setup.py bdist_wheel --universal
#python -m twine upload dist/

__version__ = "0.1"
__author__ = 'Whirlpool-Programmer'
__credits__ = 'Whirlpool-Programmer'
