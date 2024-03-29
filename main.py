#!/usr/bin/python3
The error message indicates a syntax error, likely caused by an invalid syntax around line 108. It seems like there's an issue with the code structure or formatting.

Given that the error message points to the beginning of a multi-line string (indicated by triple backticks ```), it suggests that there might be a mistake in how the code was copied or pasted.

Ensure that you haven't inadvertently copied any non-code text, such as markdown code blocks (```), when integrating the provided code. Markdown code blocks are not valid Python syntax and should not be included in the Python script.

Here's a corrected version of the code without any markdown code blocks:

```python
class RawMaterial:
    def __init__(self, name, region, town, quantity, crop_type):
        self.name = name
        self.region = region
        self.town = town
        self.quantity = quantity
        self.crop_type = crop_type

class RawMaterialInventory:
    def __init__(self):
        self.materials = []

    def add_material(self, material):
        self.materials.append(material)

    def search_materials_by_region(self, region):
        materials_in_region = [material for material in self.materials if material.region.lower() == region.lower()]
        return materials_in_region

    def search_materials_by_town(self, town):
        materials_in_town = [material for material in self.materials if material.town.lower() == town.lower()]
        return materials_in_town

    def search_materials_by_crop_type(self, crop_type):
        materials_of_crop_type = [material for material in self.materials if material.crop_type.lower() == crop_type.lower()]
        return materials_of_crop_type

    def get_total_quantity_by_region(self, region):
        total_quantity = sum(material.quantity for material in self.materials if material.region.lower() == region.lower())
        return total_quantity

# Sample data for raw materials inventory
raw_materials_inventory = RawMaterialInventory()

# Adding sample raw materials based on the provided information

# Northern Region
raw_materials_inventory.add_material(RawMaterial("Tomatoes", "Northern", "Tamale", 500, "Vegetables"))
raw_materials_inventory.add_material(RawMaterial("Soybeans", "Northern", "Tamale", 300, "Legumes"))
raw_materials_inventory.add_material(RawMaterial("Groundnut", "Northern", "Yendi", 400, "Legumes"))
raw_materials_inventory.add_material(RawMaterial("Cassava", "Northern", "Bimbilla", 200, "Starchy Crops"))
raw_materials_inventory.add_material(RawMaterial("Yam", "Northern", "Salaga", 600, "Starchy Crops"))

# Savannah Region
raw_materials_inventory.add_material(RawMaterial("Maize", "Savannah", "Damongo", 700, "Cereals"))
raw_materials_inventory.add_material(RawMaterial("Sorghum", "Savannah", "Sawla", 500, "Cereals"))
raw_materials_inventory.add_material(RawMaterial("Rice", "Savannah", "Daboya", 300, "Cereals"))

# North East Region
raw_materials_inventory.add_material(RawMaterial("Vegetables", "North East", "Nalerigu", 200, "Vegetables"))
raw_materials_inventory.add_material(RawMaterial("Sesame", "North East", "Walewale", 150, "Crops"))
raw_materials_inventory.add_material(RawMaterial("Cashew", "North East", "Gambaga", 300, "Fruits"))

# Upper East Region
raw_materials_inventory.add_material(RawMaterial("Cereals", "Upper East", "Bolgatanga", 800, "Cereals"))
raw_materials_inventory.add_material(RawMaterial("Legumes", "Upper East", "Navrongo", 600, "Legumes"))

# Upper West Region
raw_materials_inventory.add_material(RawMaterial("Cereals", "Upper West", "Wa", 700, "Cereals"))
raw_materials_inventory.add_material(RawMaterial("Legumes", "Upper West", "Nadowli", 500, "Legumes"))

# Oti Region
raw_materials_inventory.add_material(RawMaterial("Cocoa", "Oti", "Jasikan", 1000, "Crops"))
raw_materials_inventory.add_material(RawMaterial("Maize", "Oti", "Kadjebi", 800, "Cereals"))

# Additional Regions and Raw Materials
raw_materials_inventory.add_material(RawMaterial("Coconuts", "Western", "Takoradi", 200, "Fruits"))
raw_materials_inventory.add_material(RawMaterial("Pineapples", "Western", "Sekondi", 150, "Fruits"))

raw_materials_inventory.add_material(RawMaterial("Cocoa", "Ashanti", "Kumasi", 300, "Crops"))
raw_materials_inventory.add_material(RawMaterial("Plantains", "Ashanti", "Obuasi", 400, "Fruits"))

raw_materials_inventory.add_material(RawMaterial("Cocoa", "Eastern", "Koforidua", 250, "Crops"))
raw_materials_inventory.add_material(RawMaterial("Oil Palm", "Eastern", "Akim Oda", 350, "Fruits"))

raw_materials_inventory.add_material(RawMaterial("Pineapples", "Greater Accra", "Accra", 500, "Fruits"))
raw_materials_inventory.add_material(RawMaterial("Chillies", "Greater Accra", "Tema", 200, "Vegetables"))

raw_materials_inventory.add_material(RawMaterial("Cocoa", "Bono", "Sunyani", 400, "Crops"))
raw_materials_inventory.add_material(RawMaterial("Pineapples", "Bono", "Techiman", 300, "Fruits"))

raw_materials_inventory.add_material(RawMaterial("Plantains", "Bono East", "Techiman",

250, "Fruits"))
raw_materials_inventory.add_material(RawMaterial("Pineapples", "Bono East", "Kintampo", 150, "Fruits"))

raw_materials_inventory.add_material(RawMaterial("Cocoa", "Ahafo", "Goaso", 200, "Crops"))
raw_materials_inventory.add_material(RawMaterial("Cashew", "Ahafo", "Dormaa", 300, "Fruits"))

raw_materials_inventory.add_material(RawMaterial("Pineapples", "Central", "Cape Coast", 400, "Fruits"))
raw_materials_inventory.add_material(RawMaterial("Coconuts", "Central", "Elmina", 250, "Fruits"))

raw_materials_inventory.add_material(RawMaterial("Cocoa", "Volta", "Ho", 350, "Crops"))
raw_materials_inventory.add_material(RawMaterial("Oil Palm", "Volta", "Keta", 200, "Fruits"))

raw_materials_inventory.add_material(RawMaterial("Plantains", "Western North", "Sefwi Wiawso", 300, "Fruits"))
raw_materials_inventory.add_material(RawMaterial("Cocoa", "Western North", "Sefwi Debiso", 200, "Crops"))

# Sample function to display all raw materials
def display_all_raw_materials():
    print("Raw Materials Inventory:")
    for material in raw_materials_inventory.materials:
        print(f"Region: {material.region}, Town: {material.town}, Crop Type: {material.crop_type}, Quantity: {material.quantity}")

# Sample usage
display_all_raw_materials()
"""
