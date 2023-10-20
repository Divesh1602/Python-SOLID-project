from calculator import Calculator

weather_calculator = Calculator("weather_data.csv", column1=1, column2=2)
min_diff = weather_calculator.execute()
print("Minimum temperature difference:", min_diff)
