from __future__ import division, print_function

import numpy as np

class material:
    '''
    material class
    describes material parameters (elastic and plastic) for dynamic rupture
    '''
    def __init__(self, rho = 2.67, lam = 32.04, g = 32.04, mu = 0.5735, beta = 0.2867, eta = 0.2775):
        assert(rho > 0.)
        assert(lam > 0.)
        assert(g > 0.)
        assert(mu > 0.)
        assert(beta > 0.)
        assert(eta > 0.)
        self.rho = rho
        self.lam = lam
        self.g = g
        self.mu = mu
        self.beta = beta
        self.eta = eta

    def get_rho(self):
        '''
        returns density
        '''
        return self.rho

    def get_lam(self):
        '''
        returns first Lame parameter
        '''
        return self.lam

    def get_g(self):
        '''
        returns shear modulus
        '''
        return self.g

    def get_mu(self):
        '''
        returns internal friction angle
        '''
        return self.mu

    def get_beta(self):
        '''
        returns plastic dilatancy
        '''
        return self.beta

    def get_eta(self):
        '''
        returns plastic viscosity
        '''
        return self.eta

    def get_cs(self):
        '''
        returns shear wave speed
        '''
        return np.sqrt(self.g/self.rho)

    def get_cp(self):
        '''
        returns dilatational wave speed
        '''
        return np.sqrt((self.lam + 2.*self.g)/self.rho)

    def get_zs(self):
        '''
        returns shear impedance
        '''
        return np.sqrt(self.g*self.rho)

    def get_zp(self):
        '''
        returns dilatational impedance
        '''
        return np.sqrt((self.lam + 2.*self.g)*self.rho)

    def set_rho(self,rho):
        '''
        sets density to new value
        '''
        assert(rho > 0.)
        self.rho = float(rho)

    def set_lam(self,lam):
        '''
        sets lame parameter to new value
        '''
        assert(lam > 0.)
        self.lam = float(lam)

    def set_g(self,g):
        '''
        sets shear modulus to new value
        '''
        assert(g > 0.)
        self.g = float(g)

    def set_mu(self,mu):
        '''
        sets internal friction to new value
        '''
        assert(mu > 0.)
        self.mu = float(mu)

    def set_eta(self,beta):
        '''
        sets plastic dilatancy to new value
        '''
        assert(beta > 0.)
        self.beta = float(beta)

    def set_eta(self,eta):
        '''
        sets plastic viscosity to new value
        '''
        assert(eta > 0.)
        self.eta = float(eta)

    def __str__(self):
        '''
        returns string representation for printing
        '''
        return ('Material properties: density = ' + str(self.rho) + ', Lame parameter = ' + str(self.lam) +
                ', shear modulus = ' + str(self.g) + '\nInternal friction angle = ' + str(self.mu) +
                ', plastic dilatancy = ' + str(self.beta) + ', plastic viscosity = ' + str(self.eta))

