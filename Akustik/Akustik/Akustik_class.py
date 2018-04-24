import numpy as n

class Transducer:
    def __init__(self, Fs=None, Re=None, Qms=None, Qes=None,
                    Qts=None, Vas=None, Vd=None, Cms=None,
                    BL=None, Mms=None, Xmax=None, Sd=None,
                    Le=None):
        self.Fs = Fs
        self.Re = Re
        self.Qms = Qms
        self.Qes = Qes
        self.Qts = Qts
        self.Vas = Vas
        self.Vd = Vd
        self.Cms = Cms
        self.BL = BL
        self.Mms = Mms
        self.Xmax = Xmax
        self.Sd = Sd
        self.Le = Le

class Loudspeaker:

    def __init__(self, brand, model):
        self.transducer = Transducer()
        self.brand = brand
        self.model = model

class Enclosure:
    rho0 = 1.3 #[kg/m^3] mean density of air at 300K
    c_air = 0.718 #[kj/kg.K] Specific heat of air at...
                  #...constant isovolumetric process
    gamma = 1.4 #ratio of specific heats for air at 300K
    c0 = 344 #[m/s] speed of sound in air

    def __init__(self, h=None, w=None, d=None, a=None, Sd=None, Sp=None, Lp=None, rho_fill=None, c_fill=None, Vfill=None  ):
        self.height = h
        self.width = w
        self.depth = d
        self.speakerRadius = a
        self.diaphragmArea = Sd
        self.portArea = Sp
        self.portLength = Lp
        self.rho_fill = rho_fill
        self.c_fill = c_fill
        self.Vfill = Vfill

    def Vb(self):
        '''Vb: Box volume'''
        return self.height * self.width * self.depth

    def Sb(self):
        '''Sb: Baffle area'''
        return self.width * self.height

    def B(self):
        Sb = self.Sb()
        Sd = self.diaphragmArea
        d = self.depth
        a = (d/3)*(Sd/Sb)**2 * n.sqrt(n.pi / Sd)
        b = (8 / (3 * n.pi)) * (1 - Sd / Sb)
        return a + b

    def rho_eff(self):
        return

if __name__ == '__main__':
    fane = Loudspeaker("Fane", "Sovereign 15-250")
    print(fane)
    print(fane.brand, " ", fane.model)
    print(fane.transducer.Fs)
