def weather_info(temp):
    c = convertToCelsius(temp)
    if (c < 0):
        print(str(c) + " is freezing temperature")
        return (str(c) + " is freezing temperature")
    else:
        print(str(c) + " is above freezing temperature")
        return (str(c) + " is above freezing temperature")


def convertToCelsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius
weather_info(50)
