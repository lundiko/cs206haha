import numpy as numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backData.npy")
frontLegSensorValues = numpy.load("data/frontData.npy")
matplotlib.pyplot.plot(backLegSensorValues, label ='back leg', linewidth =4 )
matplotlib.pyplot.plot(frontLegSensorValues, label ='front leg' )
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
