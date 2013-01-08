/*
Lights controller. If
 */
boolean one = false;
boolean two = false;
boolean three = false;

void setup() {                
  // initialize the digital pin as an output.
  // Pin 13 has an LED connected on most Arduino boards:
  pinMode(10, OUTPUT);  
  pinMode(12, OUTPUT);  
  pinMode(11, OUTPUT);


  Serial.begin(9600);
}

void loop() {


  // send data only when you receive data:
  if (Serial.available() > 0) {
    // we receive a char representing an integer. let's converto to int
    int incomingData = Serial.read();
    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingData);
  

    switch (incomingData){

    case 48:   
      digitalWrite(10, LOW);   // set all the LED off
      digitalWrite(11, LOW);
      digitalWrite(12, LOW);

      one = false;
      two = false;
      three = false;


      break;



    case 49:
      if (!one){
        digitalWrite(10, HIGH);   
        one = true;
        break;
      }
      else{
        digitalWrite(10, LOW);   
        one= false;
        break;
      }
      
    case 50:
      if (!two){
        digitalWrite(11, HIGH);  
        two=true;  
        break;
      }
      else{
        digitalWrite(11, LOW); 
        two=false;
        break;
      }

    case 51:
      if(!three){
        digitalWrite(12, HIGH);
        three=true;
        break;
      }
      else{
        digitalWrite(12, LOW);
        three =  false;  
        break;
      }
      
    case 52:
     digitalWrite(10, HIGH);   // set all the LED on
      digitalWrite(11, HIGH);
      digitalWrite(12, HIGH);

      one = true;
      two = true;
      three = true;

      break;


    }
  }
} 









