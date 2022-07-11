from parameters import parameters, id_eurofers
from solve_H_transport import run_H_transport


if __name__ == "__main__":

    S_0_eur_original = 2.4088e23

    reduction_factors = [
        1,
        10,
        100,
        200,
        300,
        400,
        500,
        600,
        700,
        800,
        900,
        1000,
        1e4,
        1e5,
        1e6,
        1e7,
    ]

    folder = "Results/parametric_studies/varying_perm_barrier"
    E_S_eurofer = 0.3026
    for reduction_factor in reduction_factors:
        reduced_S_0_eurofer = S_0_eur_original/reduction_factor
        for material in parameters["materials"]:
            if material["id"] in id_eurofers:
                material["S_0"] = reduced_S_0_eurofer
                material["E_S"] = E_S_eurofer

        results_folder = folder + '/S_0_eur={:.1e}'.format(reduced_S_0_eurofer)

        parameters['exports']["xdmf"]["folder"] = results_folder
        parameters['exports']["derived_quantities"]["folder"] = results_folder
        print('Current step is S_0_eur = {:.1e}'.format(reduced_S_0_eurofer))
        run_H_transport(parameters, log_level=40)
