/*
 * dht11.c
 *
 *  Created on: Oct 16, 2023
 *      Author: Manar
 */


#include "dht11.h"

extern TIM_HandleTypeDef htim6;

void delay(uint16_t time){
	 __HAL_TIM_SET_COUNTER(&htim6,0);
	while((__HAL_TIM_GET_COUNTER(&htim6))<0);
}



void SET_Pin_Output(GPIO_TypeDef *GPIOx, uint16_t GPIO_PIN){
	  GPIO_InitTypeDef GPIO_InitStruct = {0};

	 GPIO_InitStruct.Pin = GPIO_PIN;
	  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
	  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
	  HAL_GPIO_Init(GPIOx, &GPIO_InitStruct);

}
void SET_Pin_Input(GPIO_TypeDef *GPIOx, uint16_t GPIO_PIN){
	  GPIO_InitTypeDef GPIO_InitStruct = {0};

	 GPIO_InitStruct.Pin = GPIO_PIN;
	  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
	  GPIO_InitStruct.Pull = GPIO_NOPULL;
	  HAL_GPIO_Init(GPIOx, &GPIO_InitStruct);

}

void dht11_Start(void){
	SET_Pin_Output(DHT_PORT, DHT_PIN);
	HAL_GPIO_WritePin(DHT_PORT,DHT_PIN,0);
	delay(18000);
	HAL_GPIO_WritePin(DHT_PORT,DHT_PIN,1);
	SET_Pin_Input(DHT_PORT, DHT_PIN);

}

uint8_t dht11_response(void){
	uint8_t Response = 0;
		delay (40);
		if (!(HAL_GPIO_ReadPin (DHT_PORT, DHT_PIN)))
		{
			delay (80);
			if ((HAL_GPIO_ReadPin (DHT_PORT, DHT_PIN))) Response = 1;
			else Response = -1;
		}
		while ((HAL_GPIO_ReadPin (DHT_PORT, DHT_PIN)));   // wait for the pin to go low

		return Response;
}
uint8_t DHT_Read (void)
{
	uint8_t i,j;
	for (j=0;j<8;j++)
	{
		while (!(HAL_GPIO_ReadPin (DHT_PORT, DHT_PIN)));   // wait for the pin to go high
		delay (40);   // wait for 40 us
		if (!(HAL_GPIO_ReadPin (DHT_PORT, DHT_PIN)))   // if the pin is low
		{
			i&= ~(1<<(7-j));   // write 0
		}
		else i|= (1<<(7-j));  // if the pin is high, write 1
		while ((HAL_GPIO_ReadPin (DHT_PORT, DHT_PIN)));  // wait for the pin to go low
	}
	return i;
}
 char dht11_data(void){

		dht11_Start();
			presence = dht11_response();
			temp1 = DHT_Read();
			temp2 = DHT_Read();
			rh1 = DHT_Read();
			rh2 = DHT_Read();
			SUM = DHT_Read();
			TEMP = temp1 + temp2;
			RH = rh1 + rh2;
			temperature = (float) TEMP;
			humidity = (float) RH;

 }
