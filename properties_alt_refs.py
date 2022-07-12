import matplotlib.pyplot as plt
import numpy as np

k_B = 8.6e-5

# ##### Tungsten ######
#
# Taken from (P.Tolias, 2017)


def Cp_W(T, main=False):  # units in J/(kg*K)
    return (
        21.868372
        + 8.068661e-03 * T
        - 1e-06 * T**2
        + 1.075862e-09 * T**3
        + 1.406637e04 / T**2
    )


def rho_W(T, main=False):  # units in kg/m**3
    """
    (adjusted by factor 1000 as orginial equation in g/cm**3)
    """
    T_W_0 = 293.15
    return (
        19250
        - 2.66207e-01 * (T - T_W_0)
        - 3.0595e-06 * (T - T_W_0) ** 2
        - 9.5185e-09 * (T - T_W_0) ** 3
    )


def thermal_cond_W(T, main=False):  # units in W/(m*K)
    return (
        149.441
        - 45.466e-03 * T
        + 13.193e-06 * T**2
        - 1.484e-09 * T**3
        + 3.866e06 / (T + 1) ** 2
    )
    # (T+1) is there to avoid dividing by 0


# taken from (Frauenfelder, R. 1969)
D_0_W = 2.4e-7  # Diffusivity coefficient pre-exponential factor (m)
E_D_W = 0.39  # Diffusivity coefficient activation energy (eV)
S_0_W = 1.87e24  # Solubility coefficient pre-exponential factor
E_S_W = 1.04  # Solutbiility coefficient activation energy (eV)

atom_density_W = 6.3222e28


def D_W(T, main=False):
    return D_0_W * np.exp(-E_D_W / k_B / T)


def S_W(T, main=False):
    return S_0_W * np.exp(-E_S_W / k_B / T)


# ##### EUROfer ######
#
#   Values taken from Materials properties handbook


def Cp_eurofer(T, main=False):  # units in J/(kg*K)
    return -139.66 + 3.4777 * T - 0.0063847 * T**2 + 4.0984e-06 * T**3


# def Cp_eurofer_2(T, main=False):  # units in J/(kg*K)(Mergia)
#     return 2.696*T - 0.00496*T**2 + 3.335e-06*T**3


def rho_eurofer(T, main=False):  # units in kg/m**3
    return 7852.102143 - 0.331026405 * T


def thermal_cond_eurofer(T, main=False):  # units in W/(m*K)
    return 5.4308 + 0.13565 * T - 2.3862e-04 * T**2 + 1.3393e-07 * T**3


# # taken from (Esteban, 2007)
D_0_eurofer_esteban = 1.33e-06  # Diffusivity coefficient pre-exponential factor (m2/s)
E_D_eurofer_esteban = 0.315  # Diffusivity coefficient activation energy (eV)
S_0_eurofer_esteban = (
    5.5463e21  # Solubility coefficient pre-exponential factor (atom/m3 Pa^-0.5)
)
E_S_eurofer_esteban = 0.0434  # Solutbiility coefficient activation energy (eV)a

# taken from (Chen, 2021)
D_0_eurofer = 3.15e-08  # Diffusivity coefficient pre-exponential factor (m2/s)
E_D_eurofer = 0.0622  # Diffusivity coefficient activation energy (eV)
S_0_eurofer = (
    2.4088e23  # Solubility coefficient pre-exponential factor (atom/m3 Pa^-0.5)
)
E_S_eurofer = 0.3026  # Solutbiility coefficient activation energy (eV)

atom_density_eurofer = 8.409e28  # (m-3)
trap_density_eurofer = 4.5e23  # (m-3)
trap_energy_eurofer = 0.7804  # (eV)

# taken from (Aiello, 2002)
D_0_eurofer_3 = 1.5e-07  # Diffusivity coefficient pre-exponential factor (m2/s)
E_D_eurofer_3 = 0.1503  # Diffusivity coefficient activation energy (eV)
S_0_eurofer_aiello = (
    6.1424e22  # Solubility coefficient pre-exponential factor (atom/m3 Pa^-0.5)
)
E_S_eurofer_aiello = 0.2467  # Solutbiility coefficient activation energy (eV)


