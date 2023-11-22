import psutil
'''
Основна ідея полягає в тому, щоб мати базовий клас Sensor, 
який визначає загальну структуру та абстрактний метод get_data. 
Потім створюються конкретні класи BatterySensor і DiskSensor, 
які успадковують від базового класу і надають конкретну реалізацію 
методу get_data для датчика батареї та датчика дискового простору відповідно.
'''
class Sensor:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        raise NotImplementedError("Subclasses must implement this method")

class BatterySensor(Sensor):
    def get_data(self):
        battery = psutil.sensors_battery()
        return battery.percent

class DiskSensor(Sensor):
    def __init__(self, name, path='/'):
        super().__init__(name)
        self.path = path

    def get_data(self):
        disk = psutil.disk_usage(self.path)
        free_space_gb = disk.free / (2**30)  # Переведення байтів в гігабайти
        return free_space_gb

# Приклад використання
battery_sensor = BatterySensor("Battery")
disk_sensor = DiskSensor("Disk", path='/')

print(f"{battery_sensor.name} percentage: {battery_sensor.get_data()}%")
print(f"{disk_sensor.name} free space: {disk_sensor.get_data():.2f} GB")
