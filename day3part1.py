## Advent of Code 2018 Day 3

## imports
import os
import difflib
import re

## parameters
fname = 'input.txt'
strArray = []

coordinates = {}
for i in range(0,2000):
    for j in range(0,2000):
        coordinates[(i,j)] = "..."

print(coordinates[(0,0)])
## get input
for line in open(fname, 'r'):
    if line.strip():           # line contains eol character(s)
        line = re.sub('[@#:\n'']', '', line)
        strArray.append(line)

index = 0
for index in range(0,len(strArray)):
    newValue = [i for i in strArray[index].split(" ")]
    strArray[index] = newValue
    strArray[index].remove('')
    strArray[index][0] = int(strArray[index][0])
    strArray[index][1] = [int(i) for i in strArray[index][1].split(",")]
    strArray[index][2] = [int(i) for i in strArray[index][2].split("x")]
    index += 1

print(strArray[0:5])

for index in range(0,len(strArray)):
    value = hex(strArray[index][0])
    startX = strArray[index][1][0]
    startY = strArray[index][1][1]
    sizeX = strArray[index][2][0]
    sizeY = strArray[index][2][1]

    for i in range (0, sizeX):
        for j in range (0, sizeY):
            if (coordinates[(i+startX,j+startY)] != "..."):
                coordinates[(i+startX,j+startY)] = "ZZZ"
            else:
                coordinates[(i+startX,j+startY)] = value

count = 0
for i in range(0,2000):
    for j in range(0,2000):
        if(coordinates[(i,j)] == "ZZZ"):
            count += 1

print (count)


        #
        #
        # index1 = 0
        # index2 = 0
        # diffArray = []
        # for index1 in range(0,len(strArray)):
        #     string1 = strArray[index1]
        #     for index2 in range(0,len(strArray)):
        #         string2 = strArray[index2]
        #         if string1 == string2:
        #             continue
        #         else:
        #             diffArray.append([enumerate(difflib.ndiff(string1, string2)),index1, index2,0])
        #
        # for element in diffArray:
        #     for i,j in element[0]:
        #         if j[0]==' ': continue
        #         elif j[0]=='-':
        #             element[3] += 1
        #         elif j[0]=='+':
        #             element[3] += 1
        #
        # candidateArray = []
        # ## create candidate array
        # for element in diffArray:
        #     if element[3] <3:
        #         candidateArray.append(element)
        #
        # print (candidateArray)
        # print (strArray[135])
        # print (strArray[227])

## nnfqdsvwryteogambzuchiwkpx ##31
## wnfqzsvwjyteogambduchirkpx ##116

## lnfqdsvwpyteogabbhuchirkpx ##30
## lnfqdsvwjyteogambzucczrgpx ##115
