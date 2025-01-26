import pytest
import unit_converter

def test_miles_to_kilometers():
    assert unit_converter.miles_to_kilometers(1) == 1.60934

def test_kilometers_to_miles():
    assert unit_converter.kilometers_to_miles(1.60934) == pytest.approx(1)

def test_fahrenheit_to_celsius():
    assert unit_converter.fahrenheit_to_celsius(32) == 0
    assert unit_converter.fahrenheit_to_celsius(212) == 100
    with pytest.raises(ValueError, match="Temperature below absolute zero is not possible."):
        unit_converter.fahrenheit_to_celsius(-460)

def test_celsius_to_fahrenheit():
    assert unit_converter.celsius_to_fahrenheit(0) == 32
    assert unit_converter.celsius_to_fahrenheit(100) == 212
    with pytest.raises(ValueError, match="Temperature below absolute zero is not possible."):
        unit_converter.celsius_to_fahrenheit(-274)

def test_celsius_to_kelvin():
    assert unit_converter.celsius_to_kelvin(0) == 273.15
    assert unit_converter.celsius_to_kelvin(100) == 373.15
    with pytest.raises(ValueError, match="Temperature below absolute zero is not possible."):
        unit_converter.celsius_to_kelvin(-274)

def test_kelvin_to_celsius():
    assert unit_converter.kelvin_to_celsius(273.15) == 0
    assert unit_converter.kelvin_to_celsius(373.15) == 100
    with pytest.raises(ValueError, match="Temperature below absolute zero is not possible."):
        unit_converter.kelvin_to_celsius(-1)

def test_fahrenheit_to_kelvin():
    assert unit_converter.fahrenheit_to_kelvin(32) == 273.15
    assert unit_converter.fahrenheit_to_kelvin(212) == 373.15
    with pytest.raises(ValueError, match="Temperature below absolute zero is not possible."):
        unit_converter.fahrenheit_to_kelvin(-460)

def test_kelvin_to_fahrenheit():
    assert unit_converter.kelvin_to_fahrenheit(273.15) == 32
    assert unit_converter.kelvin_to_fahrenheit(373.15) == 212
    with pytest.raises(ValueError, match="Temperature below absolute zero is not possible."):
        unit_converter.kelvin_to_fahrenheit(-1)

def test_pounds_to_kilograms():
    assert unit_converter.pounds_to_kilograms(1) == pytest.approx(0.45359237)

def test_kilograms_to_pounds():
    assert unit_converter.kilograms_to_pounds(0.45359237) == pytest.approx(1)

def test_yards_to_meters():
    assert unit_converter.yards_to_meters(1) == pytest.approx(0.9144)

def test_meters_to_yards():
    assert unit_converter.meters_to_yards(0.9144) == pytest.approx(1)
