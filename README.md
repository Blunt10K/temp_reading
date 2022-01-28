# Temperature reading project

## Goals
This project is designed to measure temperature and log the data as part of an indoor climate monitoring system.
When enough data is collected, it is possible to visualise it. With breakdowns by hour, day, month, season, year, etc.

This data can then be used to develop a smart temperature controller for a room (or multiple rooms with a network of sensors). This will be a further extension of this project.


### Hardware used:

#### - Aruduino Uno
#### - KY-001 temperature module
#### - Raspberry Pi 4  

### Library dependencies:

#### - OneWire (Arduino)
#### - DallasTemperatures (Arduino)
#### - PySerial (Raspberry Pi)
#### - 

## Measurements
Temperature readings are logged at the top of each minute and logged into a MySQL database.

## Visualisation
The visualisation is realised in a dashboard developed using Plotly Dash. The dashboard includes live data from the temperature sensor and historical data from the database.
