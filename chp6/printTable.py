#!python
#print a table of strings that are right justified. table entries must be all aligned

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#TODO Adjust for each column to have individual max column width
def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        for k in range(len(table[i])):
            if colWidths[i] < len(table[i][k]):
                colWidths[i] = len(table[i][k])

    for i in range(len(table)):
        for k in range(len(table[i])):
            table[i][k] = table[i][k].rjust(colWidths[i]+1)

    line = ''
    for i in range(len(table[i])):
        for k in range(len(table)):
            line = line + table[k][i]
        line = line + '\n'

    print(line)

printTable(tableData)


