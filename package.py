# Runtime complexity O (1) Space Complexity O (1) Creates the package class
class Package:

    def __init__(self, package_id, address, city, state, zip_code, dead_line, mass, special_note):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.dead_line = dead_line
        self.mass = mass
        self.special_note = special_note
        self.time_left_hub = None
        self.delivery_time = None
        self.delivery_truck = None
