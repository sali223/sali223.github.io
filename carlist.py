class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class CarList:
    def __init__(self):
        self.cars = []

    def add_car(self, make, model, year):
        car = Car(make, model, year)
        self.cars.append(car)

    def remove_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model:
                self.cars.remove(car)
                return f"{make} {model} removed."
        return "Car not found."

    def display_cars(self):
        if not self.cars:
            return "No cars in the list."
        return "\n".join(str(car) for car in self.cars)

# Main menu
def main():
    car_list = CarList()

    while True:
        print("\nCar List Menu:")
        print("1. Add Car")
        print("2. Remove Car")
        print("3. Display Cars")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            car_list.add_car(make, model, year)
            print(f"{make} {model} added.")

        elif choice == "2":
            make = input("Enter car make to remove: ")
            model = input("Enter car model to remove: ")
            result = car_list.remove_car(make, model)
            print(result)

        elif choice == "3":
            print("\nCar List:")
            print(car_list.display_cars())

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
