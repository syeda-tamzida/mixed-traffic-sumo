import os
import xml.etree.ElementTree as ET
import pytest
import mixed_traffic_sumo as mts


@pytest.mark.parametrize("name", mts.list_scenarios())
def test_files_exist(name):
    for path in mts.scenario_files(name).values():
        assert os.path.exists(path)


@pytest.mark.parametrize("name", mts.list_scenarios())
def test_vehicle_mix_matches_route_file(name):
    root = ET.parse(mts.scenario_files(name)["route_file"]).getroot()
    probs = sorted(float(v.get("probability")) for v in root.iter("vType"))
    assert sorted(mts.scenario_info(name)["vehicle_mix"].values()) == pytest.approx(probs)


@pytest.mark.parametrize("name", mts.list_scenarios())
def test_demand_matches_route_file(name):
    root = ET.parse(mts.scenario_files(name)["route_file"]).getroot()
    flows = {f.get("route"): int(float(f.get("vehsPerHour"))) for f in root.iter("flow")}
    assert flows == mts.scenario_info(name)["demand_veh_per_hour"]


def test_unknown_scenario():
    with pytest.raises(ValueError):
        mts.scenario_files("nowhere")
