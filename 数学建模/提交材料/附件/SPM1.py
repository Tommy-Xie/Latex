import pybamm
import numpy as np
import matplotlib.pyplot as plt

model = pybamm.lithium_ion.SPM()
geometry = model.default_geometry

param = model.default_parameter_values
param.process_model(model)
param.process_geometry(geometry)
mesh = pybamm.Mesh(geometry, model.default_submesh_types, model.default_var_pts)
disc = pybamm.Discretisation(mesh, model.default_spatial_methods)
disc.process_model(model);



solver = model.default_solver
n = 250
t_eval = np.linspace(0, 3600, n)
print('Solving using',type(solver).__name__,'solver...')
solution = solver.solve(model, t_eval)
print('Finished.')

voltage = solution['Terminal voltage [V]']
current = solution['Current [A]']
Lithium_concentration = solution['Electrolyte concentration [mol.m-3]']
c_s_n_surf = solution['Negative particle surface concentration']
c_s_p_surf = solution['Positive particle surface concentration']
a = solution['Electrolyte potential [V]']

t = solution["Time [s]"].entries
x = solution["x [m]"].entries[:, 0]
f, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(1, 6, figsize=(13,6))

ax1.plot(t, voltage(t))
ax1.set_xlabel(r'$Time [s]$')
ax1.set_ylabel('Terminal voltage [V]')

ax2.plot(t, c_s_n_surf(t=t, x=x[0]))  # can evaluate at arbitrary x (single representative particle)
ax2.set_xlabel(r'$Time [s]$')
ax2.set_ylabel('Negative particle surface concentration')

ax3.plot(t, c_s_p_surf(t=t, x=x[-1]))  # can evaluate at arbitrary x (single representative particle)
ax3.set_xlabel(r'$Time [s]$')
ax3.set_ylabel('Positive particle surface concentration')

ax4.plot(t, current(t))  # can evaluate at arbitrary x (single representative particle)
ax4.set_xlabel(r'$Time [s]$')
ax4.set_ylabel('Current[A]')

ax5.plot(t, Lithium_concentration(t=t, x=x[-1]))  # can evaluate at arbitrary x (single representative particle)
ax5.set_xlabel(r'$Time [s]$')
ax5.set_ylabel('Electrolyte concentration [mol.m-3]')

ax6.plot(t, Lithium_concentration(t=t, x=x[-1]))  # can evaluate at arbitrary x (single representative particle)
ax6.set_xlabel(r'$Time [s]$')
ax6.set_ylabel('Electrolyte potential [V]')

plt.tight_layout()
plt.show()