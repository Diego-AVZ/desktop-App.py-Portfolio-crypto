import tkinter as tk

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

all = [tokenA]

print(all[0]["name"])

inversorType = ""

def setInvestortypeCons():
    global inversorType
    inversorType = "cons"
    print("Inversor type selected: " + inversorType)

ventana = tk.Tk()

boton = tk.Button(ventana, text="set cons", command=setInvestortypeCons)

boton.pack(pady=10)

ventana.mainloop()
