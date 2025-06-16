#write a python program to create a mobile class and declare the states of mobile as colour,price,brand,series,version,features,storage,battery_capacity,ram,processor
#create 10 objects and initalize using constructer print the details of the individual objets using function
class Mobile:
    def __init__(self, colour, price, brand, series, version, features, storage, battery_capacity, ram, processor):
        self.colour=colour
        self.price=price
        self.brand=brand
        self.series=series
        self.version=version
        self.features=features
        self.storage=storage
        self.battery_capacity=battery_capacity
        self.ram =ram
        self.processor= processor

    def display_details(self):
        print("-----mobile_details-----")
        print(f"Brand           : {self.brand}")
        print(f"Series          : {self.series}")
        print(f"Version         : {self.version}")
        print(f"Colour          : {self.colour}")
        print(f"Price           : ₹{self.price}")
        print(f"Features        : {self.features}")
        print(f"Storage         : {self.storage}")
        print(f"Battery_Capacity: {self.battery_capacity} mAh")
        print(f"RAM             : {self.ram} GB")
        print(f"Processor       : {self.processor}")

m1 = Mobile("Black", 15000,"samsung","galaxy","M14","5G, DualSIM","128GB", 6000, 6, "Exyno 1330")
m2 = Mobile("White",20000, "googlepixel", "Note", "Note 12", "AMOLED, 5G", "256GB", 5000, 8, "Snapdragon 695")
m3 = Mobile("Black",15000,"oneplus","galaxy","M14","5G, DualSIM","128GB", 6000, 6, "Exyno 1330")
m4 = Mobile("White",20000, "googlepixel", "14", "Note 12", "AMOLED, 5G", "256GB", 5000, 8, "Snapdragon 695")
m5 = Mobile("Black",15000,"samsungs24","galaxy","M14","5G, DualSIM","128GB", 6000, 6, "Exyno 1330")
m6 = Mobile("White",20000, "i10", "Note", "Note 12", "AMOLED, 5G", "256GB", 5000, 8, "Snapdragon 695")
m7 = Mobile("Black", 15000,"iqoo","galaxy","M14","5G, DualSIM","128GB", 6000, 6, "Exyno 1330")
m8 = Mobile("White",20000, "Redmi", "10", "Note 12", "AMOLED, 5G", "256GB", 5000, 8, "Snapdragon 695")
m9 = Mobile("Black",15000,"samsung","galaxy","M14","5G, DualSIM","128GB", 6000, 6, "Exyno 1330")
m10 = Mobile("White",20000, "apple", "5", "Note 12", "AMOLED, 5G", "256GB", 5000, 8, "Snapdragon 695")

m1.display_details()
m2.display_details()
m3.display_details()
m4.display_details()
m5.display_details()
m6.display_details()
m7.display_details()
m8.display_details()
m9.display_details()
m10.display_details()

    



