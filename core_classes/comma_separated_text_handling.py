class comma_separated_handling_class():

    def __init__(self, df):
        self.df = df

    # main function that iterates through each column in a sheet
    def main(self):
        list_of_columns = list(self.df.columns)

        print(list_of_columns)  # testing code

        # calls remove_commas for each column in the sheet
        for column in list_of_columns:
            self.remove_commas(column)

        return self.df

    # removes the commas in each number and returns the edited dataset
    def remove_commas(self, column_name):
        count = 0   # counter for reference of element index in the respective column
        for value in self.df[column_name]:
            value = self.convert_to_string(value)

            # identify if the current element contains a comma
            if self.locate_commas(value):
                new_value = value.replace(",", "")   # substitute all the commas to blank spaces
                value = self.convert_to_float(new_value, value)
                self.df[column_name].iat[count] = value   # use element index to substitute new value

                print(self.df[column_name].iloc[count])  # testing code

            count = count + 1

    # identifies if an element contains a comma or not and returns true or false respectively
    def locate_commas(self, value):
        character = ','
        if character in value:
            return True
        else:
            return False

    # converts the given value to float
    def convert_to_float(self, new_value, value):
        try:
            final = float(new_value)
            return final
        except:
            print('Not a number')  # testing code
            return value

    # converts the given value to string
    def convert_to_string(self, value):
        final = str(value)
        return final




