import pybamm

# load models
models = [
    pybamm.lithium_ion.SPM(
        options={"particle": "Fickian diffusion"}, name="Fickian diffusion"   # 菲克扩散
    ),
    pybamm.lithium_ion.SPM(
        options={"particle": "uniform profile"}, name="uniform profile"       # 统一轮廓，均匀分布
    ),
    pybamm.lithium_ion.SPM(
        options={"particle": "quadratic profile"}, name="quadratic profile"    # 二次曲线，二次分布
    ),
    pybamm.lithium_ion.SPM(
        options={"particle": "quartic profile"}, name="quartic profile"       # 四次轮廓，四次分布
    ),
]

experiment = pybamm.Experiment(
    [
        "Discharge at C/10 for 10 hours or until 3.3 V",
        "Rest for 1 hour",
        "Charge at 1 A until 4.1 V",
        "Hold at 4.1 V until 50 mA",
        "Rest for 1 hour",
    ]
)
# pick parameter values
# parameter_values = pybamm.ParameterValues("Ecker2015")parameter_values=parameter_values

# create and solve simulations
sims = []
for model in models:
    # sim = pybamm.Simulation(model,experiment=experiment)
    sim = pybamm.Simulation(model, experiment=experiment)
    sim.solve([0, 3600])
    sims.append(sim)
    print("Particle model: {}".format(model.name))
    print("Solve time: {}s".format(sim.solution.solve_time))

# plot results
pybamm.dynamic_plot(sims)
