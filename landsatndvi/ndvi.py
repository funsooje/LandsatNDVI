from .gee_interface import initialize_gee
import ee

def get_ndvi(point, start_date, end_date):
    """
    Returns the NDVI for a given point and date range.
    
    Parameters:
        point (tuple): A tuple containing the latitude and longitude of the point.
        start_date (str): The start date of the date range in the format 'YYYY-MM-DD'.
        end_date (str): The end date of the date range in the format 'YYYY-MM-DD'.
        
    Returns:
        NDVI value
    """
    # Initialize the Google Earth Engine API
    initialize_gee()
    
    # Create a point geometry
    point = ee.Geometry.Point(point)
    
    # Load the Landsat 8 surface reflectance data
    collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')
    
    # Filter the collection by date and location
    filtered = collection.filterDate(start_date, end_date).filterBounds(point)
    
    # Calculate the NDVI
    ndvi = filtered.map(lambda image: image.normalizedDifference(['B5', 'B4'])).mean()
    
    return ndvi