"tests the output of io.py"
from titration.io import load_titration_csv

def test_load_titration_csv_reads_columns():
    filepath = "titration_template.csv"
    df = load_titration_csv(filepath) 
    assert not df.isna().any().any(), "expected = num pH and vol_mL readings"
def test_load_titration_csv_has_no_missing_pH():  
    filepath = "titration_template.csv"
    df = load_titration_csv(filepath)
    assert list(df.columns) == ["volume_mL", "pH"]