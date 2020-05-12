
from pyA20.gpio import gpio
from pyA20.gpio import port  # import GPIO
from HX711 import HX711  # import the class HX711


hx = HX711(dout_pin = port.PC2, pd_sck_pin = port.PC0)  # create an object


hx.set_scale_ratio(-19992.2) 
print(hx.get_weight_mean(1), 'g')
print (hx.get_raw_data_mean())  # get raw data reading from hx711


