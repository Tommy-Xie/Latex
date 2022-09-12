import pybamm

options1 = {"thermal": "isothermal"}
options2 = {"thermal": "lumped"}
options3 = {"thermal": "x-lumped"}
options4 = {"thermal": "x-full"}


models = [pybamm.lithium_ion.SPM(options=options1, name= "isothermal"),
          pybamm.lithium_ion.SPM(options=options2, name= "lumped"),
          pybamm.lithium_ion.SPM(options=options3, name= "x-lumped"),
          pybamm.lithium_ion.SPM(options=options4,name ="x-full"),
]
solutions = ["isothermal", "lumped", "x-lumped", "x-full"]
# solutions = [None] * 3

for i, model in enumerate(models):
    sim = pybamm.Simulation(model)
    sim.solve([0, 3700])
    solutions[i] = sim.solution


plot = pybamm.QuickPlot(solutions)
plot.dynamic_plot()