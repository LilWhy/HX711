


from time import sleep
#библиотека для orange pi
from pyA20.gpio import gpio
from pyA20.gpio import port
#библиотека для сервера
from flask import Flask
#библиотека для работы с весами
from HX711 import HX711 

#назначаем порт на вращение вперед
left = port.PG6
#назначаем порт на вращение назад
right = port.PG7
#порты для весов
dout_pin = port.PC2
pd_sck_pin = port.PC0
#порт для сигнала ИК-датчика
signal_rotate = port.PA10

#инициализация портов
gpio.init()
#установка режима портов
gpio.setcfg(left, gpio.OUTPUT)
gpio.setcfg(right, gpio.OUTPUT)
gpio.setcfg(signal_rotate, gpio.INPUT)

app = Flask(__name__)
@app.route("/")
def index():
	gpio.output(right, 0)
	gpio.output(left, 0)
	return 'stop rotating'
@app.route('/rotate/<int:gram>')
def rotate(time):
	#назначаем пины у весов
	hx = HX711(dout_pin = port.PC2, pd_sck_pin = port.PC0)
	n = 0
	#выдавать корм пока на весах не будет необходимое кол-во грамм
	while n <= gram:
		if_rotate()
		n = hx.get_weight_mean(1)
	#остановить вращение
	gpio.output(left, 0)	
	return 'rotate'

#проверка на вращение
def if_rotate():
	gpio.output(left, 1)
	speed =	gpio.input(signal_rotate)
	sleep(0.3)
	#если мотор не крутится, то покрутить в обратную сторону две секунды
	if (speed == gpio.input(signal_rotate)):
		gpio.output(left, 0)
		gpio.output(right, 1)
		sleep(2)
	
@app.route('/get_cur_weight')
def get_cur_weight():
	hx = HX711(dout_pin = port.PC2, pd_sck_pin = port.PC0)
	return hx.get_weight_mean(1)

if __name__ == '__main__':
	app.run(debug=True, port=80, host='0.0.0.0')
