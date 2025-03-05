array= [20, "yangki", 156.99, "python", "EE"]
firstarrylength = len(array)
print(firstarrylength)
array.append(6)
secondarrylength = len(array)
print( firstarrylength - secondarrylength)

programAtCST = ["IT", "EE", "ME", "ECE", "ICE", "ARC", "WRE", "EG", "SWE", "CE"]
arraylength = len(programAtCST)

for index in range(arraylength):
    print(programAtCST[index])
    print(programAtCST[index].lower())

for element in programAtCST:
    print(element)


programAtCST = ["IT", "EE", "ME", "ECE", "ICE", "ARC", "WRE", "EG", "SWE", "CE"]
arraylen= len(programAtCST)
index = 0
while index < arraylen:
    print(programAtCST[index])
    index = index + 1 
   