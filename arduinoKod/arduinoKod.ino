#include<Servo.h>
Servo cam;
char val;
int gradus=0,grad2;
void setup() {
  Serial.begin(9600);
  cam.attach(13);
}
int ChangeCharToNumber(char val2){
  if(val=='0') return 0;
  if(val=='1') return 1;
  if(val=='2') return 2;
  if(val=='3') return 3;
  if(val=='4') return 4;
  if(val=='5') return 5;
  if(val=='6') return 6;
  if(val=='7') return 7;
  if(val=='8') return 8;
  if(val=='9') return 9;
  }
  
void loop() {
if(Serial.available()){
  val=Serial.read();
  if(val!=' '){
  gradus=gradus*10+ChangeCharToNumber(val);
  }
  else{
  grad2=map(gradus,10,430,130,60);
  gradus=0;  
  }
  
  
  }
  cam.write(grad2);
}
