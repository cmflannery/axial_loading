import matplotlib.pyplot as plt
import numpy as np
import subprocess

# cylinder obj
class airframe(object):
    """airframe creates an instance of an object that defines the properties of
    an axially loaded cylinder under various loading conditions and internal
    pressures"""
    def __init__(self):
        super(airframe, self).__init__()
        self.L = 120.0  # setting length of cylinder as a contant for now (inches)
        self.E = 22000.0  # modulus of elasticity for AL 6061-T4 (psi)
        self.num_steps = 20

        self.get_t()
        self.get_R()
        self.get_K0()
        self.get_pbar()
        self.get_sigmacr_np()

        print self.sigmacr_np

    def get_t(self):
        """generate array of t values, assume units of inches"""
        self.t = np.linspace(0.001, 0.1, self.num_steps)

    def get_R(self):
        """generate array of R values; assume units of inches"""
        self.R = np.linspace(1.0, 8.0, self.num_steps)

    def get_K0(self):
        """K0 is calculated from a formula derived from empirical measurements
        made by Fung et. Sechler"""
        self.K0 = self.R/self.t*(9*(self.t/self.R)**1.6 +
                                 0.16*(self.t/self.L)**1.3)

    def get_p(self):
        self.p = np.linspace(0.0, 29.0)

    def get_pbar(self):
        self.pbar = (self.p/self.E)*(self.R/self.t)**2

    def get_sigmacr_np(self):
        """calculate sigmacr without internal pressure"""
        self.sigmacr_np = self.K0 * self.E * (self.t/self.R)

    def get_sigmacr_p(self):
        self.sigmacr_np = self.K0 * self.E * (self.t/self.R)

    def plot_sigmacr_np_v_tR(self):
        with plt.xkcd():
            plt.plot(self.t/self.R, self.sigmacr_np, 'b')
            plt.xlabel('t/R')
            plt.ylabel('Sigma_cr (psi)')
            plt.title('Strength of Thin Wall Cylinder under Axial Load (No Internal Pressure)')
            plt.show()


if __name__ == "__main__":
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('cls', shell=True)

    LaunchySLV = airframe()
    LaunchySLV.plot_sigmacr_np_v_tR()
