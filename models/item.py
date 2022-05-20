from typing import Dict   #this is the type hinting for the database.
import re
import requests
import uuid
from bs4 import BeautifulSoup
from models.model import Model

class Item(Model):
   
    collection = "items" 
    def __init__(self,url:str,tag_name:str,query:Dict,_id:str =None):
        super().__init__()
        self.url=url
        self.tag_name= tag_name
        self.query = query
        self.price=None
        #sets the collecton of every Item object to the collection called "item" in the pricing database.
        self._id =_id or uuid.uuid4().hex


#using type hinting to indicate the data type that is returned
    def load_price(self) -> float: 
        response=requests.get(self.url)
        content=response.content
        soup = BeautifulSoup(content, "html5")
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
            "query":self.query
        }


  