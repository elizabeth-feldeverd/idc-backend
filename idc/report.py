import numpy as np

def model_report(y_pred):
    report = {}
    report['mean_whole_slide'] = round(np.mean(y_pred)*100, 2)
    report['high_IDC_regions'] = round((sum(y_pred >= 0.9)/len(y_pred) * 100)[0], 2)
    report['medium_IDC_regions'] = round((sum((y_pred < 0.9) & (y_pred >= 0.6))/len(y_pred) * 100)[0], 2)
    report['low_IDC_regions'] = round((sum((y_pred >= 0.3) & (y_pred < 0.6))/len(y_pred) * 100)[0], 2)
    report['no_IDC_regions'] = round(sum((y_pred < 0.3)/len(y_pred) * 100)[0], 2)
    return report
