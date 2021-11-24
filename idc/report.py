import numpy as np

def binary_predict(y_pred, custom_threshold=0.44):
    return (y_pred > custom_threshold).astype(int)

def model_diagnosis(y_pred):
    # Probability ranges from Cruz-Roa et al. (2014)
    mean_prob = np.mean(y_pred)
    if mean_prob >= 0.9:
        return 'High IDC probability'
    elif mean_prob >= 0.6:
        return 'Medium IDC probability'
    return 'Low IDC probability'

def generate_report(y_pred):
    report = {}

    # Converts probabilities into binary. Can pass custom threshold.
    y_binary = binary_predict(y_pred)

    # Returns the sum of 50x50 images deemed positive for IDC
    report['sum_positive'] = sum(y_binary)[0]

    # Returns the percent of images deemed positive for IDC
    report['percent_positive'] = round(
        (report['sum_positive'] / y_pred.shape[0]) * 100, 2)

    # Returns the mean probability of IDC across all images
    report['mean_probability'] = round(np.mean(y_pred) * 100, 2)

    # Returns a string (e.g. High IDC probability)
    report['model_diagnosis'] = model_diagnosis(y_pred)
    return report
