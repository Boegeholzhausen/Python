from phue import Bridge
import random
from tkinter import *


bridge_ip_address = "192.168.2.100"
b = Bridge(bridge_ip_address)


root = Tk()

horizontal_frame = Frame(root)
horizontal_frame.pack()

lights = b.get_light_objects('id')

for light_id in lights:
    channel_frame = Frame(horizontal_frame)
    channel_frame.pack(side = LEFT)

    scale_command = lambda x, light_id=light_id: b.set_light(light_id,{'bri': int(x), 'transitiontime': 1})
    scale = Scale(channel_frame, from_ = 254, to = 0, command = scale_command, length = 200, showvalue = 0)
    scale.set(b.get_light(light_id,'bri'))
    scale.pack()

    button_var = BooleanVar()
    button_var.set(b.get_light(light_id, 'on'))
    button_command = lambda button_var=button_var, light_id=light_id: b.set_light(light_id, 'on', button_var.get())
    button = Checkbutton(channel_frame, variable = button_var, command = button_command)
    button.pack()

    label = Label(channel_frame)
    label.config(text = b.get_light(light_id,'name'))
    label.pack()

root.mainloop()


# for light in lights:
# 	light.brightness = 254
# 	light.xy = [random.random(),random.random()]



# print(b.get_group())
# b.set_light(["Hue play 1", "Hue play 2"], "bri", 100)


# def access_lights():
    # b = Bridge(bridge_ip_address)
    # light_name_list = b.get_light_objects("name")
    # return light_name_list

# def room_lights():
#     lights = access_lights(bridge_ip_address)
#     for light in lights:
#         lights[light].on = True
#         lights[light].hue = 15000
#         lights[light].saturation = 120

# def danger_mode():
#     lights = access_lights(bridge_ip_address)
#     for light in lights:
#         lights[light].on = True
#         lights[light].hue = 15000
#         lights[light].saturation = 120

# if __name__ == "__main__":
#     room_lights()