from dataclasses import dataclass
from typing import Any

import requests
from fuel import Fuel


mise_url = "https://carburanti.mise.gov.it/ospzApi/registry/servicearea/"


@dataclass
class FuelStation:
    id: int
    name: str
    nomeImpianto: str
    address: str
    brand: str
    fuels: list[Fuel]

    @staticmethod
    def from_dict(obj: Any) -> "FuelStation":
        _id = int(obj.get("id"))
        _name = str(obj.get("name"))
        _nomeImpianto = str(obj.get("nomeImpianto"))
        _address = str(obj.get("address"))
        _brand = str(obj.get("brand"))
        _fuels = [Fuel.from_dict(y) for y in obj.get("fuels")]
        return FuelStation(_id, _name, _nomeImpianto, _address, _brand, _fuels)

    def get_fuel_data(self):
        """Return a dictionary of fuel prices."""
        return {fuel.name: fuel.to_dict() for fuel in self.fuels}


def get_station_from_impianto(impianto_id: str):
    url = mise_url + impianto_id
    result = requests.get(url)
    station = FuelStation.from_dict(result.json())
    return station
