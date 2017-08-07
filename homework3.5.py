# -*- coding: utf-8 -*-
import osa


def convert_temperature(value, from_unit, to_unit):
    client = osa.Client(
            'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
            )
    result = client.service.ConvertTemp(value, from_unit, to_unit)
    return result


def convert_currency(value, from_unit, to_unit):
    client = osa.Client(
            'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
            )
    result = client.service.ConvertToNum(
            fromCurrency=from_unit,
            toCurrency=to_unit,
            MetricWeightValue=value,
            amount=value,
            rounding=False
            )
    return result


def convert_length(value, from_unit, to_unit):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    result = client.service.ChangeLengthUnit(value, from_unit, to_unit)
    return result


def calculate_means(file_name):
    with open(file_name) as file:
        temperature_sum = 0
        count = 0
        for line in file:
            temperature_list = line.split()
            temperature_sum += int(temperature_list[0])
            count += 1
    return(temperature_sum/count)


def total_distance(file_name):
    with open(file_name) as file:
        distance = 0
        for line in file:
            distance_list = line.split()
            distance += float(distance_list[1].replace(',', ''))
    return(distance)


def means_temp_in_c(file_name):
    means_temp_in_f = calculate_means(file_name)
    result = convert_temperature(
            means_temp_in_f, 'degreeFahrenheit', 'degreeCelsius'
            )
    return round(result, 2)


def total_distance_in_km(file_name):
    dist_in_miles = total_distance(file_name)
    result = convert_length(dist_in_miles, 'Miles', 'Kilometers')
    return round(result, 2)


def total_price(file_name):
    with open(file_name) as file:
        total_price = 0
        for line in file:
            price_list = line.split()
            total_price += convert_currency(
                    int(price_list[1]), price_list[2], 'RUB'
                    )
    return(round(total_price))

print(means_temp_in_c('temps.txt'))
print(total_price('currencies.txt'))
print(total_distance_in_km('travel.txt'))

