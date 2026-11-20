"""Tigerpass: a real-world heterogeneous-traffic intersection scenario for SUMO.

The Tigerpass intersection in Chattogram, Bangladesh, carries nine vehicle classes,
including rickshaws, CNG auto-rickshaws, tempos and human haulers, which are rarely
found in public traffic-simulation benchmarks.
"""
from importlib import resources
from pathlib import Path

__version__ = "0.1.0"
__all__ = ["NET_FILE", "ROUTE_FILE", "SUMOCFG_FILE", "VEHICLE_MIX", "DEMAND_VEH_PER_HOUR",
           "scenario_files", "make_env", "make_parallel_env"]

_SCEN = Path(str(resources.files(__name__) / "scenarios"))
NET_FILE = str(_SCEN / "tigerpass.net.xml")
ROUTE_FILE = str(_SCEN / "tigerpass.rou.xml")
SUMOCFG_FILE = str(_SCEN / "tigerpass.sumocfg")

#: Share of each vehicle class in the generated traffic.
VEHICLE_MIX = {
    "car": 0.26, "cng": 0.22, "motorcycle": 0.16, "bus": 0.11, "human_hauler": 0.07,
    "rickshaw": 0.06, "truck": 0.05, "tempu": 0.04, "bicycle": 0.03,
}

#: Turning-movement demand (vehicles per hour), keyed "origin_destination" (n/e/s/w).
DEMAND_VEH_PER_HOUR = {
    "n_s": 534, "n_e": 395, "n_w": 346, "e_w": 346, "e_s": 316, "e_n": 314,
    "s_n": 585, "s_w": 226, "s_e": 454, "w_n": 274,
}


def scenario_files():
    """Return the paths of the network, route and configuration files."""
    return {"net_file": NET_FILE, "route_file": ROUTE_FILE, "sumocfg_file": SUMOCFG_FILE}


def _defaults(kwargs):
    kw = dict(net_file=NET_FILE, route_file=ROUTE_FILE, num_seconds=3600,
              delta_time=5, yellow_time=3, min_green=10, use_gui=False)
    kw.update(kwargs)
    return kw


def make_env(**kwargs):
    """Single-agent Gymnasium environment (requires ``sumo-rl``).

    Any keyword argument of ``sumo_rl.SumoEnvironment`` can be overridden,
    for example ``make_env(use_gui=True, num_seconds=1800)``.
    """
    from sumo_rl import SumoEnvironment
    return SumoEnvironment(single_agent=True, **_defaults(kwargs))


def make_parallel_env(**kwargs):
    """PettingZoo parallel environment (requires ``sumo-rl``)."""
    import sumo_rl
    return sumo_rl.parallel_env(**_defaults(kwargs))
