class TerrainReport:
    def __init__(self, message=None):
        if message is None:
            self.all = message
            self.lat = None
            self.lon = None
            self.spacing = None
            self.terrain_height = None
            self.current_height = None
            self.pending = None
            self.loaded = None
        else:
            self.all = message
            self.lat = message.lat
            self.lon = message.lon
            self.spacing = message.spacing
            self.terrain_height = message.terrain_height
            self.current_height = message.current_height
            self.pending = message.pending
            self.loaded = message.loaded
