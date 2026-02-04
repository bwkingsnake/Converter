from tkinter import *
from tkinter import ttk

class converter:
    def __init__(self, number, base):

        number = number.upper()
        self.hexdecimals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

        if base == "Hexadecimal":
            self.converted = self.hexToDecimal(number)
          
        elif base == "Binary":
            self.converted = self.binaryToDecimal(number)
        else:
            self.converted = number
     
    ###################Utility-Functions####################

    def reverseString(self, s):
        i = len(s)-1
        reversedString = ""
        while i >= 0:
            reversedString = reversedString + s[i]
            i = i -1 
        return reversedString
    
    ###################Helper-Functions####################

    def binaryToDecimal(self, number):
        reversedNumber = self.reverseString(number)
        power = 1
        converted = 0
        for c in reversedNumber:
            if c == "1":
                converted = converted + power
            power = power * 2
        return converted
    
    def hexToDecimal(self, number):
        reversedNumber = self.reverseString(number)
        base = 16
        power = 0
        converted = 0
        for c in reversedNumber:
            for i, h in enumerate(self.hexdecimals):
                if c == h:
                    converted = converted + (i * base ** power)
            power = power + 1
        return converted
    
    ###################Conversion-Functions####################

    def toBinary(self):
        number = int(self.converted)
        converted = ""
        while True:
            r = (number % 2)
            number = (number//2)
            if r == 0:
                converted = converted + "0"
            elif r == 1:
                converted = converted + "1"
            if number == 0:
                break
        return self.reverseString(converted)
    
    def toHex(self):
        buffer = []
        q = int(self.converted)
        while True:
            r = (q % 16)
            buffer.append(r)
            q = (q // 16) 
            if q == 0:
                break
        buffer.reverse()
        converted = ""
        for num in buffer:
            for i,  h in enumerate(self.hexdecimals):
                if num == i:
                    converted = converted + h
        return converted
    
    def toDecimal(self):
        return self.converted
            
class myApp:
    def __init__(self, root):
        #INIT
        root.title("converter")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        #row1
        fromLabel = ttk.Label(mainframe, text="From",)
        fromLabel.grid(column=0,row=0, sticky=(W))

        toLabel = ttk.Label(mainframe, text="To")
        toLabel.grid(column=1,row=0, sticky=(W))

        #row2

        bases = ('Decimal', 'Hexadecimal', 'Binary')
        defaultValue = "Decimal"

        self.fromBase = StringVar()
        fromComoBox = ttk.Combobox(mainframe, textvariable=self.fromBase,state="readonly")
        fromComoBox.set(defaultValue)
        fromComoBox['values'] = bases
        fromComoBox.grid(column=0,row=1)
        fromComoBox.bind("<<ComboboxSelected>>", self.updateEntryText)

        self.toBase = StringVar()
        toComoBox = ttk.Combobox(mainframe, textvariable=self.toBase,state="readonly")
        toComoBox.set(defaultValue)
        toComoBox['values'] = bases
        toComoBox.grid(column=1,row=1)

        self.entryLabelVar = StringVar()
        self.entryLabelVar.set(f"Enter {defaultValue} Number")
        entryLabel = ttk.Label(mainframe, textvariable=self.entryLabelVar)
        entryLabel.grid(column=0,row=2, sticky=(W))

        #row3

        self.entryVar = StringVar()
        self.Entry = ttk.Entry(mainframe, textvariable=self.entryVar)
        self.Entry.grid(row=3, column=0, columnspan=3, sticky=(N, W, E, S))

        #row4

        ConvertButton = ttk.Button(mainframe, text="Convert", command=self.convert)
        ConvertButton.grid(column=0, row=4, sticky=W)

        clearButton = ttk.Button(mainframe, text="Clear", command=self.clear)
        clearButton.grid(column=0, row=4, sticky=E)

        self.text = Text(mainframe, width=40, height=10)
        self.text.grid(row=5, columnspan=3)


        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def updateEntryText(self, *args):
        self.entryLabelVar.set(f"Enter {self.fromBase.get()} Number")
    
    ###Validations

    def checkDecimal(self, userInput):
        validCharacters = ["0","1","2","3","4","5","6","7","8","9"]
        valid = False
        for c in userInput:
            if c not in validCharacters:
                return False
            elif c in validCharacters:
                valid = True
        return valid

    def checkBinary(self, userInput):
        validCharacters = ["0","1"]
        valid = False
        for c in userInput:
            if c not in validCharacters:
                return False
            elif c in validCharacters:
                valid = True
        return valid
       

    def checkHexadecimal(self, userInput):
        validCharacters = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        valid = False
        for c in userInput:
            if c not in validCharacters:
                return False
            elif c in validCharacters:
                valid = True
        return valid
    
    def isValid(self, userInput):
        validBase = False
        if self.fromBase.get() == "Decimal":
            validBase = self.checkDecimal(userInput)
        elif self.fromBase.get() == "Binary":
            validBase = self.checkBinary(userInput)
        else:
            validBase = self.checkHexadecimal(userInput)
        return validBase

    def convert(self, *args):
        userInput = self.entryVar.get().upper()
        validBase = self.isValid(userInput)
        self.converter = converter(userInput, self.fromBase.get())

        self.text.delete("1.0", "end-1c")

        if validBase == True:
            if self.toBase.get() == "Decimal":
                self.text.insert("1.0", (self.converter.toDecimal()))
            elif self.toBase.get() == "Binary":
                self.text.insert("1.0", (self.converter.toBinary()))
            elif self.toBase.get() == "Hexadecimal":
                    self.text.insert("1.0", (self.converter.toHex()))
        else:
            print("Base Does Not Match User Input")
        
    def clear(self,*args):
        self.Entry.delete(0, END)
        self.text.delete("1.0", "end-1c")

def main():
    root = Tk()
    app = myApp(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
