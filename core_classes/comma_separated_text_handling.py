class comma_separated_handling_class():

    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name

    # removes the commas in each number and returns the edited dataset
    def remove_commas(self):
        count = 0   # counter for reference of element index in the respective column
        for value in self.df[self.column_name]:
            value = self.convert_to_string(value)

            # identify if the current element contains a comma
            if self.locate_commas(value):
                value = value.replace(",", "")   # substitute all the commas to blank spaces
                value = self.convert_to_float(value)
                self.df[self.column_name].iat[count] = value   # use element index to substitute new value
                print(self.df[self.column_name].iloc[count])

            count = count + 1

        return self.df

    # identifies if an element contains a comma or not and returns true or false respectively
    def locate_commas(self, value):
        character = ','
        if character in value:
            return True
        else:
            return False

    # converts the given value to float
    def convert_to_float(self, value):
        final = float(value)
        return final

    # converts the given value to string
    def convert_to_string(self, value):
        final = str(value)
        return final




