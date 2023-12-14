import unittest
import json
from neows_client.api import NeoWsClient

API_KEY = 'DEMO_KEY'
class TestAPI(unittest.TestCase):

    def test_get_asteroid_feed(self):
        neo_client = NeoWsClient(API_KEY)
        # Example test for get_asteroid_feed function
        start_date = '2023-01-01'
        end_date = '2023-01-08'
        data = neo_client.get_asteroid_feed(start_date, end_date)
        self.assertIn('near_earth_objects', data)
        self.assertTrue(len(data['near_earth_objects']) > 0)

    def test_get_asteroid_lookup(self):
        neo_client = NeoWsClient(API_KEY)
        # Example test for get_asteroid_lookup function
        asteroid_id = '3542519'  # Example asteroid ID, change as needed
        data = neo_client.get_asteroid_lookup(asteroid_id)
        self.assertIn('name', data)
        self.assertEqual(data['id'], asteroid_id)

    def test_browse_asteroids(self):
        neo_client = NeoWsClient(API_KEY)
        # Example test for browse_asteroids function
        data = neo_client.browse_asteroids()
        self.assertIn('near_earth_objects', data)
        self.assertTrue(len(data['near_earth_objects']) > 0)
    def test(self):
        neows_client = NeoWsClient(API_KEY)
        data = neows_client.get_asteroid_feed('2023-01-01', '2023-01-08')

        # Flatten the data, as it's nested under dates
        asteroids = [asteroid for date in data['near_earth_objects'] for asteroid in data['near_earth_objects'][date]]
        # Querying
        filtered_asteroids = neows_client.query_asteroids(asteroids, 100)

        # Analysis
        stats = neows_client.get_asteroid_statistics(filtered_asteroids)
        # Print results
        print(stats)
        
        hazard_count = neows_client.analyze_potential_hazards(filtered_asteroids)
        print(f"Number of potentially hazardous asteroids: {hazard_count}")


        # Visualization
        neows_client.plot_asteroid_diameter_distribution(filtered_asteroids)


if __name__ == '__main__':
    unittest.main()
