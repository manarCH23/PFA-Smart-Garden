/*
 * dht11.h
 *
 *  Created on: Oct 16, 2023
 *      Author: Manar
 */

#ifndef INC_DHT11_H_
#define INC_DHT11_H_





typedef struct
{
	float Temperature;
	float Humidity;
}DHT_DataTypedef;


void DHT_GetData (DHT_DataTypedef *DHT_Data);

#endif /* INC_DHT11_H_ */
