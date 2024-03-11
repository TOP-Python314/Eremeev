import datetime
from decimal import Decimal as d
import numbers


class PowerMeter:
    """
    Описывает двухтарифный счётчик потреблённой электрической мощности

    """

    def __init__(
            self,
            tariff1: numbers.Number = 5,
            tariff2: numbers.Number = 7,
            tariff2_starts: datetime.time = datetime.time(23),
            tariff2_ends: datetime.time = datetime.time(7)
    ):
        self.tariff1: dec = d(tariff1)
        self.tariff2: dec = d(tariff2)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power: dec = d(0)
        self.current_date: datetime.data = datetime.date.today().strftime("01-%m-%Y")
        self.charges: dict[datetime.date, dec] = {self.current_date: self.power}

    def __repr__(self):
        return f'<PowerMeter: {self.power} кВт/ч>'

    def __str__(self):
        return f'({datetime.date.today().strftime("%b")}) {self.charges[self.current_date]}'

    def meter(self, power: numbers.Number) -> dec:

        """
        Принимает значение потреблённой мощности, вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент

        """

        power = d(power)
        self.power += power.quantize(d("1.00"))
        if self.tariff2_ends < datetime.datetime.now().time() < self.tariff2_starts:
            power *= self.tariff1
        else:
            power *= self.tariff2
        self.charges[self.current_date] += power.quantize(d("1.00"))

        return power.quantize(d("1.00"))

#>>> pm2 = PowerMeter()
#>>> pm2.meter(2)
#Decimal('10.00')
#>>> pm2.meter(1.2)
#Decimal('6.00')
#>>> pm2
#<PowerMeter: 3.20 кВт/ч>
#>>> print(pm2)
#(Mar) 16.00        