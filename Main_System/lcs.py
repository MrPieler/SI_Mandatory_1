# Created by Mikkel and Jakob

import pathlib
import pandas as pd
from random import randint
import requests
import json
import msgpack

from person import Person

cwd = pathlib.Path(__file__).parent.absolute()
base_url = "http://127.0.0.1:8080"

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
            
        headers = {"Content-Type": "application/xml"}
        response = requests.post(f"{base_url}/nemId", data=person.serialize_xml(), headers=headers)
        person.nemID = json.loads(response.content)["nemID"]

        with open(f"{cwd}/msgpack_files/{person.cpr}.msgpack", "wb") as outfile:
            packed = msgpack.packb(person.__dict__)
            outfile.write(packed)

        


