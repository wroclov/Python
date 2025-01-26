# unit_converter.py

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def fahrenheit_to_celsius(fahrenheit):
    fahrenheit = float(fahrenheit)
    if fahrenheit < -459.67:
        raise ValueError("Temperature below absolute zero is not possible.")
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    celsius = float(celsius)
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not possible.")
    return (celsius * 9 / 5) + 32
def celsius_to_kelvin(celsius):
    celsius = float(celsius)
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not possible.")
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    kelvin = float(kelvin)
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero is not possible.")
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    fahrenheit = float(fahrenheit)
    if fahrenheit < -459.67:
        raise ValueError("Temperature below absolute zero is not possible.")
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    kelvin = float(kelvin)
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero is not possible.")
    kelvin = float(kelvin)
    celsius = kelvin - 273.15
    return (celsius * 9 / 5) + 32

def pounds_to_kilograms(pounds):
    return pounds * 0.45359237

def kilograms_to_pounds(kilograms):
    return kilograms / 0.45359237

def yards_to_meters(yards):
    return yards * 0.9144

def meters_to_yards(meters):
    return meters / 0.9144
