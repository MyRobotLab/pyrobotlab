
#define MRLCOMM_VERSION         32

// serial protocol functions
#define MAGIC_NUMBER            170 // 10101010

// ----- MRLCOMM FUNCTION GENERATED INTERFACE BEGIN -----------
///// INO GENERATED DEFINITION BEGIN //////
// {publishMRLCommError Integer} 
#define PUBLISH_MRLCOMM_ERROR    1
// {getVersion} 
#define GET_VERSION   2
// {publishVersion Integer} 
#define PUBLISH_VERSION   3
// {analogReadPollingStart Integer} 
#define ANALOG_READ_POLLING_START   4
// {analogReadPollingStop Integer} 
#define ANALOG_READ_POLLING_STOP    5
// {analogWrite Integer Integer} 
#define ANALOG_WRITE    6
// {digitalReadPollingStart Integer} 
#define DIGITAL_READ_POLLING_START    7
// {digitalReadPollingStop Integer} 
#define DIGITAL_READ_POLLING_STOP   8
// {digitalWrite Integer Integer} 
#define DIGITAL_WRITE   9
// {motorAttach Motor} 
#define MOTOR_ATTACH    10
// {motorDetach Motor} 
#define MOTOR_DETACH    11
// {motorMove Motor} 
#define MOTOR_MOVE    12
// {motorMoveTo Motor} 
#define MOTOR_MOVE_TO   13
// {motorReset Motor} 
#define MOTOR_RESET   14
// {motorStop Motor} 
#define MOTOR_STOP    15
// {pinMode Integer Integer} 
#define PIN_MODE    16
// {publishCustomMsg Object[]} 
#define PUBLISH_CUSTOM_MSG    17
// {publishLoadTimingEvent Long} 
#define PUBLISH_LOAD_TIMING_EVENT   18
// {publishPin Pin} 
#define PUBLISH_PIN   19
// {publishPulse Long} 
#define PUBLISH_PULSE   20
// {publishPulseStop Integer} 
#define PUBLISH_PULSE_STOP    21
// {publishSensorData Object} 
#define PUBLISH_SENSOR_DATA   22
// {publishServoEvent Integer} 
#define PUBLISH_SERVO_EVENT   23
// {publishTrigger Pin} 
#define PUBLISH_TRIGGER   24
// {pulse int int int int} 
#define PULSE   25
// {pulseStop} 
#define PULSE_STOP    26
// {sensorAttach SensorDataSink} 
#define SENSOR_ATTACH   27
// {sensorPollingStart String int} 
#define SENSOR_POLLING_START    28
// {sensorPollingStop String} 
#define SENSOR_POLLING_STOP   29
// {servoAttach Servo Integer} 
#define SERVO_ATTACH    30
// {servoDetach Servo} 
#define SERVO_DETACH    31
// {servoEventsEnabled Servo} 
#define SERVO_EVENTS_ENABLED    32
// {servoSweepStart Servo} 
#define SERVO_SWEEP_START   33
// {servoSweepStop Servo} 
#define SERVO_SWEEP_STOP    34
// {servoWrite Servo} 
#define SERVO_WRITE   35
// {servoWriteMicroseconds Servo} 
#define SERVO_WRITE_MICROSECONDS    36
// {setDebounce int} 
#define SET_DEBOUNCE    37
// {setDigitalTriggerOnly Boolean} 
#define SET_DIGITAL_TRIGGER_ONLY    38
// {setLoadTimingEnabled boolean} 
#define SET_LOAD_TIMING_ENABLED   39
// {setPWMFrequency Integer Integer} 
#define SET_PWMFREQUENCY    40
// {setSampleRate int} 
#define SET_SAMPLE_RATE   41
// {setSerialRate int} 
#define SET_SERIAL_RATE   42
// {setServoSpeed Servo} 
#define SET_SERVO_SPEED   43
// {setTrigger int int int} 
#define SET_TRIGGER   44
// {softReset} 
#define SOFT_RESET    45
///// INO GENERATED DEFINITION END //////

// ----- MRLCOMM FUNCTION GENERATED INTERFACE END -----------
// Start of Adafruit16CServoDriver defines
#define AF_BEGIN 50
#define AF_SET_PWM_FREQ 51
#define AF_SET_PWM 52
#define AF_SET_SERVO 53

#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)
#define PCA9685_MODE1 0x0
#define PCA9685_PRESCALE 0xFE
#define LED0_ON_L 0x6
// End of Adafruit16CServoDriver defines

