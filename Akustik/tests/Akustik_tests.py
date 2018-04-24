from nose.tools import *
from Akustik.vented_box import *
from Akustik.Akustik_class import *

def setup():
    print("SETUP")


def teardown():
    print("TEARDOWN")


def test_basic():
    print("I RAN!", end='')

def test_calc_Q_L():
    fs = 140
    Qms = 7.3
    Qes = 0.82
    Qts = 0.73
    Re = 6.2
    fB = 100
    fL = 40
    fH = 80
    R0 = 20

    fsb = calc_Fsb(fL,fH,fB)
    assert_equal(fsb, (fL * fH) / fB)

    Im = calc_Im(R0, Re)
    assert_equal(Im, Re / R0)

    Qmsb = calc_Qmsb(fs, fsb, Qms)
    assert_equal(Qmsb, (fs / fsb) * Qms)

    Qesb = calc_Qesb(fs, fsb, Qes)
    assert_equal(Qesb,  (fs / fsb) * Qes)

    Qtsb = calc_Qtsb(fs, fsb, Qts)
    assert_equal(Qtsb,  (fs / fsb) * Qts)

    ha = calc_ha(fB, fsb)
    assert_equal(ha, fB/fsb)

    alpha = calc_alpha(fB, fH, fL)
    assert_equal(alpha,  ((fH**2-fB**2)*(fB**2-fL**2)) / (fH**2 * fL**2))

    Q_L = calc_Ql(fs,Qms,Qes,Qts,Re,fB,fL,fH,R0)

def test_freq_response_vented_box():
    Fs = 43
    Qts = 0.73
    Vb = 500
    Vas = 144
    Fb = 50
    Ql = 7 #normal optimal value of box losses
    F = 100
    dBmag = freq_response_vented_box(Vb, Vas, Fs, Qts, Fb, Ql, F)

def test_Enclosure():
    w = 2.5#[decimeter]
    d = 3
    h = 6
    a = 0.82#[decimeter]
    Sd = 0.04#[m^2]
    Sp = 0.01
    Lp = 0.03
    box = Enclosure(h, w, d, a, Sd, Sp, Lp)
    Sb = box.Sb()
    Vb = box.Vb()
    B = box.B()
