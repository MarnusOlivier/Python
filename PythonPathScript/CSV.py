from csv import reader, writer

def imp(file_path, header_row_index):
    file_handle = open(file_path)
    csv_reader  = reader(file_handle)   
    baselist = []
    count = 0    
    for row in csv_reader:
        if count == header_row_index:
            headerlist = row
        else:
            baselist.append(row)
        count = count + 1
    return headerlist, baselist
    
def exprt(file_path, headerlist, row_data):
    data = row_data
    data.insert(0, headerlist)
    with open(file_path,'wb') as f:
        write = writer(f)
        write.writerows(data)
