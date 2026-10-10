
#include <WiFi.h>
#include "DHT.h"

// Sensor configuration
#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

// Wi-Fi credentials (optional)
const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

void setup() {
  Serial.begin(115200);
  dht.begin();

  Serial.println("ESP32 IoT Environmental Monitoring");
  Serial.println("----------------------------------");

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi");

  unsigned long startTime = millis();

  while (WiFi.status() != WL_CONNECTED &&
         millis() - startTime < 15000) {
    delay(500);
    Serial.print(".");
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nWi-Fi connected!");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("\nWi-Fi unavailable. Sensor works locally.");
  }
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error reading DHT11 sensor!");
    delay(2000);
    return;
  }

  Serial.println("\nEnvironmental Data");
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  if (temperature >= 35) {
    Serial.println("Alert: High temperature!");
  } else {
    Serial.println("Temperature status: Normal");
  }

  delay(2000);
}
