import numpy as np


def model_report(y_pred):
    report = {}
    report["high_IDC_regions"] = round((sum(y_pred >= 0.9) / len(y_pred) * 100)[0], 2)
    report["medium_IDC_regions"] = round(
        (sum((y_pred < 0.9) & (y_pred >= 0.6)) / len(y_pred) * 100)[0], 2
    )
    report["low_IDC_regions"] = round(
        (sum((y_pred >= 0.3) & (y_pred < 0.6)) / len(y_pred) * 100)[0], 2
    )
    report["no_IDC_regions"] = round(sum((y_pred < 0.3) / len(y_pred) * 100)[0], 2)
    return report


def recommend(report):
    recommendation = "No IDC detected."
    if report["high_IDC_regions"] != 0:
        recommendation = "Further testing strongly recommended."
    elif report["medium_IDC_regions"] != 0:
        recommendation = "Consider additional testing."
    elif report["low_IDC_regions"] != 0:
        recommendation = "Routine checkups recommended."
    return recommendation
