from dataclasses import dataclass


@dataclass
class Connessione:
    ORIGIN_AIRPORT_ID: int
    DESTINATION_AIRPORT_ID: int
    numVoli: int
    sommaKm: int