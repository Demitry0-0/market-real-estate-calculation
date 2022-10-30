import enum


class Segment(enum.Enum):
    new_building = "новостройка"
    modern_housing = "современное жилье"
    old_housing_stock = "старый жилой фонд"


class WallMaterial(enum.Enum):
    Brick = "кирпич"
    panel = "панель"
    monolith = "монолит"


class Condition(enum.Enum):
    without_finishing = "без отделки"
    municipal_repair = "муниципальный ремонт"
    modern_finishing = "современная отделка"


class Data:
    def __init__(self, address: str, count_rooms: int, segment: Segment, maximum_floor: int,
                 wall_material: WallMaterial, floor: int, apartment_area: float,
                 kitchen_area: float, is_balcony: bool, metro_distance: float, condition: Condition):
        self.address = address  # !
        self.count_rooms = count_rooms  # ?
        self.segment = segment  # !
        self.maximum_floor = maximum_floor  # @
        self.wall_material = wall_material  # !
        self.floor = floor  # @
        self.apartment_area = apartment_area  # @
        self.kitchen_area = kitchen_area  # @
        self.is_balcony = is_balcony  # @
        self.metro_distance = metro_distance  # @
        self.condition = condition  # @


class DateCalculate:
    def __init__(self, full_price: int,
                 count_rooms: int, maximum_floor: int,
                 floor: int, apartment_area: float,
                 kitchen_area: float, is_balcony: bool, metro_distance: float, condition: Condition):
        self.price = full_price
        self.count_rooms = count_rooms  # ?
        self.maximum_floor = maximum_floor  # @
        self.floor = floor  # @
        self.apartment_area = apartment_area  # @
        self.kitchen_area = kitchen_area  # @
        self.is_balcony = is_balcony  # @
        self.metro_distance = metro_distance  # @
        self.condition = condition  # @



