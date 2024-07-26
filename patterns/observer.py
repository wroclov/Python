from abc import ABC, abstractmethod

# Observer abstract base class
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# Concrete Observer - Phone Display
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"Phone Display: Temperature updated to {temperature}°C")

# Concrete Observer - Web App Display
class WebAppDisplay(Observer):
    def update(self, temperature):
        print(f"Web App Display: Temperature updated to {temperature}°C")

# Subject (Observable) - Weather Station
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

# Client Code
if __name__ == "__main__":
    # Create the weather station
    weather_station = WeatherStation()

    # Create displays
    phone_display = PhoneDisplay()
    web_app_display = WebAppDisplay()

    # Register displays with the weather station
    weather_station.register_observer(phone_display)
    weather_station.register_observer(web_app_display)

    # Simulate temperature changes
    weather_station.set_temperature(25)
    weather_station.set_temperature(30)

    # Remove phone display and change temperature again
    weather_station.remove_observer(phone_display)
    weather_station.set_temperature(28)
