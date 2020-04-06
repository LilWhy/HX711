
from pyA20.gpio import gpio
from pyA20.gpio import port  # import GPIO
from hx711 import HX711  # import the class HX711

def dout_pin = port.PC2
def pd_sck_pin = port.PC0
hx = HX711(dout_pin, pd_sck_pin)  # create an object
print hx.get_raw_data_mean()  # get raw data reading from hx711
