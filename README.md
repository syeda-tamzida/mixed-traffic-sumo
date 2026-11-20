# mixed-traffic-sumo

**Real-world mixed-traffic scenarios for SUMO and reinforcement-learning traffic signal control.**

Most public signal-control benchmarks contain only cars, buses and trucks. The scenarios in this package come from cities where traffic is **mixed and non-lane-based**: rickshaws, CNG auto-rickshaws, tempos, human haulers, motorcycles and bicycles share the road with cars and buses. They plug directly into [sumo-rl](https://github.com/LucasAlegre/sumo-rl), so any Gymnasium or PettingZoo agent can be trained on them.

## Scenarios

| Name | Location | Type | Vehicle classes |
|---|---|---|---|
| `tigerpass` | Tigerpass intersection, Chattogram, Bangladesh | 4-leg signalized intersection, 10 turning movements | 9 |

More scenarios are planned. Contributions of real-world mixed-traffic networks are welcome.

<p align="center"><img src="docs/tigerpass_network.png" width="70%" alt="Tigerpass SUMO network and turning movements"></p>

## Install

```bash
pip install git+https://github.com/syeda-tamzida/mixed-traffic-sumo
```

SUMO is installed automatically through the `eclipse-sumo` package. Set `SUMO_HOME` once:

```bash
export SUMO_HOME=$(python -c "import sumo; print(sumo.SUMO_HOME)")
```

## Quick start

```python
import mixed_traffic_sumo as mts

mts.list_scenarios()                          # ['tigerpass']
env = mts.make_env("tigerpass")               # Gymnasium environment
obs, info = env.reset(seed=0)
obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
```

- `mts.make_parallel_env("tigerpass")` returns a PettingZoo environment for multi-agent methods.
- Any `sumo_rl.SumoEnvironment` argument can be passed, e.g. `mts.make_env("tigerpass", use_gui=True)` to watch the simulation.
- `mts.scenario_files("tigerpass")` returns the raw `.net.xml`, `.rou.xml` and `.sumocfg` paths for direct SUMO use.
- `mts.scenario_info("tigerpass")` returns the location, vehicle mix and demand.

## Tigerpass traffic composition

| Vehicle class | Share | | Vehicle class | Share |
|---|---|---|---|---|
| Car | 26% | | Human hauler | 7% |
| CNG auto-rickshaw | 22% | | Rickshaw | 6% |
| Motorcycle | 16% | | Truck | 5% |
| Bus | 11% | | Tempo | 4% |
| | | | Bicycle | 3% |

Demand ranges from 226 to 585 vehicles per hour per turning movement. Each class has its own length, maximum speed and HBEFA emission class, so the scenario also supports emissions studies.

## Baselines: Tigerpass (1 simulated hour, seed 0)

| Controller | Mean waiting time (s) | Mean queued vehicles | Mean speed (m/s) |
|---|---|---|---|
| Fixed-time (original plan) | 21.0 | 89.3 | 0.95 |
| Random phase selection | 20.8 | 96.0 | 1.00 |

Reproduce with `python examples/fixed_time_baseline.py`. A DQN training script is in `examples/train_dqn.py` (`pip install "mixed-traffic-sumo[train]"`).

## Research using these scenarios

- Akter, S. T., Lamun, S. S. I., Ahmed, E., Sarkar, S., Roy, C. (2026). Machine Learning Based CO₂ Emission Prediction at an Urban Intersection under Heterogeneous Traffic Using SUMO Microsimulation. *IEEE QPAIN 2026*. [Paper](https://doi.org/10.1109/QPAIN69676.2026.11546352)
- Traffic Signal Control Optimization for Heterogeneous Traffic Using Reinforcement Learning (MPLight, IDQN vs. fixed time). Under review. [Code](https://github.com/syeda-tamzida/Traffic-Signal-Control-Optimization-for-Heterogeneous-Traffic-Using-Reinforcement-Learning)

## Citation

If you use these scenarios, please cite them (see `CITATION.cff`, or GitHub's "Cite this repository" button).

## License

MIT. The environment wrappers use [sumo-rl](https://github.com/LucasAlegre/sumo-rl) by Lucas N. Alegre.
