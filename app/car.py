class Car:    def __init__(            self,            brand: str,            fuel_consumption: float,    ) -> None:        self.brand = brand        self.fuel_consumption = fuel_consumption    def calculate_trip_cost(            self,            distance: int,            FUEL_PRICE: int    ) -> float:        cost_trip = (distance * (self.fuel_consumption / 100)) * FUEL_PRICE        return cost_trip