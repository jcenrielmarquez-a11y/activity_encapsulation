from fan import Fan

def main():
    fan1 = Fan(Fan.FAST, 10, "yellow", True)
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    #display fan1 details
    print("Fan1_Speed:", fan1.get_speed(),
          "Radius:", fan1.get_radius(),
          "Color:", fan1.get_color(),
          "On:", fan1.is_on())