// TODO - UNIONS !!!! - all unions begin with type

// ------ non generated types begin ------
// FIXME - all freeform types need to be in Java ! - all should be part
// of the generator !!!

// ------ stepper types ------
#define STEPPER_TYPE_SIMPLE       1

// ------ stepper event types ------
#define STEPPER_EVENT_STOP        1
#define STEPPER_EVENT_STEP        2

// ------ stepper event types ------
#define  SERVO_EVENT_STOPPED      1
#define  SERVO_EVENT_POSITION_UPDATE  2

// ------ error types ------
#define ERROR_SERIAL          1
#define ERROR_UNKOWN_CMD        2
#define ERROR_ALREADY_EXISTS      3
#define ERROR_DOES_NOT_EXIST      4
#define ERROR_UNKOWN_SENSOR     5


// ------ sensor types ------
// refer to - org.myrobotlab.service.interfaces.SensorDataSink
#define SENSOR_TYPE_PIN            0
#define SENSOR_TYPE_ULTRASONIC       1
#define SENSOR_TYPE_PULSE          2

#define CUSTOM_MSG            50

// need a method to identify type of board
// http://forum.arduino.cc/index.php?topic=100557.0

#define COMMUNICATION_RESET    252
#define NOP            255

// ----------  MRLCOMM FUNCTION INTERFACE END -----------

// MAX definitions
// MAX_SERVOS defined by boardtype/library
// TODO - BOARD IDENTIFICATION - PIN IDENTIFICATION
// #define NUM_DIGITAL_PINS            20
// #define NUM_ANALOG_INPUTS           6

//#define SENSORS_MAX  NUM_DIGITAL_PINS // this is max number of pins (analog included)
#define SENSORS_MAX  20 // TODO: Setting to value larger than 32 causes TX/RX errors in MRL. (Make sensor loop faster to fix.)
#define DIGITAL_PIN_COUNT

// ECHO FINITE STATE MACHINE
#define ECHO_STATE_START 1
#define ECHO_STATE_TRIG_PULSE_BEGIN 2
#define ECHO_STATE_TRIG_PULSE_END 3
#define ECHO_STATE_MIN_PAUSE_PRE_LISTENING 4
#define ECHO_STATE_LISTENING 5
#define ECHO_STATE_GOOD_RANGE 6
#define ECHO_STATE_TIMEOUT  7

#define SENSOR_TYPE_ANALOG_PIN_READER 0

// FIXME FIXME FIXME
// -- FIXME - modified by board type BEGIN --
// Need Arduino to do a hardware abstraction layer
// https://code.google.com/p/arduino/issues/detail?id=59
// AHAAA !! - many defintions in - pins_arduino.h !!!
// Need a "board" identifier at least !!!

// #define MAX_SERVOS 48 - is defined @ compile time !!

#define ARDUINO_TYPE_INT 16; // :) type identifier - not size - but what the hell ;)

/*
* TODO - CRC for last byte
* getCommand - retrieves a command message
* inbound and outbound messages are the same format, the following represents a basic message
* format
*
* MAGIC_NUMBER|NUM_BYTES|FUNCTION|DATA0|DATA1|....|DATA(N)
*              NUM_BYTES - is the number of bytes after NUM_BYTES to the end
*
*/

int msgSize = 0; // the NUM_BYTES of current message

unsigned int debounceDelay = 50; // in ms
byte msgBuf[64];

unsigned long loopCount = 0;
unsigned long lastMicros = 0;
int byteCount = 0;
unsigned char newByte = 0;
unsigned char ioCmd[64];  // message buffer for all inbound messages
int readValue;

// FIXME - normalize with sampleRate ..
int loadTimingModulus = 1000;

boolean loadTimingEnabled = false;
unsigned long loadTime = 0;
// TODO - avg load time

unsigned int sampleRate = 1; // 1 - 65,535 modulus of the loopcount - allowing you to sample less


/*
 *  This sketch demonstrates how to set up a simple HTTP-like server.
 *  The server will set a GPIO pin depending on the request
 *    http://server_ip/gpio/0 will set the GPIO2 low,
 *    http://server_ip/gpio/1 will set the GPIO2 high
 *  server_ip is the IP address of the ESP8266 module, will be 
 *  printed to Serial when the module is connected.
 */

#include <ESP8266WiFi.h>

const char* ssid = "............";
const char* password = "...........";

