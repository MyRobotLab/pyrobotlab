#include<stdlib.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 8
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

#define SSID "YOUR SSID  HERE"
#define PASS "YOUR PASSWORD HERE"
#define IP "184.106.153.149" // thingspeak.com
String GET = "GET /update?key=YOURTHINGSPEAKAPIKEY&field2=";


void setup()
{
  Serial.begin(115200);
  sensors.begin();
  Serial.println("AT");
  delay(5000);
  if(Serial.find("OK")){
    connectWiFi();
  }
}

void loop(){
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  //tempC = DallasTemperature::toFahrenheit(tempC);
  char buffer[10];
  String tempF = dtostrf(tempC, 4, 1, buffer);
  updateTemp(tempF);
  //Serial.println(tempF);
  delay(60000);
}

void updateTemp(String tempF){
  String cmd = "AT+CIPSTART=\"TCP\",\"";
  cmd += IP;
  cmd += "\",80";
  Serial.println(cmd);
  delay(2000);
  if(Serial.find("Error")){
    return;
  }
  cmd = GET;
  cmd += tempF;
  cmd += "\r\n";
  Serial.print("AT+CIPSEND=");
  Serial.println(cmd.length());
  //delay(1000);
  if(Serial.find(">")){
    Serial.print(cmd);
  }else{
    Serial.println("AT+CIPCLOSE");
  }
}


boolean connectWiFi(){
  Serial.println("AT+CWMODE=3");
  delay(2000);
  String cmd="AT+CWJAP=\"";
  cmd+=SSID;
  cmd+="\",\"";
  cmd+=PASS;
  cmd+="\"";
  Serial.println(cmd);
  delay(5000);
  if(Serial.find("OK")){
    return true;
  }else{
    return false;
  }
}

After managing to send data to web, I tried to implement a webserver which can post data to my network, from where I can monitor that incoming wifi stream with my browser... Found a wonderful sketch on the net which is written by Ray Wang to test wifi sensor node by ESP8266 unit.... works like a charm... I can monitor all my analog ports with this sketch... easy to be modified to one's needs for other ports... The sketch enables the wifi unit, connects to your wifi network via WPA2-PSK, gets an IP adress from the router and you can monitor your sensor node in your beowser using the unit's IP at port 8080...

/* ====== ESP8266 Demo ======
 *   Print out analog values
 * ==========================
 *
 * Change SSID and PASS to match your WiFi settings.
 * The IP address is displayed to soft serial upon successful connection.
 *
 * Ray Wang @ Rayshobby LLC
 * http://rayshobby.net/?p=9734
 */

// comment this part out if not using LCD debug
#include <SoftwareSerial.h>
SoftwareSerial dbg(7, 8); // using pin 7, 8 for software serial

enum {WIFI_ERROR_NONE=0, WIFI_ERROR_AT, WIFI_ERROR_RST, WIFI_ERROR_SSIDPWD, WIFI_ERROR_SERVER, WIFI_ERROR_UNKNOWN};

#define BUFFER_SIZE 128

#define SSID  "YOURSSID"   // change this to match your WiFi SSID
#define PASS  "YOURPASS"  // change this to match your WiFi password
#define PORT  "8080"      // using port 8080 by default

char buffer[BUFFER_SIZE];

void setup() {

  Serial.begin(115200);
  Serial.setTimeout(5000);

  dbg.begin(9600);
  dbg.println("begin.");

  byte err = setupWiFi();
  if (err) {
    // error, print error code
    dbg.print("setup error:");
    dbg.println((int)err);
  } else {
    // success, print IP
    dbg.print("ip addr:");
    char *ip = getIP();
    if (ip) {
      dbg.println(ip);
    }
    else {
      dbg.println("none");
    }
    maxTimeout();
  }
}

bool maxTimeout() {
  // send AT command
  Serial.println("AT+CIPSTO=0");
  if(Serial.find("OK")) {
    return true;
  } else {
    return false;
  }
}

char* getIP() {
  // send AT command
  Serial.println("AT+CIFSR");

  // the response from the module is:
  // AT+CIFSR\n\n
  // 192.168.x.x\n
  // so read util \n three times
  Serial.readBytesUntil('\n', buffer, BUFFER_SIZE);
  Serial.readBytesUntil('\n', buffer, BUFFER_SIZE);
  Serial.readBytesUntil('\n', buffer, BUFFER_SIZE);
  buffer[strlen(buffer)-1]=0;
  return buffer;
}

void loop() {
  int ch_id, packet_len;
  char *pb;
  Serial.readBytesUntil('\n', buffer, BUFFER_SIZE);
  if(strncmp(buffer, "+IPD,", 5)==0) {
    // request: +IPD,ch,len:data
    sscanf(buffer+5, "%d,%d", &ch_id, &packet_len);
    if (packet_len > 0) {
      // read serial until packet_len character received
      // start from :
      pb = buffer+5;
      while(*pb!=':') pb++;
      pb++;
      if (strncmp(pb, "GET /", 5) == 0) {
        serve_homepage(ch_id);
      }
    }
  }
}

void serve_homepage(int ch_id) {
  String header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\nRefresh: 5\r\n";

  String content="";
  // output the value of each analog input pin
  for (int analogChannel = 0; analogChannel < 6; analogChannel++) {
    int sensorReading = analogRead(analogChannel);
    content += "analog input ";
    content += analogChannel;
    content += " is ";
    content += sensorReading;
    content += "<br />\n";
  }

  header += "Content-Length:";
  header += (int)(content.length());
  header += "\r\n\r\n";
  Serial.print("AT+CIPSEND=");
  Serial.print(ch_id);
  Serial.print(",");
  Serial.println(header.length()+content.length());
  if (Serial.find(">")) {
    Serial.print(header);
    Serial.print(content);
    delay(20);
  }
  /*Serial.print("AT+CIPCLOSE=");
  Serial.println(ch_id);*/
}

byte setupWiFi() {
  Serial.println("AT");
  if(!Serial.find("OK")) {
    return WIFI_ERROR_AT;
  }
  delay(500);

  // reset WiFi module
  Serial.println("AT+RST");
  if(!Serial.find("ready")) {
    return WIFI_ERROR_RST;
  }
  delay(500);

  // set mode 3
  Serial.print("AT+CWJAP=\"");
  Serial.print(SSID);
  Serial.print("\",\"");
  Serial.print(PASS);
  Serial.println("\"");
  delay(2000);
  if(!Serial.find("OK")) {
    return WIFI_ERROR_SSIDPWD;
  }
  delay(500);

  // start server
  Serial.println("AT+CIPMUX=1");
  if(!Serial.find("OK")){
    return WIFI_ERROR_SERVER;
  }
  delay(500);

  Serial.print("AT+CIPSERVER=1,"); // turn on TCP service
  Serial.println(PORT);
  if(!Serial.find("OK")){
    return WIFI_ERROR_SERVER;
  }
  delay(500);

  return WIFI_ERROR_NONE;
}
