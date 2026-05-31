from time import sleep

from picarx import Picarx
import keyboard

def control_init():
    pass

def control_main(px:Picarx):
    try:
        if keyboard.is_pressed('w'):
            px.set_dir_servo_angle(0)
            px.forward(80)
        elif keyboard.is_pressed('s'):
            px.set_dir_servo_angle(0)
            px.backward(80)
        elif keyboard.is_pressed('a'):
            px.set_dir_servo_angle(-30)
            px.forward(80)
        elif keyboard.is_pressed('d'):
            px.set_dir_servo_angle(30)
            px.forward(80)
        else:
            px.set_dir_servo_angle(0)
            px.forward(0)

    except KeyboardInterrupt:
        px.set_cam_tilt_angle(0)
        px.set_cam_pan_angle(0)
        px.set_dir_servo_angle(0)
        px.stop()
        sleep(.2)