from __future__ import annotations
from abc import ABC, abstractmethod
from termcolor import colored
from typing import List

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self, observer: Observer):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

class WeatherData(Subject):
    def __init__(self):
        self.observers: List[Observer] = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self)-> str:
        return f"Current conditions: {self.temperature} F degrees, {self.humidity} % and {self.pressure} bar."

class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self)-> str:
        return "Average, Min and Max measurements"

class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        return "Forecast"

if __name__ == '__main__':
    weather_data = WeatherData()
    current_conditions_display = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 1)
    print(current_conditions_display.display())
    weather_data.set_measurements(82, 70, 0.98)
    print(current_conditions_display.display())
    weather_data.set_measurements(78, 90, 1.03)
    print(current_conditions_display.display())