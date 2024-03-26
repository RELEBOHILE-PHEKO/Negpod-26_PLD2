class RawMaterial:
   def _init_(self, name, region, town, quantity, crop_type):
     self.name = name
     self.region = region
     self.town = town
     self.quantity = quantity
     self.crop_type = crop_type
class RawMaterialInventory:
    def init(self):
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
