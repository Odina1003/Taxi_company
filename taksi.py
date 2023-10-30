from passenger import Passager
from taksi_company import TaxiCompany
from place import Place

class Taxi:
    def __init__(self, name, surname, id):
        self._name = name
        self._surname = surname
        self._id = id
        self._taxi_band: list[TaxiCompany]
    @property
    def name(self):
        return self._name
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def id(self):
        return self._id

    def to_string(self):
        return f'{self.name}, {self.surname}, {self.id}'
    
    def begin_trip(self, passager: Passager):
        return "Manzil qabul qilindi"
    
    def terminate_trip(self, name, places: Place):
        print(end_trips = list(places))
        for i in self._taxi_band:
            if name in self._taxi_band:
                self._taxi_band.remove(name)
                return "taxi bo'sh"
        return "Tugatildi"