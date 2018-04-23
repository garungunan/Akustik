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

def calc_Q_B(Q_L=7, Q_A=1, Q_P=1):
    '''Q_L: box leakage loss, Q_A: dampening loss, Q_P: port loss'''
    return 1 / ( 1 / Q_L + 1 / Q_A + 1 / Q_P)


def calc_Q_L(fs, Qms, Qes, Qts, Re, fB, fL, fH, R0):
    '''Return the Q value of enclosure losses.'''

    def calc_fsb(fL, fH, fB):
        '''fB: resonant box frequency, fH: frequency at high peak of enclosure impedance curve. fL: lower peak of enclosure impedance curve.'''
        return (fL * fH) / fB

    def calc_Im(R0, Re):
        '''R0: impedance at fB, Re: resistive impedance of voicecoil'''
        return Re / R0

    def calc_Qmsb(fs, fsb, Qms):
        '''fs:resonant freq. of speaker, Qms: mech. Q value'''
        return (fs / fsb) * Qms

    def calc_Qesb(fe, fsb, Qes):
        return calc_Qmsb(fe, fsb, Qes)

    def calc_Qtsb(fe, fsb, Qts):
        return calc_Qmsb(fs, fsb, Qts)

    def calc_ha(fb, fsb):
        return fb / fsb

    def calc_alpha(fb, fH, fL):
        a = fb**2
        b = fH**2
        c = fL**2
        return ((b-a)*(a-c)) / (b*c)

    fsb = calc_fsb(fL, fH, fb)
    ha = calc_ha(fb, fsb)
    alpha = calc_alpha(fb, fH, fL)
    Qesb = calc_Qesb(fe, fsb, Qes)
    Qmsb = calc_Qmsb(fe, fsb, Qms)
    Im = calc_Im(R0, Re)
    Q_L = (ha/alpha) * ((1/(Qesb*(Im-1))) - (1/Qmsb))

    return Q_L


def calculate_Vb(Qts, ):


    return Vb
