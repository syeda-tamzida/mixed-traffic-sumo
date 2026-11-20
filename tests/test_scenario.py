import os
import xml.etree.ElementTree as ET
import tigerpass_traffic as tp


def test_files_exist():
    for path in tp.scenario_files().values():
        assert os.path.exists(path)


def test_vehicle_mix_matches_route_file():
    root = ET.parse(tp.ROUTE_FILE).getroot()
    probs = [float(v.get("probability")) for v in root.iter("vType")]
    assert len(probs) == 9
    assert abs(sum(probs) - 1.0) < 1e-6
    assert abs(sum(tp.VEHICLE_MIX.values()) - 1.0) < 1e-6


def test_demand_matches_route_file():
    root = ET.parse(tp.ROUTE_FILE).getroot()
    flows = {f.get("route"): int(float(f.get("vehsPerHour"))) for f in root.iter("flow")}
    assert flows == tp.DEMAND_VEH_PER_HOUR
