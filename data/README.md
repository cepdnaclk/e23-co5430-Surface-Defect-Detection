# Dataset

This project uses the NEU Surface Defect Database for steel surface defect classification.

## Defect Classes

The dataset contains six surface defect categories:

1. Crazing
2. Inclusion
3. Patches
4. Pitted Surface
5. Rolled-in Scale
6. Scratches

## Dataset Structure

The original dataset is stored locally/Google Drive and is not included directly in this GitHub repository.

The dataset used during the experiments follows the structure:

data/
├── raw/
└── split/
    ├── train/
    ├── validation/
    └── test/

Each split contains separate folders for the six defect classes.

## Dataset Split

A fixed train/validation/test split was generated in
`notebooks/01_dataset_preparation.ipynb`.

The same exact split was used for all models:

- Baseline CNN
- MobileNetV2
- ResNet18

Using the same split ensures that the models are evaluated under identical conditions and allows a fair comparison.

## Important

The dataset is not regenerated separately for each model.

All training and evaluation notebooks use the existing split created during dataset preparation.

This prevents data leakage and ensures reproducibility of the experiments.

## Dataset Source

NEU Surface Defect Database.

The dataset can be obtained from the Kaggle NEU Surface Defect Database page.

See `notebooks/01_dataset_preparation.ipynb` for the complete dataset preparation and splitting procedure.