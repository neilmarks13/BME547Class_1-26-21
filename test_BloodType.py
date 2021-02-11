def test_analyze_hdl():
    from BloodType import analyze_hdl
    assert "Normal" == analyze_hdl(65)