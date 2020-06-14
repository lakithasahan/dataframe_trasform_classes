from core_classes.comma_separated_text_handling import comma_separated_handling_class
import pandas as pd





#getting data from the data_files folder
df=pd.read_excel('data_files/insurance_data_file.xlsx')
print(df)



#class testing starts
class_obj=comma_separated_handling_class(df)