# recombination coefficient
Kr_0_eurofer = 1.4143446334700682e-26
E_Kr_eurofer = -0.25727457261201786  # WAAARNIIING THIS HAS TO BE NEGATIIIIIVE!!!!!!


# recombination coefficient from Braun (1980)
# Kr_0_eurofer = 5.9680e-17
# E_Kr_eurofer = 0.888

# recombination coefficient from Esteban (2000)
# Kr_0_eurofer = 4.7127e-31
# E_Kr_eurofer = 2.471


def D_eurofer(T, main=False):
    return D_0_eurofer * np.exp(-E_D_eurofer / k_B / T)


def S_eurofer(T, main=False):
    return S_0_eurofer * np.exp(-E_S_eurofer / k_B / T)


def S_eurofer_esteban(T, main=False):
    return S_0_eurofer_esteban * np.exp(-E_S_eurofer_esteban / k_B / T)


def S_eurofer_aiello(T, main=False):
    return S_0_eurofer_aiello * np.exp(-E_S_eurofer_aiello / k_B / T)


# ##### LiPi ######
#
#  Values taken from (D.Martelli et al, 2019)


def Cp_lipb(T, main=False):  # units in J/(kg*K)
    """
    adjusted by factor 1000 as orginial equation in J/(g*K)
    for values of temperature 508K < T < 800K,
    """
    return 195 - 9.116e-03 * T


def rho_lipb(T, main=False):  # units in kg/(m**3)
    return 10520.35 - 1.19051 * T


def thermal_cond_lipb(T, main=False):  # units in W/(m*K)
    """
    adjusted by factor 100 as original equation in W/(cm*K))
    """
    return 9.14779235 + 0.019631 * T


def visc_lipb(T, main=False):  # units (Pa s)
    # return 0.0061091 - 2.2574e-05*(T - 273.15) + 3.766e-08*(T - 273.15)**2 - 2.2887e-11*(T - 273.15)**3
    return (
        0.01555147189
        - 4.827051855e-05 * T
        + 5.641475215e-08 * T**2
        - 2.2887e-11 * T**3
    )


def beta_lipb(T, main=False):  # units in K-1
    return 1.1221e-04 + 1.531e-08 * T


rho_0_lipb = 9808.2464435  # value T = 300K, units in kg/(m**3)

# taken from (Reiter, 1990)
D_0_lipb = 4.03e-08  # Diffusivity coefficient pre-exponential factor
E_D_lipb = 0.2021  # Diffusivity coefficient activation energy (eV)

# taken from (Aiello, 2008)
S_0_lipb = 1.427214e23  # Solubility coefficient pre-exponential factor
E_S_lipb = 0.133  # Solutbiility coefficient activation energy (eV)


def D_lipb(T, main=False):
    return D_0_lipb * np.exp(-E_D_lipb / k_B / T)


def S_lipb(T, main=False):
    return S_0_lipb * np.exp(-E_S_lipb / k_B / T)


# ##### Literature review
# taken from (Reiter, 1990)
S_0_lipb_reiter_H = 4.4310e20  # Solubility coefficient pre-exponential factor
E_S_lipb_reiter_H = 0.01399  # Solutbiility coefficient activation energy (eV)

S_0_lipb_reiter_D = 4.2857e20  # Solubility coefficient pre-exponential factor
E_S_lipb_reiter_D = 0.01399  # Solutbiility coefficient activation energy (eV)

S_0_lipb_reiter_T = 4.2131e20  # Solubility coefficient pre-exponential factor
E_S_lipb_reiter_T = 0.01399  # Solutbiility coefficient activation energy (eV)

# taken from (Aiello, 2008)
S_0_lipb_aiello = 1.427214e23  # Solubility coefficient pre-exponential factor
E_S_lipb_aiello = 0.133  # Solutbiility coefficient activation energy (eV)

# taken from G.Alberro 2015
S_0_lipb_alberro = 5.203e21  # Solubility coefficient pre-exponential factor
E_S_lipb_alberro = 0.00938  # Solutbiility coefficient activation energy (eV)

