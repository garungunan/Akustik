from math import *
import numpy as n
import plot

def herz_to_meter(frec, temp=20, decimal=2):

    def herz_to_meter(frec, temp, decimal):
        '''Return the wavelength of a given frequency and temperature
            in celsius, in meter'''
        speed_of_sound = 343
        c_air = 331.3 * sqrt(1 + temp / 275.15 )
        wavelength = c_air / frec
        return round(wavelength, decimal)

    if type(frec) == int or type(frec) == float:
        return herz_to_meter(frec, temp, decimal)
    elif type(frec) == list and type(temp) == list:
        pass
    else:
        print("Wrong data type, frec: ", type(frec), " temp: ", type(temp),  "decimal: ", type(decimal))

def plot_wavelength_analysis(startfrec, endfrec, starttemp, endtemp):

    frequency_range = n.arange(startfrec, endfrec, 1)
    temperature_range = n.arange(starttemp, endtemp, 1)
    wavelength = herz_to_meter(frequency_range, temperature_range)
    plot.plot3D(Y=frequency_range, X=temperature_range, Z=wavelength)
    #X, Y = n.meshgrid(temperature_range, frequency_range)


def testPWA():

    startfrec = 100
    endfrec = 1000
    starttemp = 20
    endtemp= 30
    plot_wavelength_analysis(startfrec, endfrec, starttemp, endtemp)
