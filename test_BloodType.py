import pytest

@pytest.mark.parametrize("number, level", [(65,"Normal"),(45,"Borderline Low"),(25,"Low")])
def test_analyze_hdl(number,level):
    from BloodType import analyze_hdl
    assert level == analyze_hdl(number)
    