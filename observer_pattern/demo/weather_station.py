from __future__ import annotations
from abc import ABC, abstractmethod
from termcolor import colored
from typing import List, Tuple

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
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, previous: bool = False):
        for observer in self.observers:
            if not previous:
                observer.update(self.temperature, self.humidity, self.pressure)
            else:
                observer.previous_temperature = self.get_temperature()
                observer.previous_humidity = self.get_humidity()
                observer.previous_pressure = self.get_pressure()

    def measurements_changed(self):
        self.notify_observers()

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.notify_observers(previous = True)
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

    def __get_statistics(self)-> Tuple[list]:
        min_statistics = [self.previous_temperature, self.previous_humidity, self.previous_pressure]
        max_statistics = [self.previous_temperature, self.previous_humidity, self.previous_pressure]

        data = [self.temperature, self.humidity, self.pressure]
        i = 0
        for d in data:
            if min_statistics[i] is None:
                min_statistics[i] = d
            else:
                if d < min_statistics[i]:
                    min_statistics[i] = d
            
            if max_statistics[i] is None:
                max_statistics[i] = d
            else:
                if d > max_statistics[i]:
                    max_statistics[i] = d

            i += 1

        average_statistics = [(a + b) / 2 for a, b in zip(min_statistics, max_statistics)]
        return min_statistics, max_statistics, average_statistics

    def display(self)-> str:
        min_statistics, max_statistics, average_statistics = self.__get_statistics()
        return f"Min Conditions: Temperature: {min_statistics[0]} F degrees, Humidity: {min_statistics[1]} %, Pressure: {min_statistics[2]} bar. \
                \nMax Conditions: Temperature: {max_statistics[0]} F degrees, Humidity: {max_statistics[1]} %, Pressure: {max_statistics[2]} bar. \
                \nAverage Conditions: Temperature {average_statistics[0]} F degrees, Humidity: {average_statistics[1]} %, Pressure: {average_statistics[2]} bar"

class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def __get_forecast(self)-> str:
        if self.previous_pressure is None:
            return "Improving weather on the way!"
        else:
            if self.previous_pressure < self.pressure:
                return "Improving weather on the way!"
            elif self.previous_pressure == self.pressure:
                return "More of the same"
            else:
                return "Watch out for cooler, rainy weather"

    def display(self)-> str:
        return f"Forecast: {self.__get_forecast()}"

if __name__ == '__main__':
    weather_data = WeatherData()
    current_conditions_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 1)
    print(colored('------------- CURRENT CONDITIONS DISPLAY ------------', 'red'))
    print(current_conditions_display.display())
    print(colored('----------------- STATISTICS DISPLAY ----------------', 'blue'))
    print(statistics_display.display())
    print(colored('----------------- FORECAST DISPLAY -----------------', 'green'))
    print(forecast_display.display(),'\n')

    weather_data.set_measurements(82, 70, 0.98)
    print(colored('------------- CURRENT CONDITIONS DISPLAY ------------', 'red'))
    print(current_conditions_display.display())
    print(colored('----------------- STATISTICS DISPLAY ----------------', 'blue'))
    print(statistics_display.display())
    print(colored('----------------- FORECAST DISPLAY -----------------', 'green'))
    print(forecast_display.display(),'\n')

    weather_data.set_measurements(78, 90, 1.03)
    print(colored('------------- CURRENT CONDITIONS DISPLAY ------------', 'red'))
    print(current_conditions_display.display())
    print(colored('----------------- STATISTICS DISPLAY ----------------', 'blue'))
    print(statistics_display.display(),'\n')
    print(colored('----------------- FORECAST DISPLAY -----------------', 'green'))
    print(forecast_display.display())