from graphics import *

win=GraphWin("Fahrenheit Converter",400,300)
win.setCoords(0.0,0.0,3.0,4.0)

Text(Point(1,3),"Farenheit  Temperature:").draw(win)
Text(Point(1,1),"Celcius Temperture:").draw(win)

celcius_entry= Entry(Point(2,3), 5)
celcius_entry.draw(win)

button=Text(Point(1.5,2.0),"Convert it")
button.draw(win)
Rectangle(Point(1,1.5), Point(2, 2.5)).draw(win)

output=Text(Point(2,1),"")
output.draw(win)

win.getMouse()

#Conversion
fahrenheit=eval(celsius_entry.getText())
celcius=5.0/9.0*fahrenheit-32

#display
output.setText(fahrenheit)
button.setText("Quit")

win.getMouse()
win.close()
