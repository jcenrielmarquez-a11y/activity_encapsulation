from car import Car

def main():
    year_model = int(input("Enter a Year Model of Car: "))
    make = input("Enter a model of Car: ")

    car = Car(year_model, make)

    print(f"\nYear Model: {car.get_make()}, Make: {car.get_year_model()}\n")

    print("Accelerating:")
    for i in range(5):
        car.accelerate()
        print(car.get_speed())

    print("\nBraking:")
    for i in range(5):
        car.brake()
        print(car.get_speed())