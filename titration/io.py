"""Loading and validating titration data (CSV/Excel with columns volume_mL, pH)."""
import pandas as pd
def load_titration_csv(file_path):
    """loads the titration data from a CSV file

    Takes that csv and returns the volume (mL) and pH"""
    df = pd.read_csv(file_path, comment="#")
    return df