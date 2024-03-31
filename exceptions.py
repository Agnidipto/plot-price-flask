class ModelNotLoaded(Exception):
    """Custom exception for representing specific errors."""

    def __init__(self, message="Model is not loaded!"):
        self.message = message
        super().__init__(self.message)