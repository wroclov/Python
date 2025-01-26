# UnitConverterLibrary.py

from robot.api.deco import keyword
import unit_converter

class UnitConverterLibrary:
    @keyword
    def convert_miles_to_kilometers(self, miles):
        return unit_converter.miles_to_kilometers(float(miles))

    @keyword
    def convert_kilometers_to_miles(self, kilometers):
        return unit_converter.kilometers_to_miles(float(kilometers))

    @keyword
    def convert_fahrenheit_to_celsius(self, fahrenheit):
        return unit_converter.fahrenheit_to_celsius(float(fahrenheit))

    @keyword
    def convert_celsius_to_fahrenheit(self, celsius):
        return unit_converter.celsius_to_fahrenheit(float(celsius))

    @keyword
    def convert_celsius_to_kelvin(self, celsius):
        return unit_converter.celsius_to_kelvin(celsius)

    @keyword
    def convert_kelvin_to_celsius(self, kelvin):
        return unit_converter.kelvin_to_celsius(kelvin)

    @keyword
    def convert_fahrenheit_to_kelvin(self, fahrenheit):
        return unit_converter.fahrenheit_to_kelvin(fahrenheit)

    @keyword
    def convert_kelvin_to_fahrenheit(self, kelvin):
        return unit_converter.kelvin_to_fahrenheit(kelvin)

    @keyword
    def convert_pounds_to_kilograms(self, pounds):
        return unit_converter.pounds_to_kilograms(float(pounds))

    @keyword
    def convert_kilograms_to_pounds(self, kilograms):
        return unit_converter.kilograms_to_pounds(float(kilograms))

    @keyword
    def convert_yards_to_meters(self, yards):
        return unit_converter.yards_to_meters(float(yards))

    @keyword
    def convert_meters_to_yards(self, meters):
        return unit_converter.meters_to_yards(float(meters))
