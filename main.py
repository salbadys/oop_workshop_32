from typing import List


class Trip:
    def __init__(self,distance: float, comment: str = "Просто поездка") -> None:
        self.distance = distance
        self.comment = comment

class Transport:
    def __init__(self, fuel:int, trips: List[Trip]) -> None:
        self.fuel = fuel
        self.trips = trips
    
    def add_trip(self, trip: Trip) -> None:
        """Добавляет поездку"""
        self.trips.append(trip)

    def sum_trip_distance(self) -> float:
        """Рассчитывает всю пройденную станцию данного вида транспорта"""
        
        return sum([trip.distance for trip in self.trips])
    
    def calc_reachable_distance(self):
        """Оставшийся путь транспорта с учётом сделанных поездок"""
        raise NotImplemented("Для базового класса нереализуемо")

class Car(Transport):
    FUEL_CONSUMPTION_CAR = 0.12 #л на км
    def calc_reachable_distance(self) -> str:
        result = (self.fuel - (self.sum_trip_distance() * self.FUEL_CONSUMPTION_CAR)) // self.FUEL_CONSUMPTION_CAR
        return f'Машина осталось ехать {result} км'

class Airplane(Transport):
    FUEL_CONSUMPTION_AIRPLANE = 200

    def calc_reachable_distance(self):
        result = self.fuel - (self.sum_trip_distance() * self.FUEL_CONSUMPTION_AIRPLANE) // self.FUEL_CONSUMPTION_AIRPLANE
        return f'Самолёту осталось лететь {result} км'

audi = Car(80, [
    Trip(200,"Калуга - Москва"),
    Trip(222,"fff")
])

print(audi.calc_reachable_distance())