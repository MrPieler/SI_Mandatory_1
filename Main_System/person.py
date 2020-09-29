import xml.etree.ElementTree as gfg  

class Person:
    def __init__(self, first_name, last_name, cpr, email, dob, address, phone, country, nemID=None):
        self.first_name = first_name
        self.last_name = last_name
        self.cpr = cpr
        self.email = email
        self.dob = dob
        self.address = address
        self.phone = phone
        self.country = country
        self.nemID = nemID

    def serialize_xml(self):
        root = gfg.Element("Person") 
        
        a1 = gfg.SubElement(root, "FirstName") 
        a1.text = self.first_name
        a2 = gfg.SubElement(root, "LastName") 
        a2.text = self.last_name
        a3 = gfg.SubElement(root, "CprNumber")
        a3.text = self.cpr
        a4 = gfg.SubElement(root, "Email")
        a4.text = self.email
        
        tree = gfg.ElementTree(root) 
        
        return tree