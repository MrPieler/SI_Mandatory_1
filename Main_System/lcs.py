import pathlib
import pandas as pd
from random import randint
import requests
import json
import msgpack

from person import Person

cwd = pathlib.Path(__file__).parent.absolute()
base_url = "http://localhost:8080/"

def gen_cpr(day, month, year):
    random_digits = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
    return f"{day}{month}{year}-{random_digits}"

if __name__ == "__main__":
    people = []
    for index, row in pd.read_csv(f"{cwd}\people.csv").iterrows():
        day, month, year = row["DateOfBirth"].split("-")       
        cpr = gen_cpr(day, month, year[-2:])

        person = Person(
            row["FirstName"], 
            row["LastName"], 
            cpr, 
            row["Email"], 
            row["DateOfBirth"],
            row["Address"], 
            row["Phone"],
            row["Country"])
            
        response = requests.post(f"{base_url}/nemID", person.serialize_xml())
        person.nemID = response.content["nemID"]

        with open(f"{cwd}/msgpack_files/{person.cpr}.msgpack", "wb") as outfile:
            packed = msgpack.packb(person.__dict__)
            outfile.write(packed)

        


