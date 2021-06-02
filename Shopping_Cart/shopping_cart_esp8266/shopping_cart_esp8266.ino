static const uint8_t D0   = 16;
static const uint8_t D1   = 5;
static const uint8_t D2   = 4;
static const uint8_t D3   = 0;
static const uint8_t D4   = 2;
static const uint8_t D5   = 14;
static const uint8_t D6   = 12;
static const uint8_t D7   = 13;
static const uint8_t D8   = 15;


#include <ESP8266WiFi.h>
#include <Firebase_ESP_Client.h>
#include "Button2.h";
#include <SPI.h>
#include <MFRC522.h>
#include <ArduinoJson.h>


/* 1. Define the WiFi credentials */
#define WIFI_SSID "Nirmalyam"
#define WIFI_PASSWORD "@# colonel 98 #@"

/* 2. Define the Firebase project host name and API Key */
#define FIREBASE_HOST "authenticatorapp-fbaa2.firebaseapp.com"

#define API_KEY "AIzaSyB9S7dEkaV0o9rBdPRy_dTVaatPEHXFncc"

/* 3. Define the project ID */
#define FIREBASE_PROJECT_ID "authenticatorapp-fbaa2"

/* 4. Define the user Email and password that alreadey registerd or added in your project */
#define USER_EMAIL "sscproject0123@gmail.com"
#define USER_PASSWORD "123456"

/* 5. Define the SS and RST pin */
#define SS_PIN D4 
#define RST_PIN D8 

/* 6. Define the pin used to take button input */
#define BUTTON_PIN  D2

Button2 button = Button2(BUTTON_PIN);
StaticJsonDocument<384> doc;

//Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

unsigned long dataMillis = 0;
unsigned long dataMillisLock = 0;
int isLocked = 0;
int count = 0;



MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
int statuss = 0;
int out = 0;
void setup() 
{
  pinMode(D1, OUTPUT);
  pinMode(D0, OUTPUT);
  digitalWrite(D1, HIGH);
  digitalWrite(D0, LOW);
  Serial.begin(9600);   // Initiate a serial communication
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
  

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    Serial.print("Connecting to Wi-Fi");
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(300);
    }
    Serial.println();
    Serial.print("Connected with IP: ");
    Serial.println(WiFi.localIP());
    Serial.println();

    /* Assign the project host and api key (required) */
    config.host = FIREBASE_HOST;
    config.api_key = API_KEY;

    /* Assign the user sign in credentials */
    auth.user.email = USER_EMAIL;
    auth.user.password = USER_PASSWORD;

    Firebase.begin(&config, &auth);
    Firebase.reconnectWiFi(true);
    fbdo.setBSSLBufferSize(1024, 1024);

    button.setTapHandler(tap);
}
void loop() 
{
  digitalWrite(D1, HIGH);   
  button.loop();
  if (millis() - dataMillisLock > 30000 && isLocked > 0){
    digitalWrite(D0, LOW);
    isLocked=0;
    Serial.print("Pin lowed, lock locked");
  }
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  Serial.println();
  Serial.print(" UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     //content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  content.toUpperCase();
  Serial.println();
  if (content.substring(1) != "") 
  {
    digitalWrite(D1, LOW); 
    writeToFirebase(content);
  } 
} 

void writeToFirebase(String x){
  if (millis() - dataMillis > 100 || dataMillis == 0)
    {
        dataMillis = millis();

        String content;
        FirebaseJson js;

        String documentPath = "cart001/products/itemsCollections/item" + String(count);

        js.set("fields/item_name/stringValue",String(x));

        js.toString(content);

        Serial.println("------------------------------------");
        Serial.println("Create a document...");

        if (Firebase.Firestore.createDocument(&fbdo, FIREBASE_PROJECT_ID, "" /* databaseId can be (default) or empty */, documentPath.c_str(), content.c_str()))
        {
            digitalWrite(D1, HIGH); 
            Serial.println("PASSED");
            Serial.println("------------------------------------");
            Serial.println(fbdo.payload());
            Serial.println("------------------------------------");
            Serial.println();
            count++;
        }
        else
        {
            digitalWrite(D1, HIGH);
            Serial.println("FAILED");
            Serial.println("REASON: " + fbdo.errorReason());
            Serial.println("------------------------------------");
            Serial.println();
        }
    }
}

void tap(Button2& btn) {
    String documentPath = "cart001/billing";
    String mask = "status";
    String jsonInput;

    Serial.println("------------------------------------");
    Serial.println("Get a document...");

    if (Firebase.Firestore.getDocument(&fbdo, FIREBASE_PROJECT_ID, "", documentPath.c_str(), mask.c_str()))
        {
            Serial.println("PASSED");
            Serial.println("------------------------------------");
            jsonInput = fbdo.payload();
            Serial.println("returning value"); 
            DeserializationError error = deserializeJson(doc, jsonInput);
            if (error) {
              Serial.print(F("deserializeJson() failed: "));
              Serial.println(error.f_str());
              isLocked=0;
            }
            String testingValue = doc["fields"]["status"]["stringValue"];
            if (testingValue.equals("false")){
              Serial.println(testingValue);
              isLocked=0;
            }else{
              Serial.println(testingValue);
              digitalWrite(D0, HIGH);
              dataMillisLock = millis();
              isLocked=1;
              count = 0;
              digitalWrite(D1, LOW); 
              delay(100);
              digitalWrite(D1, HIGH);
              delay(50);  
              digitalWrite(D1, LOW); 
              delay(100);
              digitalWrite(D1, HIGH);
              delay(50);  
              digitalWrite(D1, LOW); 
              delay(100);
              digitalWrite(D1, HIGH);  
            }
            Serial.println("------------------------------------");
            Serial.println();
        }
    else
        {
            isLocked=0;
            digitalWrite(D0, LOW);
            Serial.println("FAILED");
            Serial.println("REASON: " + fbdo.errorReason());
            Serial.println("------------------------------------");
            Serial.println();
        }
}
