# Made by : Nanotixx
# Base 2 (Binary) to Base 10 ()

def convert(binaryList):
    exponentPosition = -1
    binarySum = 0
    binaryList.reverse() # Starts counting from the left
    
    for num in binaryList:
        exponentPosition += 1
        if num == 1:
            result = (num * 2) ** exponentPosition
            binarySum += result
        else:
            continue
    print("Binary to Decimal : " + str(binarySum))
        
example = [1, 1, 0, 1] # <--- Input the numbers and put , after every digit
convert(example)