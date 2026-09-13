# single inheritance
class Parent:
    def am_parent(self):
        print("we are parent")
class Child(Parent):
    def am_child(self):
        print("we are child")
info = Child()
info.am_parent()
info.am_child()
print("-------------------------------------------------------------------------------------------")

# multiple inheritance (Many to one) - one child many parents
class Manager:
    def project_manager(self):
        print("I am the manager for the current project")
class Lead:
    def team_lead(self):
        print("I am the lead for this project and team")
class HR :
    def hr(self):
        print("I am the HR")
class Developer(Manager, Lead, HR):
    def developer(self):
        print("I am the developer and developing this project")
access1 = Developer()
access1.project_manager()
access1.team_lead()
access1.hr()
access1.developer()

print("------------------------------------------------------------------------------------------")

# multilevel inheritance (Many to one)
class Grass:
    def plant(self):
        print("I am a plant")
class Grasshopper(Grass):
    def insect(self):
        print("I am an insect and I eat grass")
class Frog(Grasshopper):
    def animal(self):
        print("I am an animal and I eat insects")
class Snake(Frog):
    def reptile(self):
        print("I am a reptile and I eat animals")
class Eagle(Snake):
    def bird(self):
        print("I am a bird and I eat reptiles")
foodchain = Eagle()
foodchain.plant()
foodchain.insect()
foodchain.animal()
foodchain.reptile()
foodchain.bird()

print("------------------------------------------------------------------------------------------")

# hierarchical inheritance (One to many) - one parent many children
class Samsung:
    def __init__(self, model, price, rating):
        self.model = model
        self.price = price
        self.rating = rating
    def display(self):
        print(f"Model: {self.model}, Price: {self.price}, Rating: {self.rating}")
class TV(Samsung):
    def __init__(self, model, price, rating, year, quality):
        super().__init__(model, price, rating)
        self.year = year
        self.quality = quality
    def display(self):
        return super().display()
class Mobile(Samsung):
    def __init__(self, model, price, battery):
        super().__init__(model, price, rating=None)  # Assuming rating is not applicable for Mobile
        self.battery = battery
    def display(self):
        return super().display()
class HomeAppliance(Samsung):
    def __init__(self, model, price, warranty):
        super().__init__(model, price, rating=None)  # Assuming rating is not applicable for HomeAppliance
        self.warranty = warranty
    def display(self):
        return super().display()
class Laptop(Samsung):
    def __init__(self, model, price, ram):
        super().__init__(model, price, rating=None)  # Assuming rating is not applicable for Laptop
        self.ram = ram
    def display(self):
        return super().display()
    
tv = TV("Samsung QLED", 1500, 4.5, 2021, "4K")
mobile = Mobile("Samsung Galaxy S21", 999, "4000mAh")   
home_appliance = HomeAppliance("Samsung Refrigerator", 1200, "2 years")
laptop = Laptop("Samsung Notebook 9", 1300, "16GB")
tv.display()
mobile.display()    
home_appliance.display()
laptop.display()