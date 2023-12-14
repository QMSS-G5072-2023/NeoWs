import requests
import pandas as pd
import matplotlib.pyplot as plt

class NeoWsClient:
    def __init__(self, api_key='DEMO_KEY'):
        self.base_url = 'https://api.nasa.gov/neo/rest/v1'
        self.api_key = api_key

    def get_asteroid_feed(self, start_date, end_date):
        url = f"{self.base_url}/feed"
        params = {
            'start_date': start_date,
            'end_date': end_date,
            'api_key': self.api_key
        }
        response = requests.get(url, params=params)
        return response.json()

    def get_asteroid_lookup(self, asteroid_id):
        url = f"{self.base_url}/neo/{asteroid_id}"
        params = {'api_key': self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    def browse_asteroids(self):
        url = f"{self.base_url}/neo/browse"
        params = {'api_key': self.api_key}
        response = requests.get(url, params=params)
        return response.json()
    def query_asteroids(self, asteroids, min_diameter=None, max_diameter=None, close_approach_date=None):
        """
        Query asteroids based on diameter and close approach date.
        :param asteroids: List of asteroid data.
        :param min_diameter: Minimum diameter in meters.
        :param max_diameter: Maximum diameter in meters.
        :param close_approach_date: Close approach date.
        :return: Filtered list of asteroids.
        """
        filtered_asteroids = []
        for asteroid in asteroids:
            diameter = asteroid.get('estimated_diameter', {}).get('meters', {}).get('estimated_diameter_max', 0)
            approach_date = asteroid.get('close_approach_data', [{}])[0].get('close_approach_date', '')

            if min_diameter and diameter < min_diameter:
                continue
            if max_diameter and diameter > max_diameter:
                continue
            if close_approach_date and approach_date != close_approach_date:
                continue

            filtered_asteroids.append(asteroid)

        return filtered_asteroids
    def get_asteroid_statistics(self, asteroids):
        """
        Get basic statistics about the asteroids.
        :param asteroids: List of asteroid data.
        :return: Dictionary with statistics.
        """
        diameters = [asteroid.get('estimated_diameter', {}).get('meters', {}).get('estimated_diameter_max', 0) for asteroid in asteroids]
        
        return {
            'average_diameter': sum(diameters) / len(diameters) if diameters else 0,
            'max_diameter': max(diameters, default=0),
            'min_diameter': min(diameters, default=0),
            'count': len(diameters)
        }

    def plot_asteroid_diameter_distribution(self, asteroids):
        """
        Plot the distribution of asteroid diameters.
        :param asteroids: List of asteroid data.
        """
        diameters = [asteroid.get('estimated_diameter', {}).get('meters', {}).get('estimated_diameter_max', 0) for asteroid in asteroids]

        plt.figure(figsize=(10, 6))
        plt.hist(diameters, bins=20, color='blue', alpha=0.7)
        plt.title('Asteroid Diameter Distribution')
        plt.xlabel('Diameter (meters)')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    def analyze_potential_hazards(self, asteroids):
        """
        Analyze and count potential hazards.
        :param asteroids: List of asteroid data.
        :return: Count of potentially hazardous asteroids.
        """
        hazardous = [asteroid for asteroid in asteroids if asteroid.get('is_potentially_hazardous_asteroid', False)]
        return len(hazardous)
