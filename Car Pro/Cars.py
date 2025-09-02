from typing import Union

class Cars_info:
    def __init__(self, name: Union[str, int], engine: Union[str, int], model: int):
        self.name = str(name)
        self.engine = str(engine)
        self.model = int(model)
    
    def __str__(self):
        return f"{self.name} | engine: {self.engine} | model: {self.model}"
    

class Car_manager:
    def __init__(self):
        self.cars_list = []

    def add_car(self):
        name = input("Car name: ")
        engine = input("Engine: ")
        model = int(input("Model (year): "))

        car = Cars_info(name, engine, model)
        self.cars_list.append(car)
        print("Car added.")

    def find_cars(self, name: str):
        for car in self.cars_list:
            if car.name == name:
                print(car)
                return
        print("Car name is not available in this list")

    def show_all_cars(self):
        if not self.cars_list:
            print("No cars yet.")
            return
        print("Cars list:")
        for car in self.cars_list:
            print(" -", car.name)


    def delet_car(self , name: str) :
        for car in self.cars_list:
            if car.name == name:
                self.cars_list.remove(car)
                print('Car deleted')
                return
        print('Car name is not available in this list')
        