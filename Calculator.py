from cmath import sin
import matplotlib.pyplot as plt
import numpy as np


constant = True
OPS = ["+", "-", "*", "/", "^"]
counter = 0
gcounter = 0
while constant == True:


    equation = input("").lower()
    equation = ''.join(equation.split())
    
    
    def calculate():
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return  num1 - num2
        elif operator == "*":
            return  num1 * num2
        elif operator == "/":
            return  num1 / num2
        elif operator == "^":
            return num1 ** num2 

    unpacked = ([*equation])
    check = any(item in OPS for item in unpacked)


    def transformations():
        vertShift = input("What is the vertical shift")
        vertStretch = input("what is the vertical stretch")
        HorShift = input("What is the horizontal shift")
        HorStretch = input("What is the horizontal stretch ")
        transformations = [vertShift, vertStretch, HorShift, HorStretch]
        return transformations


    def graph():
        x = np.linspace(-5,5,100)
        y = vertStretch * (HorShift * x**power) + vertShift
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,y, 'r')
        plt.show()


    def finder():
        x = 0
        for  i in range(len(area)):
            x = x + 1
            if unpacked[start+ x] in OPS:
                operator = unpacked[start + x]
                num1 = float(''.join(unpacked[start: unpacked.index(operator)]))
                num2 = float(''.join(unpacked[unpacked.index(operator) +1 : end]))
                stuff = [num1, operator, num2]
                return stuff



    if unpacked[0] == "g":
        print("GRAPHING MODE")
        gcounter = gcounter + 1
        while gcounter == 1:
            print("(1):Linear, (2):Quadratic, (3):Cubic, (4): Sin")
            type = int(input("what type of function would you like to graph"))
            
            if type <= 3:
                power = type
                transforms = transformations()
                vertShift = int(transforms[0])
                vertStretch = int(transforms[1])
                HorShift = int(transforms[2])
                HorStretch = int(transforms[3])
                graph()

            
            
            if type == "n":
                gcounter = gcounter - 1
                print("Normal mode")

    



    elif unpacked[0] in OPS:
            num1 = previous
            operator = unpacked[0]
            num2 = float(''.join(unpacked[1: len(unpacked)]))
            final = calculate()
            print(final)
            previous = final



    elif "(" in unpacked or ")" in unpacked:
        start = int(unpacked.index("(")) + 1
        end = int(unpacked.index(")"))
        area = unpacked[start:end]
        product = finder()
        num1 = product[0]
        operator = product[1]
        num2 = product[2]
        Inside_answer = calculate()

        num2 = float(''.join(unpacked[(end + 2):]))
        num1 = Inside_answer
        operator = str(unpacked[end + 1])
        Final = calculate()
        previous = Final
        
        print(Final)
    
    
    elif check:
        start = 0
        end = len(unpacked)
        area = unpacked
        product = finder()
        num1 = product[0]
        operator = product[1]
        num2 = product[2]
        
        final = calculate()
        print(final)
        previous = final
    
    
