#import numpy as n
from numpy import sqrt, log10, log, tanh, arcsinh
from scipy import signal

def ideal_Vented_Box(Qts, Vas, Fs, decimal=2):
    '''Calculate an "ideal" enclousure, based on drkrupp.se
        Return a dict of Vb, Fmin3dB and Fb'''

    Vb = round( 15 * Qts**2.87 * Vas, decimal)
    Fmin3dB = round( 0.26 * Qts**-1.4 * Fs, decimal)
    Fb = round( 0.42 * Qts**-0.9 * Fs, decimal)
    return {'Vb':Vb, 'Fmin3dB':Fmin3dB, 'Fb':Fb}


def Vented_box_given_Vb(Vb, Vas, Fs, Qts, decimal=2):

    Fmin3dB = round(sqrt(Vas / Vb) * Fs, decimal)
    Fb = round((Vas / Vb)**0.32 * Fs, decimal)
    peakOrDip = round(20 * log(  2.6 * Qts * ( (Vas / Vb)**0.35 )  ),decimal)
    return {'Fmin3dB': Fmin3dB, 'Fb':Fb, 'peakOrDip': peakOrDip}


def calc_Fb_ver1(Vd, Dmin, Np):
    ''' Vd[m^3]: maximum air volume displacement by cone excursion
        Dmin[m]: minimun vent port diameter
        Np:number of port or vents
        Taken from
        "https://www.ajdesigner.com/phpsubwoofervented/port_minimum_diameter_equation_fb.php"'''
    Fb = Vd**2 / ((Dmin * sqrt(Np)) / 2030)**4
    return Fb


def calc_Q_B(Ql=7, Qa=1, Qp=1):
    '''Ql: box leakage loss, Qa: dampening loss, Qp: port loss'''
    return 1 / ( 1 / Ql + 1 / Qa + 1 / Qp)


def calc_Ql(Fs, Qms, Qes, Qts, Re, Fb, Fl, Fh, R0):
    '''Return the Q value of enclosure losses.'''

    Fsb = calc_Fsb(Fl, Fh, Fb)
    ha = calc_ha(Fb, Fsb)
    alpha = calc_alpha(Fb, Fh, Fl)
    Qesb = calc_Qesb(Fs, Fsb, Qes)
    Qmsb = calc_Qmsb(Fs, Fsb, Qms)
    Im = calc_Im(R0, Re)
    Ql = (ha/alpha) * ((1/(Qesb*(Im-1))) - (1/Qmsb))

    return Ql


def calc_Fsb(Fl, Fh, Fb):
    '''Fb: resonant box frequency, Fh: frequency at high peak of enclosure impedance curve. Fl: lower peak of enclosure impedance curve.'''
    return (Fl * Fh) / Fb

def calc_Im(R0, Re):
    '''R0: impedance at Fb, Re: resistive impedance of voicecoil'''
    return Re / R0

def calc_Qmsb(Fs, Fsb, Qms):
    '''Fs:resonant freq. of speaker, Qms: mech. Q value'''
    return (Fs / Fsb) * Qms

def calc_Qesb(Fs, Fsb, Qes):
    return calc_Qmsb(Fs, Fsb, Qes)

def calc_Qtsb(Fs, Fsb, Qts):
    return calc_Qmsb(Fs, Fsb, Qts)

def calc_ha(Fb, Fsb):
    return Fb / Fsb

def calc_alpha(Fb, Fh, Fl):
    a = Fb**2
    b = Fh**2
    c = Fl**2
    return ((b-a)*(a-c)) / (b*c)


def calculate_Vb(Qts, ):


    return Vb

'''***Suit of equations for the transfer function           ***'''
'''***describing the frequency response of a vented box     ***'''

def calc_omegaB(Map, Cab):
    ''''Enclosure resonance frequency'''
    return 1/sqrt(Map * Cab)


def calc_omegaS(Mac, Cas):
    '''Loudspeaker resonance frequency'''
    return calc_omegaB(Mac, Cas)


def calc_omega0(omegaB, omegaS):
    return sqrt(omegab * omegaS)


