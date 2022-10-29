# Project overview
- Project title: Predicting Invasive Ductal Carcinoma (IDC) in Breast Cancer Histology Images

- Authors: Elizabeth (Feldeverd) Oda, Jack Claar, and Nadia Yap

- Description: The objective of this project is to identify invasive ductal carcinoma (IDC) within breast histology images using deep learning. The model architecture is based on AlexNet (Krizhevsky et al. 2012). The probabilities of IDC determined by the model are used to generate a heatmap using gradient class activation mapping, or Grad CAM. The heatmap is superimposed on the original histology image, highlighting the regions of concern.

- Data Source: Whole-slide breast cancer specimens at 40X were originally obtained and annotated by Cruz-Roa et al. (2014). For this project, we used the smaller "Breast Histology Images" dataset available on Kaggle.

- Performance: Our model can detect IDC with 84.9% recall and 74.1% precision. The F1 score is 0.792 and the balanced accuracy is 0.774.

- Our app can be found here: https://share.streamlit.io/jkclaar/idc-frontend/app.py

- This project was completed as part of the Le Wagon Tokyo Data Science course in December 2021 (Batch #728). This model is for educational purposes only and should not be used as a diagnostic tool.

# Install

This repository uses [Poetry](https://python-poetry.org/docs/) to manage dependencies. Please install `poetry==1.2.2` or another compatible version.

After cloning the repository, install dependencies by using:
```
poetry install
```

[DVC](https://dvc.org/) is used to version data and models. If you want to train your own model, the easiest open is to access the data directly from Kaggle. However, if you would like access to the data and models stored remotely in a private Google drive, just contact me.


# References

"Breast Histology Images" dataset from [Kaggle](https://www.kaggle.com/simjeg/lymphoma-subtype-classification-fl-vs-cll).

Chollet, F. (2020). Grad-CAM class activation visualization. https://keras.io/examples/vision/grad_cam/

Cruz-Roa, A., Basavanhally, A., González, F.A., Gilmore, H., Feldman, M.D., Ganesan, S., Shih, N., Tomaszeweski, J.E., & Madabhushi, A. (2014). Automatic detection of invasive ductal carcinoma in whole slide images with convolutional neural networks. Medical Imaging. DOI:10.1117/12.2043872

Janowczyk, A. (2015). USE CASE 6: INVASIVE DUCTAL CARCINOMA (IDC) SEGMENTATION. http://www.andrewjanowczyk.com/use-case-6-invasive-ductal-carcinoma-idc-segmentation/

Janowczyk, A., & Madabhushi, A. (2016). Deep learning for digital pathology image analysis: A comprehensive tutorial with selected use cases. Journal of pathology informatics, 7, 29. DOI: 10.4103/2153-3539.186902.

Krizhevsky, A., Sutskever, I., Hinton, G. E. (2012). "ImageNet classification with deep convolutional neural networks." Advances in Neural Information Processing Systems 25 (NIPS 2012). [Paper link](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf).
