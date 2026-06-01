from car_info import Car

def main():
    while True:
        try:
            year_model = int(input("Enter a Year Model of Car: "))
            make = input("Enter a model of Car: ")
            break
        except ValueError:
            print("Please enter a valid year model of Car")

    car = Car(make, year_model)
    print(car)

    print("Accelerating:")
    for _ in range(5):
        car.accelerate()
        print(car.get_speed())

    print("\nBraking:")
    for _ in range(5):
        car.brake()
        print(car.get_speed())

if __name__ == "__main__":
    main()