# pyqtLed
pyqtLed is a simple importable custom widget for LED-like indicators in PyQT5.

to create a new led instance, simply assign it like so:
`led1 = QtLed()`

you can also initialize it with a color already selected by specifying in-line
`led1 = QtLed("green")`

Change LED color at will by using
`variableName.changeColor("<color name>")`

the currently available colors are as follows:
- ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `"red"`
- ![#1c73ff](https://placehold.it/15/1c73ff/000000?text=+) `"blue"`
- ![#00ff37](https://placehold.it/15/00ff37/000000?text=+) `"green"`
- LEDs will default to ![#a8a8a8](https://placehold.it/15/a8a8a8/000000?text=+) if no color is selected


