# -*- coding: utf-8 -*-
import osa


def convert_weight(value, from_unit, to_unit):
    client = osa.Client('http://www.webservicex.net/convertMetricWeight.asmx?WSDL')
    result = client.service.ChangeMetricWeightUnit(
        MetricWeightValue=value,
        fromMetricWeightUnit=from_unit,
        toMetricWeightUnit=to_unit
    )
    return result

print(convert_weight(100, 'gramm', 'kilogramm'))

http://www.webservicex.net/ и http://fx.currencysystem.com/webservices/CurrencyServer4.asmx