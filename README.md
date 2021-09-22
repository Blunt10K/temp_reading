# Temperature reading project

## Goals
This project is designed to measure temperature and log the data.
When enough data is collected, it is possible to visualise it. With breakdowns by time of day, month, season, year, etc.

This data can then be used to develop a smart temperature controller for a room (or multiple rooms with a network of sensors). This will be a further extension of this project.


### Hardware used:

#### - Aruduino Uno
#### - KY-001 temperature module
#### - Raspberry Pi 4  

### Library dependencies:

#### - OneWire (Arduino)
#### - DallasTemperatures (Arduino)
#### - PySerial (Raspberry Pi)

## Measurements
Temperature readings are logged at the top of each minute. 

Every hour, the temperature data is saved to a log file.
