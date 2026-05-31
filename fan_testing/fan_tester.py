from fan import Fan

def main():
    fan1 = Fan(Fan.FAST, 10, "yellow", True)
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    # display fan1 details
    print("Fan 1:\n"
          "Speed:", fan1.get_speed(), "\n"
          "Radius:", fan1.get_radius(), "\n"
          "Color:", fan1.get_color(), "\n"
          "On:", fan1.is_on())

    # display fan2 details
    print("\nFan 2: \n"
          "Speed:", fan2.get_speed(), "\n"
          "Radius:", fan2.get_radius(), "\n"
          "Color:", fan2.get_color(), "\n"
          "On:", fan2.is_on())

if __name__ == "__main__":
    main()