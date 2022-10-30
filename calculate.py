from table_percentage import TablePercentage
from Date import DateCalculate, Condition


class PercentageCalculate:
    def __init__(self):
        self.price = 0.
        self.count_room = 0.
        self.floor = 0.
        self.apartment_area = 0.
        self.kitchen_area = 0.
        self.balcony = 0.
        self.metro_distance = 0.
        self.condition = 0.


class CalculateAnalog:
    def __init__(self, origindate: DateCalculate, analogdate: DateCalculate):
        self.origin = origindate
        self.origin.price = 0
        self.analog = analogdate
        self.percentage = PercentageCalculate()
        self.price_change = 0
        self.__calculate()

    @property
    def __k_prince(self) -> float:
        return TablePercentage.price / 100

    @property
    def __k_floor(self) -> float:
        def index_k_floor(date: DateCalculate):
            if date.floor == 1:
                return 0
            if date.maximum_floor == date.floor:
                return 2
            return 1

        i = index_k_floor(self.origin)
        j = index_k_floor(self.analog)
        return TablePercentage.floor[i][j] / 100

    @property
    def __k_apartment_area(self) -> float:
        def index_k_apartment_area(date: DateCalculate):
            if date.apartment_area < 30:
                return 0
            if date.apartment_area < 50:
                return 1
            if date.apartment_area < 65:
                return 2
            if date.apartment_area < 90:
                return 3
            if date.apartment_area < 120:
                return 4
            return 5

        i = index_k_apartment_area(self.origin)
        j = index_k_apartment_area(self.analog)
        return TablePercentage.apartment_area[i][j] / 100

    @property
    def __k_kitchen_area(self) -> float:
        def index_k_kitchen_area(date: DateCalculate):
            if date.apartment_area < 7:
                return 0
            if date.apartment_area < 10:
                return 1
            # if date.apartment_area < 15:
            return 2

        i = index_k_kitchen_area(self.origin)
        j = index_k_kitchen_area(self.analog)
        return TablePercentage.kitchen_area[i][j] / 100

    @property
    def __k_balcony(self) -> float:
        def index_k_balcony(date: DateCalculate):
            return int(date.is_balcony)

        i = index_k_balcony(self.origin)
        j = index_k_balcony(self.analog)
        return TablePercentage.balcony[i][j] / 100

    @property
    def __k_metro_distance(self) -> float:
        def index_k_metro_distance(date: DateCalculate):
            if date.metro_distance < 5:
                return 0
            if date.metro_distance < 10:
                return 1
            if date.metro_distance < 15:
                return 2
            if date.metro_distance < 30:
                return 3
            if date.metro_distance < 60:
                return 4
            return 5

        i = index_k_metro_distance(self.origin)
        j = index_k_metro_distance(self.analog)
        return TablePercentage.metro_distance[i][j] / 100

    @property
    def __condition(self) -> int:
        def index_condition(date: DateCalculate):
            if date.condition == Condition.without_finishing:
                return 0
            if date.condition == Condition.municipal_repair:
                return 1
            return 2

        i = index_condition(self.origin)
        j = index_condition(self.analog)
        return TablePercentage.condition[i][j]

    def __calculate(self):
        price = self.analog.price / self.analog.apartment_area

        self.percentage.price = self.__k_prince
        price += price * self.percentage.price

        self.percentage.apartment_area = self.__k_apartment_area
        price += price * self.percentage.apartment_area

        self.percentage.metro_distance = self.__k_metro_distance
        price += price * self.percentage.metro_distance

        self.percentage.floor = self.__k_floor
        price += price * self.percentage.floor

        """
        self.percentage.count_rooms = self.__k_count_rooms
        price += price * self.percentage.count_rooms
        """

        self.percentage.kitchen_area = self.__k_kitchen_area
        price += price * self.percentage.kitchen_area

        self.percentage.balcony = self.__k_balcony
        price += price * self.percentage.balcony

        self.percentage.condition = self.__condition / price
        price += price * self.percentage.condition

        self.price_change = price


def calculate(lst):
    # lst = [CalculateAnalog(...) for i in range(10)]
    prices = [p.price_change for p in lst]
    difference = max(prices) / min(prices) - 1.0
    print(difference)

    k = 0.0
    ls = []
    for p in lst:
        sm = 0
        for x in p.percentage.__dict__.values():
            sm += abs(x) * 100
        k += 1 / sm
        ls.append(sm)
    print(ls)

    l = []
    for p in ls:
        l.append(1 / p / k)
    print(l)

    sm = 0
    for i in range(len(prices)):
        sm += prices[i] * l[i]
    sm = round(sm, -2)
    print(sm)

    print(sm * lst[0].origin.apartment_area)
