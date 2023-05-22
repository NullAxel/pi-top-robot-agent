from flask import Flask, render_template
from pitop import Pitop
from pitop.robotics.drive_controller import DriveController
from time import sleep
from pitop import Buzzer
from pitop import LED
import pyttsx3
import os
import anvil.server

anvil.server.connect(os.environ.get("ANVIL_TOKEN"))
robot = Pitop()
# Note: The ports in here are CUSTOM, so please do not make a issue because of this.
drive = DriveController(left_motor_port="M3", right_motor_port="M2")
robot.add_component(drive)
buzzer = Buzzer("D7")
led1 = LED("D6")
led2 = LED("D5")
app = Flask(__name__)
common_speed = 0.5

@app.route('/l1') ## LIGHTS ON
def l1():
    led1.on()
    led2.on()
    return str(robot.battery.capacity)

@app.route('/l0') ## LIGHTS OFF
def l0():
    led1.off()
    led2.off()
    return str(robot.battery.capacity)

@app.route('/w') # DRIVE W (FORWARDS)
def w():
    robot.drive.forward(common_speed)
    sleep(1)
    robot.drive.stop()
    return str(robot.battery.capacity)

@app.route('/s') ## DRIVE S (BACKWARDS)
def s():
    robot.drive.forward(-common_speed)
    sleep(1)
    robot.drive.stop()
    return str(robot.battery.capacity)

@app.route('/a') ## DRIVE A (LEFT)
def a():
    robot.drive.left(common_speed)
    sleep(1)
    robot.drive.stop()
    return str(robot.battery.capacity)

@app.route('/d') ## DRIVE D (RIGHT)
def d():
    robot.drive.right(common_speed)
    sleep(1)
    robot.drive.stop()
    return str(robot.battery.capacity)
@app.route('/q') ## STOP DRIVING
def q():
    robot.drive.stop()
    sleep(1)
    robot.drive.stop()
    return str(robot.battery.capacity)
@app.route("/b") ## BUZZ HALF A SEC
def b():
    buzzer.on()
    sleep(.5)
    buzzer.off()
    return str(robot.battery.capacity)
@app.route("/t/<msg>") ## TEXT TO SPEECH
def t(msg):
    os.popen(f"gtts-cli '{msg}' -l es | play -t mp3 -")
    return str(robot.battery.capacity)


### V2: WORK IN PROGRESS (FOR PYGAME PATH ROUTING)
@app.route('/v2/rotate-a')
def v2_rotate_a():
    robot.drive.left(0.3)
    sleep(1)
    robot.drive.stop()
    return "Ok"
@app.route('/v2/rotate-d')
def v2_rotate_d():
    robot.drive.right(0.3)
    sleep(1)
    robot.drive.stop()
    return "Ok"
@app.route('/v2/w/<sec>')
def adelante(sec):
    robot.drive.forward(0.4)
    sleep(float(sec))
    robot.drive.stop()
    return "Ok"
@app.route('/v2/s/<sec>')
def atras(sec):
    robot.drive.forward(-0.4)
    sleep(float(sec))
    robot.drive.stop()
    return "Ok"
@app.route('/v2/a/<sec>')
def izquierda(sec):
    robot.drive.left(0.4)
    sleep(float(sec))
    robot.drive.stop()
    return "Ok"
@app.route('/v2/d/<sec>')
def derecha(sec):
    robot.drive.right(0.4)
    sleep(float(sec))
    robot.drive.stop()
    return "Ok"

if __name__ == '__main__':
    robot.miniscreen.display_multiline_text("Axel", font_size=50)
    anvil.server.wait_forever()
    #app.run(host='0.0.0.0', port=9999)
