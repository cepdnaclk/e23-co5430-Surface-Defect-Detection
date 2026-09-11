# 🔍 Steel Surface Defect Detection Using Deep Learning

A deep learning-based computer vision project for automatically classifying
surface defects in hot-rolled steel using the **NEU Surface Defect Database**.

This project was developed as part of **CO5430 – Image Processing** at the
Department of Computer Engineering, University of Peradeniya.

---

## 📌 Project Overview

Surface defects can significantly affect the quality and reliability of
manufactured steel products. Manual visual inspection can be time-consuming,
subjective and difficult to perform consistently.

This project investigates the use of deep learning for automatic steel surface
defect classification.

Four model configurations were evaluated:

- Baseline Convolutional Neural Network (CNN)
- MobileNetV2 with frozen pretrained features
- Fine-Tuned MobileNetV2
- ResNet18 using transfer learning

All final models were evaluated using the **same fixed train, validation and
test split** to ensure a fair comparison.

---

## 🏷️ Defect Classes

The system classifies steel surface images into six defect categories:

1. Crazing
2. Inclusion
3. Patches
4. Pitted Surface
5. Rolled-in Scale
6. Scratches

---

## 📊 Dataset

The project uses the **NEU Surface Defect Database**.

The dataset contains **1,800 grayscale images** distributed across six steel
surface defect categories.

Dataset preparation is performed in:

`notebooks/01_dataset_preparation.ipynb`

A fixed train/validation/test split was created and reused for the final
experiments.

```text
dataset/
└── split/
    ├── train/
    ├── validation/
    └── test/
```

The final split contains:

- Training: 1,260 images
- Validation: 270 images
- Testing: 270 images

This corresponds to a **70% / 15% / 15% split**.

The same exact split is reused by all models in the final controlled comparison.

---

## ☁️ Dataset & Trained Models

Large files such as the dataset splits and trained model weights are not stored
directly in the GitHub repository.

They are available through the project Google Drive:

**[📂 Open Project Google Drive](https://drive.google.com/drive/u/0/folders/1JdUyW7HmGCTe1weABU3nR1dOGsFM1_Ag)**

The Drive folder contains the files required for reproducing the experiments,
including the fixed dataset split and trained model files.

---

## 🧠 Models

### 1. Baseline CNN

A custom Convolutional Neural Network was trained from scratch to provide a
baseline for comparison with transfer-learning approaches.

Notebook:

`notebooks/02_baseline_cnn.ipynb`

Final Test Accuracy: **94.44%**

---

### 2. Frozen MobileNetV2

A MobileNetV2 model pretrained on ImageNet was adapted to the six-class surface
defect classification problem.

The pretrained feature extractor was frozen while the new classification head
was trained on the NEU dataset.

Notebook:

`notebooks/03_mobilenetv2.ipynb`

Final Test Accuracy: **99.63%**

---

### 3. Fine-Tuned MobileNetV2

The MobileNetV2 model was further improved by unfreezing selected pretrained
layers and fine-tuning them using a lower learning rate.

This allowed the pretrained features to adapt more closely to steel surface
textures.

Notebook:

`notebooks/03_mobilenetv2.ipynb`

Final Test Accuracy: **100.00%**

---

### 4. ResNet18

A pretrained ResNet18 architecture was trained using transfer learning on the
same fixed dataset split.

This experiment provided an additional transfer-learning architecture for
comparison with MobileNetV2.

Notebook:

`notebooks/04_resnet18.ipynb`

Final Test Accuracy: **98.15%**

---

## 📈 Final Results

All models were evaluated on the same held-out test set containing **270 images**.

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 |
|---|---:|---:|---:|---:|
| Baseline CNN | 94.44% | 94.45% | 94.44% | 94.42% |
| MobileNetV2 – Frozen | 99.63% | 99.64% | 99.63% | 99.63% |
| **MobileNetV2 – Fine-Tuned** | **100.00%** | **100.00%** | **100.00%** | **100.00%** |
| ResNet18 | 98.15% | 98.17% | 98.15% | 98.15% |

### Prediction Summary

| Model | Correct | Incorrect |
|---|---:|---:|
| Baseline CNN | 255 | 15 |
| MobileNetV2 – Frozen | 269 | 1 |
| **MobileNetV2 – Fine-Tuned** | **270** | **0** |
| ResNet18 | 265 | 5 |

### 🏆 Best Model

The **Fine-Tuned MobileNetV2** achieved the best overall performance:

- Test Accuracy: **100.00%**
- Macro Precision: **100.00%**
- Macro Recall: **100.00%**
- Macro F1-Score: **100.00%**
- Correct Predictions: **270 / 270**

These results demonstrate the effectiveness of transfer learning and
fine-tuning for steel surface defect classification on the selected test set.

---

## 📊 Evaluation

The models were evaluated using:

- Test Accuracy
- Macro Precision
- Macro Recall
- Macro F1-Score
- Confusion Matrices
- Training and Validation Accuracy
- Training and Validation Loss
- Qualitative Predictions
- Failure Case Analysis

The complete controlled comparison is available in:

`notebooks/05_final_evaluation.ipynb`

---

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/cepdnaclk/e23-co5430-Surface-Defect-Detection.git

cd e23-co5430-Surface-Defect-Detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Obtain the data and trained models

Download or access the required large files from:

**[Project Google Drive](https://drive.google.com/drive/u/0/folders/1JdUyW7HmGCTe1weABU3nR1dOGsFM1_Ag)**

---

## 👥 Team

| Student | Registration Number |
|---|---|
| K.K. Dilshara | E/23/075 |
| M.T.C. Newanma | E/23/244 |
| W.H.C.C. Samarasinghe | E/23/340 |
| K.K.S. Semindi | E/23/360 |

---

## 🎓 Course Information

**Course:** CO5430 – Image Processing 
**Project:** P17 – Surface Defect Detection  
**Category:** Industrial Inspection  
**Department:** Department of Computer Engineering  
**Institution:** University of Peradeniya  
**Year:** 2026