def calc_h(omegaB, omegaS):
    '''Helmholtz tuning ratio'''
    return omegaB / omegaS


def calc_alp(Vas, Vab):
    '''Compliance/volume ratio, Cas/Cab alt. Vas/Vab'''
    return Vas / Vab


def calc_Ql_ver2(Ral, Cab, Map):
    '''Quality factor: loss'''
    return Ral * sqrt(Cab / Map)


def calc_Qts(Rae, Ras, Mac, Cas):
    1 / (Rae + Ras) * sqrt(Mac / Cas)


def a1(Ql, h, Qts):
    '''constant a1, for the 1n pole in the freq response transfer function '''
    root_h = sqrt(h)
    return 1 / (Ql * root_h) + root_h / Qts


def a2(alp, h, Ql, Qts):
    return (alp + 1) / h + h + 1 / (Ql * Qts)


def a3(Qts, Ql, h):
    root_h = sqrt(h)
    return  1/(Qts * root_h) + root_h / Ql

def transfer_function(omega0, a1, a2, a3):
    numerator = [ 1, 0, 0, 0 ]
    denominator = [1, a3*omega0, a2*omega0**2, a1*omega0**3, omega0**4]
    return signal.lti(numerator, denominator)


def transfer_function_ver2(omega0, a1, a2, a3):
    numerator = [ 1/(omega0**4), 0, 0, 0 ]
    denominator = [1/(omega0**4), a3/(omega0**3), a2/(omega0**2), a1/(omega0), 1]
    return signal.TransferFunction(numerator, denominator)


'''Butterworth alignment coefficients'''
def a1_butter():
    return sqrt(4 + 2 * sqrt(2))

def a2_butter():
    return 2 + sqrt(2)

def a3_butter():
    return a1_butter()


'''Chebyshev alignmnet'''

def magnitude_of_cheby_ripple(epsilon):
    '''Parameters: epsilon - set the ripple of Chebyshev filter pass band'''
    '''Return: the magnitude of the passband ripple in [dB]'''
    '''Ex: ep(0.5)=1dB, ep(1)=3dB, ep(2)=7dB'''
    return 10 * log10(1 + epsilon**2)

def omegaN(omega3dB, epsilon):
    return omega3dB / 2 * sqrt(2 + sqtr(2 + 2 * sqrt(2 + 1 / epsilon**2) ) )

def Omega(omega, omegaN):
    return omega / omegaN

def omega0_cheby(omegaN, epsilon):
    '''Chebyshev resonant frequency of the system'''
    return omegaN * ((64 * epsilon**2) / (1 + epsilon**2))

def k(epsilon):
    return tanh( 1/4 * arcsinh(1/epsilon) )

def D(k):
    return (k**4 + 6 * k**2 + 1) / 8

def a1_cheby(k, D):
    return (k * sqrt(4 + 2 * sqrt(2) ) ) / (D)**(1/4)

def a2_cheby(k, D):
    return (1 + k**2(1 + sqrt(2) ) ) / sqrt(D)

def a3_cheby(a1, k, D):
    return (a1 / sqrt(D) ) * (1 - (1 - k**2) / (2 * sqrt(2) ) )



def freq_response_vented_box(Vb, Vas, Fs, Qts, Fb, Ql, F):
    Fn2 = (F / Fs)**2
    Fn4 = Fn2**2
    A = (Fb / Fs)**2
    B = A / Qts + Fb / (Fs * Ql)
    C = 1 + A + (Vas / Vb) + Fb / (Fs * Qts * Ql)
    D = 1 / Qts + Fb / (Fs * Ql)
    dBmag = 10 * log10(Fn4**2 / ((Fn4 - C * Fn2 + A)**2 + Fn2 * (D *Fn2 - B)**2))
    return dBmag


if __name__ == '__main__':
    Qts = 0.73
    Vas = 144
    Fs = 43
    Vb = 400
    idealBox = ideal_Vented_Box(Qts, Vas, Fs)
    print(idealBox)
    realisticBox = Vented_box_given_Vb(Vb,Vas,Fs,Qts)
    print(realisticBox)
