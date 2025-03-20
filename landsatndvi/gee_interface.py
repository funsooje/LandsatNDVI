import ee

def initialize_gee():
    """
    Initializes the Google Earth Engine API.
    If the initialization fails, instructs the user to authenticate.
    """
    try:
        ee.Initialize()
    except Exception as e:
        raise RuntimeError("Google Earth Engine must be authenticated. Run the following in your terminal: earthengine authenticate")