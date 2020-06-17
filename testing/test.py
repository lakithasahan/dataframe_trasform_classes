from core_classes.comma_separated_text_handling import comma_separated_handling_class
import pandas as pd
import numpy as np


# getting data from the data_files folder
df = pd.read_excel('insurance_data_file.xlsx', sheet_name='Policy Statistics')

# class testing starts
class_obj = comma_separated_handling_class(df)
df = class_obj.main()

# testing code
for value in df['Value']:
    print(value)
    print(type(value))









