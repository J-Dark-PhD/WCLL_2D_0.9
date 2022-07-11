from parameters import parameters
from solve_H_transport import run_H_transport
import numpy as np


if __name__ == "__main__":

    test_values = [np.linspace(0, 1, num=11)]

    folder = "parametric_testing_inlet_conc"
    for eta in test_values:
        parameters['exports']["xdmf"]["folder"] = folder + \
            '/eta={:.1f}'.format(eta)
        parameters['exports']["derived_quantities"]["folder"] = folder + \
            '/eta={:.1f}'.format(eta)
        print('Current step is eta = {:.1f}'.format(eta))
        relative_error = 1  # initialise relative error
        average_concentration_outlet_old = 1.01741917005023E+21/0.061  # initialise average concentration outlet old to smth
        while relative_error > 0.01:
            # run FESTIM
            output = run_H_transport(parameters, log_level=20)

            # compute what the average conc at the outlet is
            index = np.where(np.array(output["derived_quantities"][0]) == "Total solute surface 21")
            average_concentration_outlet = output["derived_quantities"][1][index[0][0]]/0.061

            # modify the BC accordingly
            parameters["boundary_conditions"][0]["value"] = eta*average_concentration_outlet

            # compute the relative error
            relative_error = (average_concentration_outlet-average_concentration_outlet_old)/average_concentration_outlet_old
            # store the old value of conc outlet
            average_concentration_outlet_old = average_concentration_outlet
            print('relative error = ', relative_error)
            print('refining')