// Create an instance of the server
// specify the port to listen on as an argument
WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  delay(10);

  // prepare GPIO2
  pinMode(2, OUTPUT);
  digitalWrite(2, 0);
  
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
  
  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());
}

void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }

  while(client.status() != CLOSED){
    ++loopCount;

  //  Serial.print("HERE 1 ");

  if (getCommand(client))
  {

    Serial.print("METHOD ");
    Serial.print(ioCmd[0]);
    Serial.println("");
   
    switch (ioCmd[0])
    {

        case GET_VERSION: 
      {
        Serial.print("GET_VERSION ");
        client.write(MAGIC_NUMBER);
        client.write(2); // size
        client.write(PUBLISH_VERSION);
        client.write((byte)MRLCOMM_VERSION);
        break;
      } // GET_VERSION


      // === system pass through begin ===
    case DIGITAL_WRITE: 
      {
        digitalWrite(ioCmd[1], ioCmd[2]);
        break; 
      } // DIGITAL_WRITE

    case ANALOG_WRITE: 
      {
        analogWrite(ioCmd[1], ioCmd[2]);
        break; 
      } // ANALOG_WRITE

    case PIN_MODE: 
      {
        pinMode(ioCmd[1], ioCmd[2]);
        break; 
      } // PIN_MODE
  default: {
      sendError(ERROR_UNKOWN_SENSOR);
      break;
         }
    }

  // reset buffer
  memset(ioCmd, 0, sizeof(ioCmd));
  byteCount = 0;


  }  // if getCommand()


  // FIXME - fix overflow with getDiff() method !!!
  unsigned long now = micros();
  loadTime = now - lastMicros; // avg outside
  lastMicros = now;

  // report load time
  if (loadTimingEnabled && (loopCount%loadTimingModulus == 0)) {

    // send it
    Serial.write(MAGIC_NUMBER);
    Serial.write(5); // size 1 FN + 4 bytes of unsigned long
    Serial.write(PUBLISH_LOAD_TIMING_EVENT);
    // write the long value out
    Serial.write((byte)(loadTime >> 24));
    Serial.write((byte)(loadTime >> 16));
    Serial.write((byte)(loadTime >> 8));
    Serial.write((byte)loadTime & 0xff);
  }

  } // while(client)

  Serial.println("");
  Serial.println("Client disonnected");

  // The client will actually be disconnected 
  // when the function returns and 'client' object is detroyed
}

// ====================== MrlComm Begin ======================

//===custom msg interface end===

// void sendServoEvent(servo_type& s, int eventType);
// unsigned long getUltrasonicRange(pin_type& pin);
// void sendMsg ( int num, ... );


boolean getCommand(WiFiClient& client) {
  // handle serial data begin
  int bytesAvailable = client.available();
//  Serial.print("BYTES AVAIL ");
//  Serial.print(bytesAvailable);
//  Serial.println("");
  
  if (bytesAvailable > 0) {
    // now we should loop over the available bytes .. not just read one by one.
    for (int i = 0 ; i < bytesAvailable; i++) {
      // read the incoming byte:
      newByte = client.read();
      ++byteCount;

    Serial.print(" cnt ");
      Serial.print(byteCount);
      Serial.print(" byte ");
      Serial.print(newByte);
      Serial.println("");

      // checking first byte - beginning of message?
      if (byteCount == 1 && newByte != MAGIC_NUMBER) {
        sendError(ERROR_SERIAL);
        // reset - try again
        byteCount = 0;
        // return false;
      }

      if (byteCount == 2) {
        // get the size of message
        // todo check msg < 64 (MAX_MSG_SIZE)
        if (newByte > 64){
          // TODO - send error back
          byteCount = 0;
          continue; // GroG - I guess  we continue now vs return false on error conditions? 
        }
        msgSize = newByte;
      }

      if (byteCount > 2) {
        // fill in msg data - (2) headbytes -1 (offset)
        ioCmd[byteCount - 3] = newByte;
      }

      // if received header + msg
      if (byteCount == 2 + msgSize) {
        // we've reach the end of the command, just return true .. we've got it
        return true;
      }
    }
  } // if Serial.available
  // we only partially read a command.  (or nothing at all.)
  return false;
}


void sendError(int type) {
  Serial.write(MAGIC_NUMBER);
  Serial.write(2); // size = 1 FN + 1 TYPE
  Serial.write(PUBLISH_MRLCOMM_ERROR);
  Serial.write(type);
}

