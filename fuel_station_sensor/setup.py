from setuptools import setup

setup(
    name="fuel_station_sensor",
    version="1.0",
    description="Custom Home Assistant sensor for fuel station data",
    author="Max Mazzeschi",
    author_email="max.mazzeschi@gmail.com",
    packages=["custom_components.fuel_station_sensor"],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
