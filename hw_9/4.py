# Задание 1: Проверка времени суток

class TimeUtils:
    def is_morning(self, hour):
        if hour in range(6,13):
            return True
        
        return False
    
time = TimeUtils()
print(time.is_morning(12))
