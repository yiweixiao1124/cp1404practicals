COLOR_TO_CODE = {"aliceblue": "#f0f8ff", "amaranth": "#e52b50", "amber": "	#ffbf00", "amethyst": "#9966cc",
                 "antiquewhite": "#faebd7", "aqua": "#00ffff", "babyblue": "#89cff0", "babypink": "#f4c2c2", "beige": "#f5f5dc", "darkorchid": "#9932cc"}

color_name = input("Enter color name: ").lower()
while color_name != " ":
    try:
        print(f"{COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid name")
    color_name = input("Enter color name: ").lower()
print("Goodbye.")