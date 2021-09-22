#include <OneWire.h>
#include <DallasTemperature.h>

#define BUS 2

OneWire oneWire(BUS);

DallasTemparature sensors(&oneWire);

void setup(void){
    Serial.begin(9600);
    Serial.println("Dallas Temp demo");
    sensors.begin();
}

void loop(void){
    sensors.requestTemperatures();
    Serial.print("Got temperature: ");

    Serial.print(sensors.getTempCByIndex(0));
}