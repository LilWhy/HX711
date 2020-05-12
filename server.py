


from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
from flask import Flask

left = port.PG6
right = port.PG7
dout_pin = port.PC2
pd_sck_pin = port.PC0
signal_rotate = port.PA10
gpio.init()
gpio.setcfg(left, gpio.OUTPUT)
gpio.setcfg(right, gpio.OUTPUT)
gpio.setcfg(signal_rotate, gpio.INPUT)

app = Flask(__name__)
@app.route("/")
def index():
	gpio.output(right, 0)
	gpio.output(left, 0)
	return 'stop rotating'
@app.route('/rotate/<int:time>')
def rotate(time):
	gpio.output(left, 1)
	n = 0
	time = time * 2
	while n <= time:
		sleep(0.05)
		if(gpio.input(signal_rotate)):
			n += 1
	gpio.output(left, 0)	
	return 'rotate'
@app.route("/right")
def action_right():	
	gpio.output(right, 1)
	gpio.output(left, 0)
	return 'Right'
if __name__ == '__main__':
	app.run(debug=True, port=80, host='0.0.0.0')
