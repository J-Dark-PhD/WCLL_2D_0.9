from fenics import *
from context import FESTIM as F
from properties import S_0_lipb, E_S_lipb

from parameters import my_model, id_lipb


def run_H_transport(model, S_0_lipb=S_0_lipb, E_S_lipb=E_S_lipb):
    """Runs a hydrogen transport simulation projecting a predefined velcoity field onto
    a given mesh, accounting for advection

    Args:
        parameters ([type]): [description]
        S_0_lipb (float, optional): pre-exponential factor of solubility in
            LiPb. Defaults to S_0_lipb.
        E_S_lipb (float, optional): activation energy of solubility in LiPb.
            Defaults to E_S_lipb.
        log_level (int, optional): [description]. Defaults to 20.

    Returns:
        [type]: [description]
    """
    # create a simulation with these normal parameters
    model.initialise()

    # # read the u_full function written in solve_NS_submesh.py
    # mesh = model.mesh.mesh
    mesh = Mesh()
    XDMFFile("meshes/2D/mesh_fine/mesh_domains_fine.xdmf").read(mesh)

    V_ele = VectorElement("CG", mesh.ufl_cell(), 2)
    V_u = FunctionSpace(mesh, V_ele)

    # mesh_cfd = "Results/velocity_fields/u_full_fine_buoyancy.xdmf"
    mesh_cfd = "Results/u.xdmf"
    # mesh_cfd = "Results/u_full_fine.xdmf"
    # # if "type" in parameters["solving_parameters"]:
    # #     if parameters["solving_parameters"]["type"] == "solve_stationary":
    # #         mesh_cfd = "Results/velocity_fields/u_full_fine_buoyancy.xdmf"
    u = Function(V_u, name="velocity")
    XDMFFile(mesh_cfd).read_checkpoint(u, "u", -1)

    # modify the form F
    id_flow = id_lipb
    test_function_solute = model.h_transport_problem.mobile.test_function
    # solute = split(model.h_transport_problem.u)[0]
    solute = model.h_transport_problem.mobile.solution
    dx = model.mesh.dx
    S_lipb = S_0_lipb * exp(-E_S_lipb / F.k_B / model.T.T)
    model.h_transport_problem.F += inner(
        dot(grad(S_lipb * solute), u), test_function_solute
    ) * dx(id_flow)

    # run the simulation with the modified formulation
    model.run()


if __name__ == "__main__":
    run_H_transport(my_model)
