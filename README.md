# Project overview
- Project title: Predicting IDC in Breast Cancer Histology Images

- Authors: Jack Claar, Elizabeth Feldeverd, and Nadia Yap

- Description: The objective of this project is to identify invasive ductal carcinoma (IDC) within breast histology images using a
Convolutional Neural Network (CNN) model. The probabilities determined by the model are then used to generate a heatmap using Grad CAM. The heatmap is superimposed on the original histology image, highlighting the regions of concern.

- Data Source: Whole-slide breast cancer specimens at 40X were originally obtained and annotated by Cruz-Roa et al. (2014). For this project, we used the smaller "Breast Histology Images" dataset available on Kaggle.

- Performance: Our model can detect IDC with 84.9% recall and 74.1% precision. The F1 score is 0.792 and the balanced accuracy is 0.774.

- Our app can be found here: https://share.streamlit.io/jkclaar/idc-frontend/app.py

- This project was completed as part of the Le Wagon Tokyo Data Science course (Batch #728). This model is for educational purposes only and should not be used as a diagnostic tool.


# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for idc in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/idc`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "idc"
git remote add origin git@github.com:{group}/idc.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
idc-run
```

# Install

Go to `https://github.com/{group}/idc` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/idc.git
cd idc
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
idc-run
```
# References

"Breast Histology Images" dataset from Kaggle: https://www.kaggle.com/simjeg/lymphoma-subtype-classification-fl-vs-cll.

Chollet, F. (2020). Grad-CAM class activation visualization. https://keras.io/examples/vision/grad_cam/

Cruz-Roa, A., Basavanhally, A., González, F.A., Gilmore, H., Feldman, M.D., Ganesan, S., Shih, N., Tomaszeweski, J.E., & Madabhushi, A. (2014). Automatic detection of invasive ductal carcinoma in whole slide images with convolutional neural networks. Medical Imaging. DOI:10.1117/12.2043872

Janowczyk, A. (2015). USE CASE 6: INVASIVE DUCTAL CARCINOMA (IDC) SEGMENTATION. http://www.andrewjanowczyk.com/use-case-6-invasive-ductal-carcinoma-idc-segmentation/

Janowczyk, A., & Madabhushi, A. (2016). Deep learning for digital pathology image analysis: A comprehensive tutorial with selected use cases. Journal of pathology informatics, 7, 29. DOI: 10.4103/2153-3539.186902
