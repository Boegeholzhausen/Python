from phue import Bridge
import random

bridge_ip_address = "192.168.2.100"
b = Bridge(bridge_ip_address)

lights = b.get_light_objects()

for light in lights:
	light.brightness = 254
	light.xy = [random.random(),random.random()]