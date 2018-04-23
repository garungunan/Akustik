import numpy as n

def ideal_Vented_Box(Qts, Vas, Fs, decimal=2):
    '''Calculate an "ideal" enclousure, based on drkrupp.se
        Return a dict of Vb, Fmin3dB and Fb'''

    Vb = round( 15 * Qts**2.87 * Vas, decimal)
    Fmin3dB = round( 0.26 * Qts**-1.4 * Fs, decimal)
    Fb = round( 0.42 * Qts**-0.9 * Fs, decimal)
    return {'Vb':Vb, 'Fmin3dB':Fmin3dB, 'Fb':Fb}


def Vented_box_given_Vb(Vb, Vas, Fs, Qts, decimal=2):

    Fmin3dB = round(n.sqrt(Vas / Vb) * Fs, decimal)
    Fb = round((Vas / Vb)**0.32 * Fs, decimal)
    peakOrDip = round(20 * n.log(  2.6 * Qts * ( (Vas / Vb)**0.35 )  ),decimal)
    return {'Fmin3dB': Fmin3dB, 'Fb':Fb, 'peakOrDip': peakOrDip}


Qts = 0.73
Vas = 144
Fs = 43
Vb = 400
idealBox = ideal_Vented_Box(Qts, Vas, Fs)
print(idealBox)
realisticBox = Vented_box_given_Vb(Vb,Vas,Fs,Qts)
print(realisticBox)
