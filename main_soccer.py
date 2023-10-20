from calculator import Calculator

soccer_calculator = Calculator("soccer_data.csv", column1=1, column2=2)
min_diff = soccer_calculator.execute()
print("Minimum goal difference:", min_diff)
