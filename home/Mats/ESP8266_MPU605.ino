/*
 *  This sketch demonstrates how to get the parameters from a http POST request from an ESP8266-01
    https://www.youtube.com/watch?v=Edbxyl2BhyU
    https://www.youtube.com/watch?v=hP3xQtrRMmQ&t=33s
    It also contains code to write and read data from an i2c device
    In this case a MPU-6050 accelerometer and gyro
    This sketch is just a very basic prototype to help people get started with the ESP8266 
 */

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ArduinoJson.h>
#include<Wire.h>
#include<stdlib.h>

ESP8266WebServer server;

const char* ssid = "your-wifi-router-ssid";
const char* password = "your.wifi-router-password";
const int MPU_addr=0x68;  // I2C address of the MPU-6050
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
float Temp;

const String AccXLabel =  "\"AccX\":";
const String AccYLabel =  "\"AccY\":";
const String AccZLabel =  "\"AccZ\":";
const String GyroXLabel = "\"GyroX\":";
const String GyroYLabel = "\"GyroY\":";
const String GyroZLabel = "\"GyroZ\":";
const String TempLabel =  "\"Temperature\":";

String pinStatus = "on";

void setup() {
  Serial.begin(115200);
  delay(10);
  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  
  // Print the IP address
  Serial.println(WiFi.localIP());

  // Setup the different response methods
  server.on("/",[](){server.send(200, "text/html", "Welcome to <b>ESP8266</b> and the <b>MPU-6050</b>");});
  server.on("/toggle",toggleLED);
  server.on("/pantilt",setPanTilt);
  server.on("/getMPU6050",getMPU6050);
 
  // Initiate the i2c Bus and wake the MPU-6050 up from sleep mode
  Wire.begin(0,2);
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  
  // Start the server
  server.begin();
  Serial.println("Server started");
}

void loop() {

  server.handleClient();
}
void toggleLED()
{
    if (pinStatus == "on"){
      pinStatus = "off";
    }
    else {
      pinStatus = "on";
    }
    server.send(200, "text/plain", "Toggling LED " + pinStatus);
  // 204 = Empty response
  // server.send("204","");   
}

void setPanTilt()
{
   String data = server.arg("plain");
   StaticJsonBuffer<200> jBuffer;
   JsonObject& jObject = jBuffer.parseObject(data);
   String pan = jObject["pan"];  
   String tilt = jObject["tilt"];  
   server.send(200, "text/plain", "Pan = " + pan + " Tilt = " + tilt);
}

void getMPU6050()
{
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  Tmp=Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
  GyX=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

  float Temp;
  Temp = Tmp/340.00+36.53;
  char Temperature[5];
  dtostrf(Temp,4,1,Temperature);

  String AccelX = String(AcX, DEC);
  String AccelY = String(AcY, DEC);
  String AccelZ = String(AcZ, DEC);

  String GyroX = String(GyX, DEC);
  String GyroY = String(GyY, DEC);
  String GyroZ = String(GyZ, DEC);

  String message = "{" +
                   TempLabel + Temperature + "," +
                   AccXLabel + AccelX + "," +
                   AccYLabel + AccelY + "," +
                   AccZLabel + AccelZ + "," +
                   GyroXLabel + GyroX + "," +
                   GyroYLabel + GyroY + "," +
                   GyroZLabel + GyroZ + 
                   "}";
                                 
  server.send(200, "application/json", message);
}
