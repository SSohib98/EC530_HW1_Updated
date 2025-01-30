import unittest
import math
import logging
from logging_config_main import setup_logging  

# Set up logging
setup_logging()  

# The functions to be tested
R = 6371.0  # Earth's radius in km

def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula to calculate distance
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    logging.info(f"Calculated distance: {distance} km")  # Info level log
    return distance

def find_closest_points(array1, array2):
    closest_points = []
    
    for point1 in array1:
        min_distance = float('inf')
        closest_point = None
        
        for point2 in array2:
            dist = haversine(point1[0], point1[1], point2[0], point2[1])
            logging.debug(f"Distance between {point1} and {point2}: {dist} km")  # Debug log statement

            if dist < min_distance:
                min_distance = dist
                closest_point = point2
                
        closest_points.append((point1, closest_point))
    
    logging.warning(f"Closest points calculated: {closest_points}")  # Warning level log
    return closest_points


# Unit Tests
class TestGeoFunctions(unittest.TestCase):

    def test_haversine(self):
        # Example: Distance between New York City and Los Angeles
        lat1, lon1 = 40.748817, -73.985428  # NYC
        lat2, lon2 = 34.052235, -118.243683  # LA

        # Expected distance between NYC and LA is around 3935.75 km
        expected_distance = 3935.75

        result = haversine(lat1, lon1, lat2, lon2)
        self.assertAlmostEqual(result, expected_distance, delta=10)  # Allowing a small margin of error

    def test_find_closest_points(self):
        # Test case: Find closest points between two arrays of coordinates
        array1 = [(40.748817, -73.985428), (34.052235, -118.243683)]  # NYC, LA
        array2 = [(51.507351, -0.127758), (48.856613, 2.352222), (40.730610, -73.935242)]  # London, Paris, NYC

        # Updated expected result based on the correct closest point calculation
        expected_result = [
            ((40.748817, -73.985428), (40.730610, -73.935242)),  # NYC is closest to NYC
            ((34.052235, -118.243683), (40.730610, -73.935242))   # LA is closest to NYC (not London)
        ]

        result = find_closest_points(array1, array2)
        logging.info(f"Test result: {result}")  
        logging.error("An error occurred while testing!")  
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
