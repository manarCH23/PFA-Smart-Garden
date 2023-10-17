#include <HTTPClient.h>
#include <WiFi.h>

HTTPClient http;

void setup() {
  Serial.begin(115200);
  WiFi.begin("Redmi Note 8", "1234567h1");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  { 
    http.begin("http://192.168.92.182:8000/api/Dht11/"); // Specify the URL
    http.addHeader("Content-Type", "application/json"); // Set the content type

    String data = "From esp"; // Define the variable and assign its value
    String payload = "{\"data\":" + data + "}"; // Concatenate the variable value into the JSON payload

    int httpCode = http.POST(payload); // Make the request

    if (httpCode > 0) { // Check for the returning code
      String response = http.getString();
      Serial.println(response);
    } else {
      Serial.println("Error on HTTP request");
    }

    http.end(); // Free the resources

    delay(1000);
  }
}
