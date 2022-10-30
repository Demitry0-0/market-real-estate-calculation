from calculate import CalculateAnalog, calculate
from Date import DateCalculate, Condition

origin = DateCalculate(full_price=0, count_rooms=2, maximum_floor=22, floor=7, apartment_area=85,
                       kitchen_area=15, is_balcony=True, metro_distance=11,
                       condition=Condition.municipal_repair)
analog1 = DateCalculate(28750000, 2, 24, 3, 77.4, 14, True, 10, Condition.modern_finishing)
analog2 = DateCalculate(30650000, 2, 18, 1, 84, 12, True, 14, Condition.modern_finishing)
analog3 = DateCalculate(26500000, 2, 18, 4, 64, 11.5, True, 11, Condition.modern_finishing)

a1 = CalculateAnalog(origin, analog1)
a2 = CalculateAnalog(origin, analog2)
a3 = CalculateAnalog(origin, analog3)

calculate([a1, a2, a3])
