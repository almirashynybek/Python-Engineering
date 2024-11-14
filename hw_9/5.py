# Задание 3: Конвертер температур

class TemperatureConverter:

    def celsius_to_fahrenheit(self, celsius):
        return ((celsius * 9//5) + 32)
    
    def fahrenheit_to_celsius(self, fahrenheit):
        return ((32 - fahrenheit) * 5//9)
    

result = TemperatureConverter()

print(result.celsius_to_fahrenheit(5))

print(result.fahrenheit_to_celsius(20))