import pytest
from math import isclose
from bolted_lap_joint_design import design_lap_joint, calculate_bolt_strength

@pytest.mark.parametrize("P", [0, 10, 25, 50, 75, 100])
@pytest.mark.parametrize("t1", [6, 8, 10, 12, 16, 20, 24])
@pytest.mark.parametrize("t2", [6, 8, 10, 12, 16, 20, 24])
def test_minimum_two_bolts_for_valid_range(P, t1, t2):
    try:
        result = design_lap_joint(P, w=100, t1=t1, t2=t2)
        assert result["number_of_bolts"] >= 2
    except ValueError:
        # If no suitable design is found for P=0 (or unrealistic combos), it's acceptable
        assert P == 0 or t1 + t2 < 10

def test_design_lap_joint_output_structure():
    result = design_lap_joint(P=100, w=150, t1=10, t2=12)
    assert isinstance(result, dict)
    required_keys = [
        "bolt_diameter", "bolt_grade", "number_of_bolts", "pitch_distance",
        "gauge_distance", "end_distance", "edge_distance", "number_of_rows",
        "number_of_columns", "hole_diameter", "strength_of_connection",
        "yield_strength_plate_1", "yield_strength_plate_2",
        "length_of_connection", "efficiency_of_connection"
    ]
    for key in required_keys:
        assert key in result

def test_efficiency_is_reasonable():
    result = design_lap_joint(P=80, w=120, t1=8, t2=10)
    assert result["efficiency_of_connection"] <= 1.0
    assert result["efficiency_of_connection"] > 0

def test_calculate_bolt_strength_for_grade():
    fu, fy = calculate_bolt_strength(4.6)
    assert isclose(fu, 400.0, rel_tol=1e-5)  # 4 × 100
    assert isclose(fy, 240.0, rel_tol=1e-5)  # 0.6 × 400

def test_no_design_found():
    with pytest.raises(ValueError, match="No suitable design found"):
        # Unrealistically high force and very small plate dimensions
        design_lap_joint(P=1e6, w=20, t1=1, t2=1)

def test_minimum_valid_input():
    result = design_lap_joint(P=30, w=100, t1=6, t2=6)
    assert isinstance(result, dict)
    assert result["number_of_bolts"] >= 3
    assert result["efficiency_of_connection"] <= 1.0
    assert result["efficiency_of_connection"] > 0
