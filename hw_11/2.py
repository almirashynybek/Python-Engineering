'''
Миксины:
○ Добавляют специфические функции (например,
  кэширование, логирование).
○ Обычно не содержат основного состояния и структуры
  объекта, а лишь дополняют их.
'''

class LogMixin:
    def log_action(self, message):
        """Log the action by printing or storing the message."""
        print(f"[LOG]: {message}")

class Cat(LogMixin):
    def make_sound(self):
        sound = "meowed"
        self.log_action(f"Cat: {sound}")
        # print(sound)

class Dog(LogMixin):
    def make_sound(self):
        sound = "barked"
        self.log_action(f"Dog: {sound}")
        # print(sound)

cat = Cat()
dog = Dog()

cat.make_sound()
dog.make_sound()