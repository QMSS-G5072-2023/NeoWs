from setuptools import setup, find_packages

setup(
    name='neows_client',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas' 
    ],
    author='Chicheng Hong',
    author_email='sh4432@columbia.edu',
    description='Python client for accessing the NASA NeoWs API',
    keywords='NASA NeoWs asteroids API client',
    url='https://github.com/QMSS-G5072-2023/NeoWs',  
)

