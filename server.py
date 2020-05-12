

import json
from time import sleep, clock
#библиотека для orange pi
from pyA20.gpio import gpio
from pyA20.gpio import port
#библиотека для сервера
from flask import Flask, request
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

#работа с json файлом и кормление
with open('/var/www/uploads/time.json') as json_file: 
    data = json.load(json_file)
	portion = data["portion"]
	for data in data:
		if data["1"] and data["1"] = clock():
			rotate(data["portion"])
		if data["2"] and data["2"] = clock():
			rotate(data["portion"])
		if data["3"] and data["3"] = clock():
			rotate(data["portion"])
		if data["4"] and data["4"] = clock():
			rotate(data["portion"])
		if data["5"] and data["5"] = clock():
			rotate(data["portion"])
		if data["6"] and data["6"] = clock():
			rotate(data["portion"])
		if data["7"] and data["7"] = clock():
			rotate(data["portion"])
		if data["8"] and data["8"] = clock():
			rotate(data["portion"])
		if data["9"] and data["9"] = clock():
			rotate(data["portion"])
		if data["10"] and data["10"] = clock():
			rotate(data["portion"])
		if data["11"] and data["11"] = clock():
			rotate(data["portion"])
		if data["12"] and data["12"] = clock():
			rotate(data["portion"])
app = Flask(__name__)
@app.route("/")
def index():
	gpio.output(right, 0)
	gpio.output(left, 0)
	return 'stop rotating'
@app.route('/rotate/<int:gram>')
def rotate(gram):
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
#взять текущий вес	
@app.route('/get_cur_weight')
def get_cur_weight():
	hx = HX711(dout_pin = port.PC2, pd_sck_pin = port.PC0)
	return hx.get_weight_mean(1)
#Pfuhepbnm json файл
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/time.json'


if __name__ == '__main__':
	app.run(debug=True, port=80, host='0.0.0.0')
