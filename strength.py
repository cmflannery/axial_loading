import matplotlib.pyplot as plt
import numpy as np
import subprocess
import os

# cylinder obj
class airframe(object):
    """airframe creates an instance of an object that defines the properties of
    an axially loaded cylinder under various loading conditions and internal
    pressures"""
    def __init__(self):
        super(airframe, self).__init__()
        self.L = 120.0  # setting length of cylinder as a contant for now (inches)
        self.E = 10.0**7  # modulus of elasticity for AL 6061-T4 (psi)
        self.num_steps = 20

        self.get_pbar()
        self.get_p()
        self.get_delta_sigmacrbar()
        self.get_Rtratio()
        self.get_R()
        self.get_t()
        self.get_K0()
        self.get_sigmacrbar0()
        self.get_sigmacr_np()
        self.get_sigmacrbar_p()
        self.get_sigmacr_p()
        self.plot_sigmacr_np_v_tR()

    def get_pbar(self):
        """generate array of pbar values
        in the linear region as defined by
        Fung and Sechler"""
        self.pbar = np.linspace(0.1, 0.8, self.num_steps)

    def get_p(self):
        # self.p = np.linspace(0.0, 14.0, self.num_steps)
        self.p = 14.0  # setting as a constant for now; this should be changed later

    def get_delta_sigmacrbar(self):
        """constand defined by Fung and Sechler"""
        self.delta_sigmacrbar = np.linspace(0, 0.229, self.num_steps)

    def get_Rtratio(self):
        """get ratios of R/t based on each pbar value and p values"""
        self.Rtratio = np.sqrt(self.pbar/self.p*self.E)

    def get_R(self):
        """constant value defined by vehicle size"""
        self.R = 6.0  # inches

    def get_t(self):
        self.t = self.R/self.Rtratio

    def get_K0(self):
        """K0 is calculated from a formula derived from empirical measurements
        made by Fung et. Sechler"""
        self.K0 = self.Rtratio*(9*(1.0/self.Rtratio)**1.6 +
                                0.16*(self.t/self.L)**1.3)

    def get_sigmacrbar0(self):
        self.sigmacrbar0 = self.K0

    def get_sigmacr_np(self):
        """calculate sigmacr without internal pressure"""
        self.sigmacr_np = self.K0 * self.E / self.Rtratio

    def get_sigmacrbar_p(self):
        self.sigmacrbar_p = self.sigmacrbar0 + self.delta_sigmacrbar

    def get_sigmacr_p(self):
        self.sigmacr_p = self.sigmacrbar_p * self.E / self.Rtratio

    def plot_sigmacr_np_v_tR(self):
        with plt.xkcd():
            plt.plot(self.Rtratio, self.sigmacr_np, 'b', label='unpressurized')
            plt.plot(self.Rtratio, self.sigmacr_p, 'r', label='pressureized')
            plt.xlabel('R/t')
            plt.ylabel('Sigma_cr (psi)')
            plt.title('Strength of Thin Wall Cylinder under Axial Load')
            plt.legend(loc='upper right')
            plt.savefig(os.path.join(os.getcwd(), 'AxialStrengthRt.png'))
            plt.show()


if __name__ == "__main__":
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('cls', shell=True)

    LaunchySLV = airframe()
    # print 'pbar',
    # print LaunchySLV.pbar
    # print 'sigma_np',
    # print LaunchySLV.sigmacr_np
    # print 'sigma_p',
    # print LaunchySLV.sigmacr_p

    print('hello')
    LaunchySLV.plot_sigmacr_np_v_tR()
