def check_weather(temperature):
    if temperature >= 20:
        print("It's warm enough to wear light clothes!")
    elif 10 <= temperature < 20:
        print("It's a bit cool, but a light jacket should be fine.")
    else:
        print("It's too cold, wear something warmer.")