import random
from tkinter import *


# ================= Roll the dice ==============================
def roll(d, n, m):
    if n != 0:
        str1 = f"{n} d{d}'s.\n"
        total = 0
        log = ""
        for i in range(n):
            roll = random.randint(1, d)
            total += roll + m
            if m > 0:
                log += f"{roll}(+{m}) "
            elif m < 0:
                log += f"{roll}({m}) "
            else:
                log += f"{roll} "
        str1 += "Rolls: " + log + "\n"
        return total, str1
    return 0, ""

# four - twenty (type of dice)
# modDice - modifier per dice // modTotal - modifier at the end of the result
def dice_roller(four=0, six=0, eight=0, ten=0, twelve=0, hundred=0, twenty=0, modDice=0, modTotal=0):
    if four < 0 or six < 0 or eight < 0 or ten < 0 or twelve < 0 or hundred < 0 or twenty < 0:
        strEnd = "Invalid number of dice!"
        return strEnd
    else:
        result = 0
        stringResult = "\nRolling...\n"
        dice = [4, 6, 8, 10, 12, 100, 20]
        nDice = [four, six, eight, ten, twelve, hundred, twenty]
        for i in range(7):
            rolled = roll(dice[i], nDice[i], modDice)
            result += rolled[0]
            stringResult += rolled[1]
        if modTotal > 0:
            result += modTotal
            stringResult += f"Modifier: +{modTotal}\n"
        elif modTotal < 0:
            result += modTotal
            stringResult += f"Modifier: {modTotal}"
        stringResult += f"Total: {result}."
        return stringResult


# ================= Interface ===================================
# main
window = Tk()
window.title("Dice Roller v1.0")

# functions
def clickRoll():
    four = int(nFour.get())  # returns the value in the text box
    six = int(nSix.get())
    eight = int(nEight.get())
    ten = int(nTen.get())
    twelve = int(nTwelve.get())
    hundred = int(nHundred.get())
    twenty = int(nTwenty.get())
    dMod = int(modDie.get())
    tMod = int(modTotal.get())
    output.configure(state="normal")
    output.insert(END, dice_roller(four, six, eight, ten,
                                   twelve, hundred, twenty, dMod, tMod))
    output.configure(state="disabled")


def clickClear():
    nFour.delete(0, END)
    nFour.insert(0, 0)
    nSix.delete(0, END)
    nSix.insert(0, 0)
    nEight.delete(0, END)
    nEight.insert(0, 0)
    nTen.delete(0, END)
    nTen.insert(0, 0)
    nTwelve.delete(0, END)
    nTwelve.insert(0, 0)
    nHundred.delete(0, END)
    nHundred.insert(0, 0)
    nTwenty.delete(0, END)
    nTwenty.insert(0, 0)
    modDie.delete(0, END)
    modDie.insert(0, 0)
    modTotal.delete(0, END)
    modTotal.insert(0, 0)
    output.configure(state="normal")
    output.delete(0.0, END)
    output.configure(state="disabled")


# text labels
Label(window, text="D4", width=5).grid(row=1, column=0, sticky=W)
Label(window, text="D6", width=5).grid(row=2, column=0, sticky=W)
Label(window, text="D8", width=5).grid(row=3, column=0, sticky=W)
Label(window, text="D10", width=5).grid(row=4, column=0, sticky=W)
Label(window, text="D12", width=5).grid(row=5, column=0, sticky=W)
Label(window, text="D100", width=5).grid(row=6, column=0, sticky=W)
Label(window, text="D20", width=5).grid(row=7, column=0, sticky=W)

Label(window, text="Number").grid(row=0, column=1)
Label(window, text="Dice Mod").grid(row=0, column=2)
Label(window, text="Result").grid(row=0, column=3, columnspan=2)

# input
# d4
nFour = Entry(window, width=10)
nFour.grid(row=1, column=1, sticky=W)
nFour.insert(0, 0)

# d6
nSix = Entry(window, width=10)
nSix.grid(row=2, column=1, sticky=W)
nSix.insert(0, 0)

# d8
nEight = Entry(window, width=10)
nEight.grid(row=3, column=1, sticky=W)
nEight.insert(0, 0)

# d10
nTen = Entry(window, width=10)
nTen.grid(row=4, column=1, sticky=W)
nTen.insert(0, 0)

# d12
nTwelve = Entry(window, width=10)
nTwelve.grid(row=5, column=1, sticky=W)
nTwelve.insert(0, 0)

# d100
nHundred = Entry(window, width=10)
nHundred.grid(row=6, column=1, sticky=W)
nHundred.insert(0, 0)

# d20
nTwenty = Entry(window, width=10)
nTwenty.grid(row=7, column=1, sticky=W)
nTwenty.insert(0, 0)

# mod
Label(window, text="Per Die").grid(row=2, column=2, padx=10)
modDie = Entry(window, width=10)
modDie.insert(0, 0)
modDie.grid(row=3, column=2, sticky=W, padx=10)

Label(window, text="Total").grid(row=5, column=2, padx=10)
modTotal = Entry(window, width=10)
modTotal.insert(0, 0)
modTotal.grid(row=6, column=2, sticky=W, padx=10)

# roll button
Button(window, text="Roll", command=clickRoll).grid(row=7, column=3)
Button(window, text="Clear", command=clickClear).grid(row=7, column=4)

# output
output = Text(window, wrap=WORD, width=20)
output.grid(row=1, column=3, rowspan=6, columnspan=2, sticky=W)
output.insert(END, "Select your Dice!\n")
output.configure(state="disabled")

# run the main loop
window.mainloop()


# = TEST ========================================================
# print(dice_roller(six=1,eight=2))
