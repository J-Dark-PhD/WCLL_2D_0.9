from fenics import *
from context import FESTIM as F
from properties import Cp_lipb, rho_lipb
from parameters import my_model


class AdvectionHeatTranfer(F.HeatTransferProblem):
    def __init__(self, u, rho, cp, **kwargs) -> None:
        super().__init__(**kwargs)
        self.u = u
        self.rho = rho
        self.cp = cp

    def define_variational_problem(self, materials, mesh, dt):
        super().define_variational_problem(materials, mesh, dt)
        # modify the form F
        print("hola chico im modifying")
        test_function_temp = self.v_T
        T = self.T
        dx = mesh.dx
        self.F += (
            self.rho(T)
            * self.cp(T)
            * inner(dot(grad(T), self.u), test_function_temp)
            * dx
        )


def heat_transfer_test(model):
    """ """
    # # read the u_full function written in solve_NS_submesh.py
    mesh = Mesh()
    XDMFFile("meshes/2D/mesh_fine/mesh_domains_fine.xdmf").read(mesh)

    V_ele = VectorElement("CG", mesh.ufl_cell(), 2)
    V_u = FunctionSpace(mesh, V_ele)

    mesh_cfd = "Results/velocity_fields/u_full_fine_buoyancy.xdmf"

    u = Function(V_u, name="velocity")
    XDMFFile(mesh_cfd).read_checkpoint(u, "u", -1)

    model.T = AdvectionHeatTranfer(
        u=u, rho=rho_lipb, cp=Cp_lipb, transient=False, linear_solver="mumps"
    )

    # run the simulation with the modified formulation
    model.initialise()
    T = my_model.T.T
    XDMFFile("Results/T_alt.xdmf").write(T)


if __name__ == "__main__":
    heat_transfer_test(my_model)
