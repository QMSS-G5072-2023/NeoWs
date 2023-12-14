# NeoWsClient Python Package

## Overview

`NeoWsClient` is a Python client for interacting with NASA's Near Earth Object Web Service (NeoWs). It allows users to retrieve and analyze data about near-Earth asteroids, including their close approach data, size, and potential hazards.

## Links to data sources / API etc

* API Portal / Home Page: [NASA API](https://api.nasa.gov/#browseAPI)
* Data Source: [NASA JPL Asteroid Team](http://neo.jpl.nasa.gov/)

## Installation

Explain how users can install your package. For instance, if it's hosted on PyPi, provide the pip installation command.

```bash
pip install neows_client
```

## Usage

Below are the functionalities provided by the `NeoWsClient` class:

### Initialization

```python
from neows_client import NeoWsClient

client = NeoWsClient(api_key='YOUR_API_KEY')
```

### Getting Asteroid Feed

Retrieve a list of asteroids based on their closest approach date to Earth.

```python
asteroids = client.get_asteroid_feed(start_date='2023-01-01', end_date='2023-01-08')
```

### Looking Up a Specific Asteroid

Retrieve detailed data about a specific asteroid using its NASA JPL small body ID.

```python
asteroid_data = client.get_asteroid_lookup(asteroid_id='3542519')
```

### Browsing Asteroids

Browse the overall dataset of known asteroids.

```python
all_asteroids = client.browse_asteroids()
```

### Querying Asteroids

Filter asteroids based on criteria such as diameter and potential hazard:

```python
client = NeoWsClient(API_KEY)
data = client.get_asteroid_feed('2023-01-01', '2023-01-08')

# Flatten the data, as it's nested under dates
asteroids = [asteroid for date in data['near_earth_objects'] for asteroid in data['near_earth_objects'][date]]
filtered_asteroids = client.query_asteroids(asteroids, 100)
```

### Analyzing Asteroids

Get statistical information about the asteroids:

```python
stats = client.get_asteroid_statistics(filtered_asteroids)
print(stats)
```

### Visualizing Asteroid Distribution

Visualize the distribution of asteroid diameters:

```python
client.plot_asteroid_diameter_distribution(filtered_asteroids)
```

### Analyzing Potential Hazards

Analyze the number of potentially hazardous asteroids:

```python
hazard_count = client.analyze_potential_hazards(filtered_asteroids)
print(f"Number of potentially hazardous asteroids: {hazard_count}")
```

## How to test this package

```python
cd src
python -m unittest tests/test_api.py 
```



## License

This project is based on the GPL v3 license