# taken from Chan and Veleski 1984
S_0_lipb_chan = 8.535e21  # Solubility coefficient pre-exponential factor
E_S_lipb_chan = 0.0933  # Solutbiility coefficient activation energy (eV)

# taken from Schumacher 1990
S_0_lipb_schumacher = 1.6131e22  # Solubility coefficient pre-exponential factor
E_S_lipb_schumacher = 0.0632  # Solutbiility coefficient activation energy (eV)


def S_lipb_reiter_H(T, main=False):
    return S_0_lipb_reiter_H * np.exp(-E_S_lipb_reiter_H / k_B / T)


def S_lipb_reiter_D(T, main=False):
    return S_0_lipb_reiter_H * np.exp(-E_S_lipb_reiter_H / k_B / T)


def S_lipb_reiter_T(T, main=False):
    return S_0_lipb_reiter_H * np.exp(-E_S_lipb_reiter_H / k_B / T)


def S_lipb_aillo(T, main=False):
    return S_0_lipb_aiello * np.exp(-E_S_lipb_aiello / k_B / T)


def S_lipb_alberro(T, main=False):
    return S_0_lipb_alberro * np.exp(-E_S_lipb_alberro / k_B / T)


def S_lipb_chan(T, main=False):
    return S_0_lipb_chan * np.exp(-E_S_lipb_chan / k_B / T)


def S_lipb_schumacher(T, main=False):
    return S_0_lipb_schumacher * np.exp(-E_S_lipb_schumacher / k_B / T)


# Testing
# print(thermal_cond_W(600))
# print(rho_W(600))
# print(Cp_W(600))

# print(rho_eurofer(600))
# print(Cp_eurofer(600))
# print(thermal_cond_eurofer(600))

# print(rho_lipb(600))
# print(Cp_lipb(600))
# print(thermal_cond_lipb(600))
# print(visc_lipb(600))
# print(beta_lipb(600))

# print(Cp_eurofer(700))
# print(Cp_eurofer_2(700))

# print(rho_W(400))
# print(rho_eurofer(400))
# print(rho_lipb(400))
# print(rho_W(900))
# print(rho_eurofer(900))
# print(rho_lipb(900))


# ##### Plotting Data ##### #

