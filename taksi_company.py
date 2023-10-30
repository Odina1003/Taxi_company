from taksi import Taxi
from passenger import Passager

class TaxiCompany:
    def __init__(self):
        self._taxi_list: list[Taxi] = []
        self._passenger_list: list[Passager] = []
        self._taxi_band = list()

    def add_taxi(self, name, surname, id):
        for taksi in self._taxi_list:
            if taksi.id != id:
                driver = Taxi(name, surname, id)
                self._taxi_list.append(driver)
                print('Taxi qo\'shildi')
            else:
                print("InvalidTaxiName")

    def get_available(self):
        pass

    def call_taxi(self, passeger: Passager):
        for driver in self._taxi_list:
            if driver.name in self._taxi_band:
                self._taxi_band.append(driver)
                self._taxi_list.remove(driver)
                return self._taxi_list
            else:
                return "Bekor qilindi"

    def get_lost_trips(self):
        return self._taxi_list
    
    def get_Trips(self, id):
        for i in self._taxi_list:
            if i.id != id:
                return "InvalidTaxiName"
            