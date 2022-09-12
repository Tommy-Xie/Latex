import pybamm

pybamm.set_logging_level("INFO")

# load models
model = pybamm.lithium_ion.SPM(),


# create and run simulations
sims = []

sim = pybamm.Simulation(model)
sim.solve([0, 3600])
sims.append(sim)

# plot
pybamm.dynamic_plot(sims)