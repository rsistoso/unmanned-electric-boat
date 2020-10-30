def run(self):
	self.PWM=Motor()
 	self.pwm_S=Servo()
	for i in range(30,151,60):
		self.pwm_S.setServoPwm('0',i)
 		time.sleep(0.2)
 		if i==30:
 			L = self.get_distance()
 		elif i==90:
 			M = self.get_distance()
 		else:
 		R = self.get_distance()
 	while True:
 	for i in range(90,30,-60):
 		self.pwm_S.setServoPwm('0',i)
 		time.sleep(0.2)
 		if i==30:
 			L = self.get_distance()
 		elif i==90:
 			M = self.get_distance()
 		else:
 			R = self.get_distance()
 		self.run_motor(L,M,R)
 	for i in range(30,151,60):
 		self.pwm_S.setServoPwm('0',i)
 		time.sleep(0.2)
 		if i==30:
 			L = self.get_distance()
 		elif i==90:
 			M = self.get_distance()
 		else:
 			R = self.get_distance()
 		self.run_motor(L,M,R)
ultrasonic=Ultrasonic()
# Main program logic follows:
if __name__ == '__main__':
	print ('Program is starting ... ')
	try:
		ultrasonic.run()
	except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be
executed.
	PWM.setMotorModel(0,0,0,0)
	ultrasonic.pwm_S.setServoPwm('0',90)
