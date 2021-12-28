# Импорт библиотек

from pyforms.controls   import ControlLabel 
from pyforms.controls   import ControlButton
from pyforms.basewidget import BaseWidget



# Главный класс приложения
class HelloWorld(BaseWidget): 
    
    def __init__(self, *args, **kwargs):
        # Инициализация с заголовком
        super().__init__('Hello World example')


        # Создание текстового поля
        self._hello = ControlLabel('Hello World!')

        # Создание кнопки закрытия приложения
        self._close = ControlButton('Exit')


        # Добавление поля на экран
        self._formset = [
            '_hello', '_close'
        ]


        # Добавление события для кнопки
        self._close.value = self._closeAction


    # При нажатии на кнопку
    def _closeAction(self):
        # Выводим сообщение о закрытии
        print("Закрытие приложения")

        # Выходим из приложения
        exit()




# Запуск приложения
if __name__ == "__main__":

    # Импорт start_app для запуска
    from pyforms import start_app

    # Запуск главного класса
    start_app(HelloWorld)