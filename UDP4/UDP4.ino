#include <Ethernet.h>
#include <EthernetUdp.h>
#include <Wire.h>
#include <TEA5767N.h>

///////////////////////////////////////////

byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
IPAddress ArduinoIP(192, 168, 10, 23);
IPAddress ArduinoDNS(192, 168, 10, 1);
IPAddress ArduinoGateway(192, 168, 10, 254);
IPAddress ArduinoMask(255, 255, 255, 0);

IPAddress ServerIP(192, 168, 10, 10);
unsigned int localPort = 5050;
EthernetUDP Udp;

TEA5767N radio = TEA5767N();
float frequency = 102.5;

char packetBuffer[UDP_TX_PACKET_MAX_SIZE];

void(* resetFunc) (void) = 0;
///////////////////////////////////////////

void setup() {
  Serial.begin(9600);

  Ethernet.begin(mac, ArduinoIP, ArduinoDNS, ArduinoGateway, ArduinoMask);
  Udp.begin(localPort);
 
  radio.selectFrequency(frequency);
  delay(5000);

 }

///////////////////////////////////////////

void loop() {
    byte b[6];
   
    if(Serial.available()){
      float Newfrequency = Serial.parseFloat();
      if(Newfrequency > 76 && Newfrequency < 108){
        delay(1);
        radio.selectFrequency(Newfrequency);
      }
    }
    

 
  Serial.print("Station selected: ");
  Serial.print(radio.readFrequencyInMHz(),1);
  Serial.println(" MHz");
  
  memset(b, 0, 6);
  for (int i = 0; i < 6; i++) {
    b[i] = radio.getSignalLevel();
    Serial.print(b[i]);
    Serial.print(",");
    delay(1);
  }
 
  sendUDP(b);
  delay(1000);

  int packetSize = Udp.parsePacket();
  if(packetSize){  
    Udp.read(packetBuffer,UDP_TX_PACKET_MAX_SIZE);  
    if(packetBuffer[0] == (char)'F' && packetBuffer[1] == (char)'q' && packetBuffer[2] == (char)':'){
      radio.selectFrequency(convertToF(packetBuffer));
    }
    if(packetBuffer[0] == (char)'R' && packetBuffer[1] == (char)'S' && packetBuffer[2] == (char)'T'){
      Serial.println("Reset");
      delay(5000);
      resetFunc();
    }
  }


}

///////////////////////////////////////////


void sendUDP(byte data[]) {
  Udp.beginPacket(ServerIP, 50005);
  Udp.write(data,6);
  Udp.endPacket();
}


float convertToF(char packetBuffer[]){
     float a;

      if(packetBuffer[3] == '4'){
        char nextFrequency[] = {packetBuffer[4], packetBuffer[5], packetBuffer[6], packetBuffer[7]};
        a = float(atoi(nextFrequency))/10;
        return a;
      }else if(packetBuffer[3] == '3'){
        char nextFrequency[] = {packetBuffer[4], packetBuffer[5], packetBuffer[6]};
        a = float(atoi(nextFrequency))/10;
        return a;
        }
  }
