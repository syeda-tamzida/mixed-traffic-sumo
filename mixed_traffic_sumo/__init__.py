"""mixed-traffic-sumo: real-world mixed (heterogeneous) traffic scenarios for SUMO
and reinforcement-learning traffic signal control.

Scenarios include vehicle classes that are rare in public benchmarks, such as
rickshaws, CNG auto-rickshaws, tempos and human haulers.

    import mixed_traffic_sumo as mts
    env = mts.make_env("tigerpass")
"""
from importlib import resources
from pathlib import Path

__version__ = "0.2.0"
__all__ = ["SCENARIOS", "list_scenarios", "scenario_info", "scenario_files", "make_env", "make_parallel_env"]

_ROOT = Path(str(resources.files(__name__) / "scenarios"))

SCENARIOS = {
    "tigerpass": {
        "location": "Tigerpass intersection, Chattogram, Bangladesh",
        "type": "4-leg signalized intersection",
        "vehicle_mix": {
            "car": 0.26, "cng": 0.22, "motorcycle": 0.16, "bus": 0.11, "human_hauler": 0.07,
            "rickshaw": 0.06, "truck": 0.05, "tempu": 0.04, "bicycle": 0.03,
        },
        "demand_veh_per_hour": {
            "n_s": 534, "n_e": 395, "n_w": 346, "e_w": 346, "e_s": 316, "e_n": 314,
            "s_n": 585, "s_w": 226, "s_e": 454, "w_n": 274,
        },
    },
}


def list_scenarios():
    """Names of the available scenarios."""
    return sorted(SCENARIOS)


def scenario_info(name):
    """Location, type, vehicle mix and demand of a scenario."""
    _check(name)
    return SCENARIOS[name]


def scenario_files(name="tigerpass"):
    """Paths of the network, route and SUMO configuration files of a scenario."""
    _check(name)
    d = _ROOT / name
    return {"net_file": str(d / f"{name}.net.xml"),
            "route_file": str(d / f"{name}.rou.xml"),
            "sumocfg_file": str(d / f"{name}.sumocfg")}


def _check(name):
    if name not in SCENARIOS:
        raise ValueError(f"Unknown scenario '{name}'. Available: {', '.join(list_scenarios())}")


def _defaults(name, kwargs):
    f = scenario_files(name)
    kw = dict(net_file=f["net_file"], route_file=f["route_file"], num_seconds=3600,
              delta_time=5, yellow_time=3, min_green=10, use_gui=False)
    kw.update(kwargs)
    return kw


def make_env(scenario="tigerpass", **kwargs):
    """Single-agent Gymnasium environment built with ``sumo-rl``.

    Any ``sumo_rl.SumoEnvironment`` argument can be overridden, e.g.
    ``make_env("tigerpass", use_gui=True, num_seconds=1800)``.
    """
    from sumo_rl import SumoEnvironment
    return SumoEnvironment(single_agent=True, **_defaults(scenario, kwargs))


def make_parallel_env(scenario="tigerpass", **kwargs):
    """PettingZoo parallel environment built with ``sumo-rl``."""
    import sumo_rl
    return sumo_rl.parallel_env(**_defaults(scenario, kwargs))