if __name__ == "__main__":

    def tick_function(X):
        V = 1000 / (X)
        return ["%.0f" % z for z in V]

    T = np.arange(500, 900, step=1)
    T_reiter = np.arange(508, 700, step=1)
    T_aiello = np.arange(600, 900, step=1)
    T_alberro = np.arange(523, 922, step=1)
    T_schumacher = np.arange(508, 1040, step=1)
    T_chan = np.arange(573, 773, step=1)
    grey_W = (228 / 255, 146 / 255, 64 / 255)
    # orange_eurofer = (228/255, 146/255, 64/255)
    orange_eurofer = "grey"
    # yellow_lipb = (180/255, 95/255, 6/255)
    yellow_lipb = "green"

    # plt.style.use('ggplot')

    # x = ['Tungsten', 'EUROFER', 'LiPb']
    # density_H = [19085, 7554, 9449]
    # density_C = [19222, 7720, 10044]

    # x_pos = [i for i, _ in enumerate(x)]

    # plt.bar(x_pos, density_C, label="T = 400K", color='red')
    # plt.bar(x_pos, density_H, label="T = 900K", color='green')
    # plt.xlabel("Material")
    # plt.ylabel("Density (kgm-3)")
    # plt.legend()
    # # plt.title("Energy output from various fuel sources")

    # plt.xticks(x_pos, x)

    # plt.show()

    # ax1.minorticks_on()
    # ax1.grid(which='minor', alpha=0.5)
    # ax1.grid(which='major', alpha=1.0)
    # ax1.legend()
    # ax1.set_ylabel(r"$D$ (m$^{2}$ s$^{-1}$)")
    # ax1.set_xlabel(r"T (K)")

    # plt.figure()

    # plt.yscale("log")
    # plt.plot(T, rho_W(T, main=True), label="W", color=grey_W)
    # plt.plot(T, rho_eurofer(T, main=True), label="Eurofer", color=orange_eurofer)
    # plt.plot(T, rho_lipb(T, main=True), label="LiPb", color=yellow_lipb)
    # plt.xlabel(r"T (K)")
    # plt.ylim(bottom=0)
    # plt.ylabel(r"$\rho$ (Kg m$^{-3}$)")
    # plt.figure()
    # plt.xlabel(r"T (K)")
    # plt.xlabel(r"T (K)")
    # plt.ylabel(r"C$_p$ (J kg$^{-1}$ K$^{-1}$)")
    # plt.plot(T, Cp_W(T, main=True), label="W", color=grey_W)
    # plt.plot(T, Cp_eurofer(T, main=True), label="Eurofer", color=orange_eurofer)
    # plt.plot(T, Cp_lipb(T, main=True), label="LiPb", color=yellow_lipb)

    # plt.xlabel(r"T (K)")
    # plt.ylabel(r"$\lambda$ (W m$^{-1}$ K$^{-1}$)")
    # plt.yscale("log")
    # plt.plot(T, thermal_cond_W(T, main=True), label="W", color=grey_W)
    # plt.plot(T, thermal_cond_eurofer(T, main=True), label="Eurofer", color=orange_eurofer)
    # plt.plot(T, thermal_cond_lipb(T, main=True), label="LiPb", color=yellow_lipb)

    # plt.xlabel(r"1000/T (K)")
    # plt.ylabel(r"Diffusivity (m$^{2}$ s$^{-1}$)")
    # plt.yscale("log")
    # plt.plot(1000/T, D_W(T, main=True), label="W", color=grey_W)
    # # plt.plot(1000/T, D_eurofer(T, main=True), label="Eurofer (Esteban, 2007)", color=orange_eurofer)
    # plt.plot(1000/T, D_eurofer(T, main=True), label="Eurofer", color=orange_eurofer)
    # # plt.plot(1000/T, D_eurofer(T, main=True), label="Eurofer (Aiello, 2002)", color=orange_eurofer)
    # plt.plot(1000/T, D_lipb(T, main=True), label="LiPb", color=yellow_lipb)

    plt.xlabel(r"1000/T (K)")
    plt.ylabel(r"Solubility (m$^{-3}$Pa$^{-0.5}$)")
    plt.yscale("log")
    # plt.plot(1000/T, S_W(T, main=True), label="W", color=grey_W)
    plt.plot(
        1000 / T,
        S_eurofer_esteban(T, main=True),
        label="Eurofer (Esteban, 2007)",
        color="red",
    )
    plt.plot(
        1000 / T, S_eurofer(T, main=True), label="Eurofer (Chen, 2021)", color="green"
    )
    plt.plot(
        1000 / T,
        S_eurofer_aiello(T, main=True),
        label="Eurofer (Aiello, 2002)",
        color="black",
    )
    # plt.plot(1000/T_reiter, S_lipb_reiter_H(T_reiter, main=True), label="H (Reiter'90)")
    # plt.plot(1000/T_reiter, S_lipb_reiter_D(T_reiter, main=True), label="D (Reiter'90)")
    # plt.plot(1000/T_reiter, S_lipb_reiter_T(T_reiter, main=True), label="T (Reiter'90)")
    # plt.plot(1000/T_aiello, S_lipb_aillo(T_aiello, main=True), label="H (Aiello'08)")
    # plt.plot(1000/T_alberro, S_lipb_alberro(T_alberro, main=True), label="T (Alberro'15)")
    # plt.plot(1000/T_chan, S_lipb_chan(T_chan, main=True), label="H (Chan'84)")
    # plt.plot(1000/T_schumacher, S_lipb_schumacher(T_schumacher, main=True), label="H (Schumacher'90)")

    # plt.xlabel(r"T (K)")
    # plt.ylabel(r"Viscosity (Pa s)")
    # plt.plot(T, visc_lipb(T, main=True), label="LiPb", color=yellow_lipb)

    # plt.xlabel(r"T (K)")
    # plt.ylabel(r"Thermal expansion coefficient")
    # plt.plot(T, beta_lipb(T, main=True), label="LiPb", color=yellow_lipb)

    plt.legend()
    plt.minorticks_on()
    plt.grid(which="minor", alpha=0.3)
    plt.grid(which="major", alpha=0.7)
    plt.show()
