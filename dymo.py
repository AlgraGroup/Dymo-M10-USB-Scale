# Code to read weight from a Dymo M5/M10 scale
#Original code from:
#https://steventsnyder.com/reading-a-dymo-usb-scale-using-python/
#Alex Lugo Reading USB in pyton, https://www.youtube.com/watch?v=xfhzbw93rzw for python 3
#Pio Baettig 2024

import usb.core
import usb.util

def find_scale():
    Dymo_VENDOR_ID = 0x0922
    Dymo_PRODUCT_ID = 0x8003

    dev = usb.core.find(idVendor=Dymo_VENDOR_ID, idProduct=Dymo_PRODUCT_ID)
    ep=dev[0].interfaces()[0].endpoints()[0]
    i=dev[0].interfaces()[0].bInterfaceNumber
    dev.reset()
    
    if dev.is_kernel_driver_active(i):
        dev.detach_kernel_driver(i)

    dev.set_configuration()
    eaddr=ep.bEndpointAddress

    return dev,eaddr
Dymo_Scale=find_scale()


def getWeight(unit='g'):
    data=Dymo_Scale[0].read(Dymo_Scale[1],8)
    print(data)
    
    match unit:
        case 'g':
            raw_weight = data[4] + data[5] * 256
        case 'kg':
            raw_weight = float(data[4] + data[5] * 256)/1000
        case 'oz':
            raw_weight = float(data[4] + data[5] * 256)/27.349523125
        case 'lb':
            raw_weight = float(data[4] + data[5] * 256)/437.59237
        case _:
            raw_weight = data[4] + data[5] * 256

    signed_weight=raw_weight*(-1) if (data[1]==5) else raw_weight

    return signed_weight


print(getWeight())
print(getWeight('g'), " g")
print(getWeight('kg'), " kg")
print(getWeight('oz'), " oz")
print(getWeight('lb'), " lb")



