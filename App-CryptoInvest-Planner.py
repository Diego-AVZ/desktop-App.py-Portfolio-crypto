import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

tokenA = {
    "name" : "BTC",
    "narrative" : "none",
    "narrative2" : "none",
    "buy" : {
        "bottom" : 10000,
        "top" : 30000
    },
    "sell" : {
        "bottom" : 100000,
        "top" : 300000
    },
    "risk" : "low",
    "pot" : "x5",
    "big" : "yes",
    "stra" : {
        "yon" : "yes",
        "sRisk" : "mid",
        "APY" : "3%",
        "action" : "lend",
        "plat" : "aave",
        "block" : "ethereumOrL2"
    }
}

tokenB = {
    "name" : "ETH",
    "narrative" : "L1",
    "narrative2" : "none",
    "buy" : {
        "bottom" : 800,
        "top" : 1500
    },
    "sell" : {
        "bottom" : 5000,
        "top" : 10000
    },
    "risk" : "low",
    "pot" : "x5",
    "big" : "yes",
    "stra" : {
        "yon" : "yes",
        "sRisk" : "mid",
        "APY" : "3%",
        "action" : "lend",
        "plat" : "aave",
        "block" : "ethereumOrL2"
    }
}

tokenC = {
    "name" : "ADA",
    "narrative" : "L1",
    "narrative2" : "none",
    "buy" : {
        "bottom" : 0.3,
        "top" : 0.75
    },
    "sell" : {
        "bottom" : 2,
        "top" : 5
    },
    "risk" : "low",
    "pot" : "x10",
    "big" : "yes",
    "stra" : {
        "yon" : "yes",
        "sRisk" : "mid",
        "APY" : "3%",
        "action" : "lend",
        "plat" : "aave",
        "block" : "ethereumOrL2"
    }
}

all = [tokenA, tokenB, tokenC]

for i in all: 
    print(i["name"])

inversorType = ""
amountToInvest = 0
goal = 0 
level = ""

def setInvestorTypeCons():
    global inversorType
    inversorType = "cons"
    print("Inversor type selected: ", inversorType)

def setInvestorTypeMod():
    global inversorType
    inversorType = "mod"
    print("Inversor type selected: ", inversorType)

def setInvestorTypeAggr():
    global inversorType
    inversorType = "aggr"
    print("Inversor type selected: ", inversorType)

def getAmountToInvest():
    global amountToInvest
    amountToInvest = input1.get()
    print("amount to invest: ", amountToInvest)

def setGoal1(): # x5
    global goal
    getAmountToInvest()
    goal = int(amountToInvest) * 5
    goal_text.config(text=f"Your Goal: ${goal}")
    i_amount.config(text=f"Initial Amount: ${amountToInvest}")
    print("your Goal is: ", goal)

def setGoal2(): # x10
    global goal
    getAmountToInvest()
    goal = int(amountToInvest) * 10
    goal_text.config(text=f"Your Goal: ${goal}")
    i_amount.config(text=f"Initial Amount: ${amountToInvest}")
    print("your Goal is: ", goal)

def set_novel():
    global level
    level = "novel"

def set_mid():
    global level
    level = "intermediate"

def set_expert():
    global level
    level = "expert"


app = tk.Tk()
app.title("App Portfolio Wizard")
app.geometry("1200x650")

canvas = tk.Canvas(app, width=1200, height=650)
canvas.pack()

bg = Image.open(r"C:\Users\avzfa\Desktop\Code1\Python prac\bg2.png")
bg = bg.resize((1200, 650), Image.LANCZOS)
tk_bg = ImageTk.PhotoImage(bg)

canvas.create_image(0, 0, anchor=tk.NW, image=tk_bg)

cB = ttk.Button(app, text="Conservaive", command=setInvestorTypeCons)
cB.place(x=50, y=50) 

mB = ttk.Button(app, text="Moderate", command=setInvestorTypeMod)
mB.place(x=50, y=100) 

aB = ttk.Button(app, text="Aggresive", command=setInvestorTypeAggr)
aB.place(x=50, y=150) 

but1_style = ttk.Style()

but1_style.configure('TButton',
                     background='#007bff',  # Color de fondo
                     foreground='black',    # Color del texto
                     font=('Arial', 12),     # Tipo de fuente y tamaño
                     padding=(10, 5)         # Relleno (padding)
                     )

cB["style"] = "TButton"
mB["style"] = "TButton"
aB["style"] = "TButton"

text1 = tk.Label(text="Amount to invest?")
text1.place(x=300, y=70)

input1 = tk.Entry(app, width=20)
input1.place(x=300, y=100)

pB1 = tk.Button(app, text="x5", width=3, height=1, background='#849fc8', foreground="white", font=('Arial', 10), cursor='hand2', command=setGoal1)
pB1.place(x=300, y=130)

pB2 = tk.Button(app, text="x10", width=3, height=1, background='#849fc8', foreground="white", font=('Arial', 10), cursor='hand2', command=setGoal2)
pB2.place(x=350, y=130)

i_amount = tk.Label(text="initial amount: ")
i_amount.place(x=300, y=185)

goal_text = tk.Label(text="Your Goal: ")
goal_text.place(x=300, y=210)

nov_but = ttk.Button(text="Novel", command= set_novel)
nov_but.place(x=600, y=30)

mid = ttk.Button(text="Intermediate", command= set_novel)
mid.place(x=600, y=70)

exp = ttk.Button(text="Expert", command= set_expert)
exp.place(x=600, y=1000)


app.mainloop()
