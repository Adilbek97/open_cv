#include<Servo.h>
Servo cam;
char val,val2;
int gradus=0,grad2;
String value="";
void setup() {
  Serial.begin(9600);
  cam.attach(4);
}
int funk(char val2){
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
    value+=val;
//  gradus=gradus*10+funk(val);
  }
  else{
    if(value[0]=='x'){
      for(int i=1;i<value.length();i++){
        val2=value[i];
        gradus=gradus*10+funk(val2);
        Serial.print(gradus);
//        Serial.print(gradus);
        }
        value="";
      }
    
  grad2=map(gradus,0,530,10,100);
  
  gradus=0;  
  
  }
  }
  cam.write(grad2);
}
