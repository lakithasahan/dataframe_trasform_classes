from opencage.geocoder import OpenCageGeocode
class lat_and_log_handling_class():

    def __init__(self, df):
        self.df = df

    def main(self):
        list_lat = []
        list_lng = []

        key = "203effefcc474b74b30dc0f52cb82ea8"
        geocoder = OpenCageGeocode(key)

        for index, row in self.df.iterrows():
            city = row['Province/State']
            state = row['Country/Region']
            query = str(city) + ", " + str(state)

            results = geocoder.geocode(query)
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            print(lat + ', ' + lng)
            list_lat.append(lat)
            list_lng.append(lng)
        return self.df


