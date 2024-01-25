#!/usr/bin/env python

import decimal

class SensorValue:
    _PREC = 3
    
    @classmethod
    def convert_value(cls, value):
        # convert value to int, then to decimal
        value = int(value)
        # the value we got is temperature * (10 ** PREC),
        # thus divide by (10 ** PREC) to get the actual value
        PREC = cls._PREC
        val = f'{value}.' + '0' * PREC
        dec = decimal.Decimal(val) / (10 ** PREC)
        return dec
    
    def get_raw_value(self):
        raise NotImplementedError("Subclasses must implement get_raw_value method.")
    
    def get_value(self):
        val = self.get_raw_value()
        return self.convert_value(val)

    @property
    def value(self):
        if not hasattr(self, '_value'):
            self._value = self.get_value()
        return self._value


class TemperatureSensor(SensorValue):
    _TEMPLATE = '/sys/class/thermal/thermal_zone{num}/temp'
    
    def __init__(self, sensor_num=0):
        super().__init__()
        sensor_num = int(sensor_num)
        self.sensor = self._TEMPLATE.format(num=sensor_num)

    def get_raw_value(self):
        with open(self.sensor, 'r') as file:
            val = file.readline().strip()
        return val


class MicrophoneLoudnessSensor(SensorValue):
    # Assuming you have a method to get microphone loudness
    def get_raw_value(self):
        # Implement the method to get microphone loudness
        pass


class CameraColorSensor(SensorValue):
    # Assuming you have a method to get camera color
    def get_raw_value(self):
        # Implement the method to get camera color
        pass


class BatteryChargeSensor(SensorValue):
    # Assuming you have a method to get battery charge level
    def get_raw_value(self):
        # Implement the method to get battery charge level
        pass


if __name__ == '__main__':
    # Example usage for temperature sensor
    temperature_sensor = TemperatureSensor()
    temperature_value = temperature_sensor.value
    print(f"Temperature: {temperature_value} Celsius")

    # Example usage for microphone loudness sensor
    microphone_sensor = MicrophoneLoudnessSensor()
    microphone_value = microphone_sensor.value
    print(f"Microphone Loudness: {microphone_value} dB")

    # Example usage for camera color sensor
    camera_sensor = CameraColorSensor()
    camera_value = camera_sensor.value
    print(f"Camera Color: {camera_value}")

    # Example usage for battery charge sensor
    battery_sensor = BatteryChargeSensor()
    battery_value = battery_sensor.value
    print(f"Battery Charge Level: {battery_value}%")
