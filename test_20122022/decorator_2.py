class SmartHome:
    name = 'Джарвис'
    bloodthirsty = False

    @classmethod
    def change_bloodthirsty(cls, new_value):
        cls.bloodthirsty = new_value

    @staticmethod
    def hello(name):
        return f'Привет, {name}'

    @property
    def data(self):
        return {
            'name': self.name,
            'bloodthristy': self.bloodthirsty
        }

    def make_coffee(self):
        if self.bloodthirsty:
            return 'Я сегодня не в духе'
        else:
            return 'Через семь минут будет готово'


print(SmartHome.hello('Марк'))  # Привет, Марк
SmartHome.change_bloodthirsty(True)

home = SmartHome()
print(home.make_coffee())  # Я сегодня не в духе
print(home.data)  # {'name': 'Джарвис', 'bloodthirsty': True}

SmartHome.change_bloodthirsty(False)
print(home.make_coffee())  # Через семь минут будет готово