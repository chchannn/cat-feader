import RPi.GPIO as GPIO
import time


def feed(p0=2, p1=7):

    with open('/home/pi/catfeeder/django_feeder/feeder/current_location.txt', 'r+') as f:
        dc = float(f.read())
        if dc == p0:
            dc = p1
        else:
            dc = p0
        f.seek(0)
        f.write(str(dc))
        f.truncate()


    print('feeding...')
    print('current DC:', dc)

    # Set GPIO numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Set pin 11 as output, and set servo as for pin 11 to 50Hz PWM
    GPIO.setup(11, GPIO.OUT)
    servo = GPIO.PWM(11, 50)

    servo.start(dc)
    time.sleep(.5)

    if dc == p0:
        print('Set DC:', p1)
        servo.ChangeDutyCycle(p1)
        time.sleep(.5)
    else:
        print('Set DC:', p0)
        servo.ChangeDutyCycle(p0)
        time.sleep(.5)

    print('feed complete, shutdown servo')
    servo.ChangeDutyCycle(0)
    servo.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    feed(2.5, 8.5)


