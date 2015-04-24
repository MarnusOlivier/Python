# The takes a list of rows from a table and constructs a string 
# that prints equally spaced in the console
def tableprint(table, max_columnWidth = 0, justify = 'L'):
    ''' Check what the max column width in each column should be'''    
    columnWidths = [0 for _ in range(len(zip(*table)))]      
    for colIndex, col in enumerate(zip(*table)):
        for row in col:
            if len(str(row)) > columnWidths[colIndex]:
                columnWidths[colIndex] = len(str(row))

    '''Construct the output string a limits the column width if 
       max_columnWidth is specified'''
    outputStr = ''
    for row in table:
        rowList = []
        for colIndex, col in enumerate(row):
            if max_columnWidth != 0:
                if columnWidths[colIndex] > max_columnWidth:
                    columnWidths[colIndex] = max_columnWidth        
            if justify == 'R': # justify right
                rowList.append(str(col)[:columnWidths[colIndex]].rjust(columnWidths[colIndex]))
            elif justify == 'L': # justify left
                rowList.append(str(col)[:columnWidths[colIndex]].ljust(columnWidths[colIndex]))
            elif justify == 'C': # justify center
                rowList.append(str(col)[:columnWidths[colIndex]].center(columnWidths[colIndex]))
        outputStr += ' | '.join(rowList) + '\n'
    
    return outputStr



