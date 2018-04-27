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


def calc_Fb_ver1(Vd, Dmin, Np):
    ''' Vd[m^3]: maximum air volume displacement by cone excursion
        Dmin[m]: minimun vent port diameter
        Np:number of port or vents
        Taken from
        "https://www.ajdesigner.com/phpsubwoofervented/port_minimum_diameter_equation_fb.php"'''
    Fb = Vd**2 / ((Dmin * n.sqrt(Np)) / 2030)**4
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


def calc_omegaB(Map, Cab):
    ''''Enclosure resonance frequency'''
    return 1/n.sqrt(Map * Cab)


def calc_omegaS(Mac, Cas):
    '''Loudspeaker resonance frequency'''
    return calc_omegaB(Mac, Cas)

def calc_omega0(omegaB, omegaS):
    return .sqrt(omegab * omegaS)


def calc_h(omegaB, omegaS):
    '''Helmholtz tuning ratio'''
    return omegaB / omegaS

def calc_alp(Vas, Vab):
    '''Compliance/volume ratio, Cas/Cab alt. Vas/Vab'''
    return Vas / Vab

def calc_Ql_ver2(Ral, Cab, Map):
    '''Quality factor: loss'''
    return Ral * n.sqrt(Cab / Map)


def calc_Qts(Rae, Ras, Mac, Cas):
    1 / (Rae + Ras) * n.sqrt(Mac / Cas)

def a1(Ql, h, Qts):
    '''constant a1, for the 1n pole in the '''
    root_h = n.sqrt(h)
    return 1 / (Ql * root_h) + root_h / Qts

def a2(alp, h, Ql, Qts):
    return (alp + 1) / h + h + 1 / (Ql * Qts)




def freq_response_vented_box(Vb, Vas, Fs, Qts, Fb, Ql, F):
    Fn2 = (F / Fs)**2
    Fn4 = Fn2**2
    A = (Fb / Fs)**2
    B = A / Qts + Fb / (Fs * Ql)
    C = 1 + A + (Vas / Vb) + Fb / (Fs * Qts * Ql)
    D = 1 / Qts + Fb / (Fs * Ql)
    dBmag = 10 * n.log10(Fn4**2 / ((Fn4 - C * Fn2 + A)**2 + Fn2 * (D *Fn2 - B)**2))
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
