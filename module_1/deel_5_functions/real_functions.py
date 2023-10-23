import math
from test_lib import test, report

def calculate_cilinder_content(nr1: float, nr2: float) ->float:
    inhoud = (nr1/ 2) * (nr1 / 2) * math.pi * nr2
    afronding = round(inhoud, 1)
    return afronding

nr1 = 8.0
nr2 = 5.0
expect_content = 251.3
calculated_content = calculate_cilinder_content(nr1,nr2)
name = f'test diameter: {nr1} height: {nr2}'
test(name, expect_content, calculated_content )

report()


def afronden_stuivers(bedrag: float):
    STUIVER = 5
    som = round(bedrag * 100 / STUIVER) * STUIVER / 100
    return som

bedrag = 14.08
expect_content = 14.10
calculated_content = afronden_stuivers(bedrag)
name = f"afronden bedrag: {bedrag} = {expect_content}"
test(name, expect_content, calculated_content )

report()