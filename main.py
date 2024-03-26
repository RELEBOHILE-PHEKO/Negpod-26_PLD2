#!/usr/bin/env python3

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
