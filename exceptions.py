class ModelNotLoaded(Exception):
    """Custom exception for representing specific errors."""

    def __init__(self, message="Model is not loaded!"):
        self.message = message
        super().__init__(self.message)
        
class CannotLoadModel(Exception) :
    
    def __init__(self, message="Cannot Load Model!") :
        self.message = message
        super().__init__(self.message)
        
class CannotLoadLocations(Exception) :
    
    def __init__(self, message="Cannot Load Locations!") :
        self.message = message
        super().__init__(self.message)