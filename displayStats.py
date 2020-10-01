from gpiozero import Button
from gpiozero import LED
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'shutdown', 'now'])

def reboot():
    check_call(['sudo', 'reboot'])

def main():
    poweredOnIndicator = LED("BOARD16")
    poweredOnIndicator.on()

    button = Button("BOARD5", hold_time=3)

    button.when_released = reboot
    button.when_held = shutdown

    pause()

if __name__ == "__main__":
    main()