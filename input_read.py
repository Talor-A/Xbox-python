import XboxController
import time

xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)
# joystickNo : specify the number of the pygame joystick you want to use, usually 0
# deadzone : the minimum value from the analogue sticks
# scale : values are returned between -1 and 1
# invertYAxis : default is -1 being up and 1 being down
# controllerCallBack : pass the name of a function and the xbox controller will call this function each time the controller changes (i.e. a button is pressed) returning the id of the control (what button, stick or trigger) and the current value


def startButtonCallBack(value):
    print "Start button pressed / released"

xboxCont.setupControlCallback(
    xboxCont.XboxControls.START,
    startButtonCallBack)

xboxCont.start()

while True :
  time.sleep(0.1)
  print xboxCont.RTRIGGER
  if xboxCont.RTRIGGER == 1:
    quit()
    xboxCont.stop()
