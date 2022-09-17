


constant = True
OPS = ["+", "-", "*", "/", "^"]
counter = 0
while constant == True:


    equation = input("")
    equation.strip()
    
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



    
    

    if unpacked[0] in OPS:
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
    
    
