#include<LPC21xx.h>
void delay()
{
	unsigned int i;
	for(i=0; i<10000; i++);
}

//TW11- Relay

int m(){
	PINSEL0 = 0x00000000;
	IO0DIR = 0x00000400;
	PINSEL0 = 0x00000400;
	while(1){
	
		IO0SET = 0x00000400;
		delay();
		IO0CLR = 0x00000400;
		delay();		
	}
	
}

//TW10 - ADC interface for tringular wave
unsigned int i;
unsigned long int temp;
int ma(){
	PINSEL0 = 0x00000000;
	PINSEL1 = 0x00000000;
	IO0DIR = 0xffffffff;
	while(1){
		for(i=0; i!=255; i++){
			temp = i;
			temp = temp << 16;
			IO0PIN = temp;
		}
		
		for(i=255; i!=0; i--){
			temp = i;
			temp = temp << 16;
			IO0PIN = temp;
		}		
	}
}

//TW9 - ADC interface for square wave

int mai(){
	PINSEL0 = 0x00000000;
	PINSEL1 = 0x00000000;
	IO0DIR = 0xffffffff;
	while(1){
		IO0PIN = 0xffffffff;
		delay();
		IO0PIN = 0x00000000;
		delay();
	}
}


//TW8-8 bit counter on p0.16 to p0.23
unsigned int count;
int main(){
	unsigned int comp =0;
	PINSEL1 = 0x00000000;
	IO0DIR = 0xffffffff;
	while(1){
		for(count=0; count<=0xff; count++){
			comp = (~count);
			comp = comp & 0x000000ff;
			IO0PIN = comp << 16;
			delay();
			
		}
	}
}



//TW7-blink light from p0.13 to p0.23

int tw7(){
	PINSEL1 = 0x00000000; //p016-p0-32 as GPIO
	IO0DIR = 0xffffffff; //p0 as output
	while(1){
		IO0SET = 0x00ff0000;
		delay();
		IO0CLR = 0x00ff0000;
		delay();
	}
	
}




