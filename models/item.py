from typing import Dict   #this is the type hinting for the database.
import re
import requests
import uuid
from dataclasses import dataclass, field
from bs4 import BeautifulSoup
from models.model import Model
@dataclass(eq=False)
class Item(Model):
    collection: str = field(init=False, default="items")
    url :str
    tag_name: str
    query: Dict
    price: float=field(default=None)
    _id: str = field(default_factory=lambda:uuid.uuid4().hex)

#using type hinting to indicate the data type that is returned
    def load_price(self) -> float: 
        response=requests.get(self.url)
        content=response.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query) 
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d*\.\d\d)") #look for a number with optional commas and 2 decimal places
        match = pattern.search(string_price) #search for the pattern
        found_price = match.group(1) #extract the first group that matches
        without_commas = found_price.replace(",","")
        self.price = float(without_commas)
        return self.price
        
        
#this mehtod converts a pyton object into a form that can be saved in mongodb.
    def json(self) -> Dict:
        return{
            "_id":self._id,
            "url":self.url,
            "tag_name":self.tag_name,
            "price":self.price,
            "query":self.query
        }


  