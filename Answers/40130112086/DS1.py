def Find_Number(arrayNumbers):
    size=len(arrayNumbers)
    for i in range(size):
        if i not in arrayNumbers:
            return i