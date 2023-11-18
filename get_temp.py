import decimal

'''
Таким чином, клас SensorBase тепер містить загальну логіку,
 а кожен конкретний датчик має свій клас для значення та
 власний клас для конвертації значення.

 Після компіляції виникає помилка через те що шляху до даних із датчика не існує
 в моїй системі.

'''


class SensorValue:
    def __init__(self, raw_value):
        self.raw_value = raw_value

    def convert_value(self):
        raise NotImplementedError("Subclasses must implement convert_value method")

class TemperatureSensorValue(SensorValue):
    _PREC = 3

    def convert_value(self):
        value = int(self.raw_value)
        val = f'{value}.' + '0' * self._PREC
        dec = decimal.Decimal(val) / (10 ** self._PREC)
        return dec

class SoundLevelSensorValue(SensorValue):
    def convert_value(self):
        # Implement the conversion logic for sound level sensor
        pass

class CameraColorSensorValue(SensorValue):
    def convert_value(self):
        # Implement the conversion logic for camera color sensor
        pass

class BatteryLevelSensorValue(SensorValue):
    def convert_value(self):
        # Implement the conversion logic for battery level sensor
        pass

class SensorBase:
    _TEMPLATE = None
    value_class = None

    def __init__(self, sensor_num=0, *, _tpl=None):
        sensor_num = int(sensor_num)
        tpl = self._TEMPLATE if _tpl is None else _tpl
        self.sensor = tpl.format(num=sensor_num)

    def get_raw_value(self):
        with open(self.sensor, 'r') as file:
            return file.readline().strip()

    def get_sensor_value(self):
        raw_value = self.get_raw_value()
        return self.value_class(raw_value)

    @property
    def value(self):
        if not hasattr(self, '_value'):
            self._value = self.get_sensor_value()
        return self._value

class TemperatureSensor(SensorBase):
    _TEMPLATE = '/sys/class/thermal/thermal_zone{num}/temp'
    value_class = TemperatureSensorValue

class SoundLevelSensor(SensorBase):
    # Define sound level sensor-specific attributes and methods
    value_class = SoundLevelSensorValue

class CameraColorSensor(SensorBase):
    # Define camera color sensor-specific attributes and methods
    value_class = CameraColorSensorValue

class BatteryLevelSensor(SensorBase):
    # Define battery level sensor-specific attributes and methods
    value_class = BatteryLevelSensorValue

if __name__ == '__main__':
    temperature_sensor = TemperatureSensor()
    temperature_value = temperature_sensor.value
    print(f"Temperature: {temperature_value.convert_value()}")

    sound_level_sensor = SoundLevelSensor()
    sound_level_value = sound_level_sensor.value
    # Process sound_level_value as needed

    camera_color_sensor = CameraColorSensor()
    camera_color_value = camera_color_sensor.value
    # Process camera_color_value as needed

    battery_level_sensor = BatteryLevelSensor()
    battery_level_value = battery_level_sensor.value
    # Process battery_level_value as needed
