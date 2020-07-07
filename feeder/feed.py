import RPi.GPIO as GPIO
import time
import os

def feed(p0=2, p1=7, n_stress_relief=3, stress_relief_offset=.5):
    """p0 should be smaller than p1"""
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'current_location.txt')
    
    with open(filename, 'r+') as f:
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
    time.sleep(.5)

    # Set GPIO numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Set pin 11 as output, and set servo as for pin 11 to 50Hz PWM
    GPIO.setup(11, GPIO.OUT)
    servo = GPIO.PWM(11, 50)
    
    if dc == p0:
        p1stop = p1 - stress_relief_offset # tick back a bit to remove stress
        
        print('Set DC:', p1)
        servo.start(p1)
        time.sleep(.5)
        
        print('Set DC:', p1stop)
        for _ in range(n_stress_relief):
            servo.ChangeDutyCycle(p1stop)
            time.sleep(.5)
        
    else:
        p0stop = p0 + stress_relief_offset
        
        print('Set DC:', p0)
        servo.start(p0)
        time.sleep(.5)
        
        print('Set DC:', p0stop)
        for _ in range(n_stress_relief):
            servo.ChangeDutyCycle(p0stop)
            time.sleep(.5)
    
    print('feed complete, shutdown servo')
    servo.ChangeDutyCycle(0)
    time.sleep(1)
    servo.stop()
    GPIO.cleanup()

      return 'feed complete, shutdown servo'


# def feed(a,b):
#     print(f'position {a}, {b}: feed complete, shutdown servo') 
#     return f'position {a}, {b}: feed complete, shutdown servo'


if __name__ == '__main__':
    _ = feed(2.5, 8.5)
