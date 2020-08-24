# PROGRAM TO SORT AN EXCEL/CSV FILE (You can use any database file format) BY GIVEN COLUMN, KEY and AXIS

def sort_File(file_name, by = None, axis = 0, key = None, reverse = False):
    """
        A function to sort an Excel/CSV file.
        
        INPUTS : Takes in the file name, column name to sort the records by (Uses the first column by default)
                 A key(Eg. str.lower()) function, axis = 0 for sorting by index
                 and a reverse functionality for asc, desc switching (False by default)
        
        OUTPUTS : A flag to indiacte successful sorting completion. 
    """
    
    import pandas as pd
    if type(file_name) is not str:
        raise TypeError(f"The expected filename is a string, not {type(file_name)}")
    if (type(by) not in [str,list]) and (by is not None):
        raise TypeError(f"The expected by kewyword should be a string or a list of strings, not {type(by)}")
    if type(axis) is not int or axis not in [0,1]:
        raise ValueError(f"The axis should be either 0 or 1, not {axis}")
    
    file_ext = file_name[-file_name[::-1].find('.'):].lower()
    if file_ext == "xlsx":
        global data
        data = pd.read_excel(file_name)
    else:
        try:    
            exec(f"global data; data = pd.read_{file_ext}('{file_name}')")
            #return data
        except AttributeError:
            raise ValueError(f"The file extension should a valid record type file, not {file_ext}")

    if by is None and axis == 0:
        by = data.columns[0]
        
    data.sort_values(by = by, axis = axis,ascending = not reverse, inplace = True)
    #data.reset_index(inplace=True)
    
    if file_ext == 'xlsx':
        data.to_excel(file_name)
    else:
        exec(f"data.to_{file_ext}('{file_name}')")

    print(f"Sorted {file_name} successfully!")
    return True

if __name__ == "__main__":
    sort_File('train.csv','Name')
    sort_File('train.xlsx','Name')