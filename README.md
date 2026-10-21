# ML Pipeline Demo

A machine learning pipeline project that demonstrates how to organize and execute an end-to-end ML workflow using Python and DVC (Data Version Control).

The pipeline is divided into stages for data ingestion, preprocessing, feature engineering, model building, and model evaluation. DVC tracks pipeline dependencies and outputs so that stages can be reproduced when relevant inputs or code change.

## Project Overview

This project demonstrates:

- Modular organization of machine learning code.
- Data ingestion and text preprocessing.
- Feature engineering using a Bag-of-Words (BoW) representation.
- Model training and serialization.
- Evaluation using accuracy, ROC-AUC, macro precision, and macro recall.
- Pipeline orchestration and reproducibility with DVC.
- Source-code version control with Git and GitHub.

> **Current evaluation snapshot:** Accuracy: 0.68562, ROC-AUC: 0.65295, macro precision: 0.71096, macro recall: 0.58792. These are the latest reported results in this repository's development workflow and may change when the data, code, or model configuration changes.

## Pipeline Architecture

```text
Data Source
    |
    v
Data Ingestion
    |
    v
Data Preprocessing
    |
    v
Feature Engineering
    |
    v
Model Building
    |
    v
Model Evaluation
    |
    v
metrics.json
```

DVC defines and manages the stages in `dvc.yaml`. The pipeline is executed in dependency order, and DVC can skip stages whose dependencies and outputs have not changed.

## Project Structure

```text
ML-PIPELINE-DEMO/
├── .dvc/
├── data/
│   ├── .gitignore
│   ├── raw/                  # Ingested data (managed by DVC / ignored by Git)
│   ├── processed/            # Cleaned data (managed by DVC / ignored by Git)
│   └── features/             # Engineered features (managed by DVC / ignored by Git)
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_building.py
│   └── model_evaluation.py
├── .gitignore
├── dvc.yaml                  # Pipeline stage definitions
├── dvc.lock                  # Locked pipeline dependencies and outputs
├── params.yaml               # Pipeline/model parameters, if configured
├── metrics.json              # Latest evaluation metrics
└── README.md
```

The exact contents of the `data/` folders depend on whether the pipeline has been run and whether the DVC-tracked artifacts have been pulled or reproduced.

## Tech Stack

- **Python** — pipeline implementation
- **Pandas** — tabular data handling
- **Scikit-learn** — machine learning utilities and evaluation metrics
- **NLTK** — text-processing resources used by the preprocessing workflow
- **DVC** — pipeline orchestration and data/artifact versioning
- **Git and GitHub** — source-code version control

Install only the dependencies required by your current scripts. If the project has a maintained `requirements.txt`, use it to install the project's pinned dependencies.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/hemant7102/ML-PIPELINE-DEMO.git
cd ML-PIPELINE-DEMO
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can either adjust your execution policy according to your organization's guidance or invoke the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

### 3. Install dependencies

If a `requirements.txt` file exists:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Otherwise, install the packages required by the scripts, including DVC and the project's data-science libraries. For example:

```powershell
python -m pip install dvc pandas scikit-learn nltk
```

Additional packages may be required depending on the model implementation. Use the same compatible Python and package versions used when the pipeline was last tested.

### 4. Prepare data and DVC artifacts

The project uses DVC to track pipeline outputs. If the repository is configured with an accessible DVC remote, retrieve tracked artifacts with:

```powershell
dvc pull
```

If the remote is not configured or is inaccessible, configure a remote that you have permission to access, or run the pipeline from the required source data if that data is available.

**Important:** A DVC remote configured to a local path on another computer is not portable. For sharing artifacts across machines, configure a shared remote such as supported cloud/object storage. Do not commit credentials or access tokens.

## Run the Pipeline

From the project root, with the virtual environment activated:

```powershell
dvc repro
```

To force all stages to run again:

```powershell
dvc repro --force
```

View the pipeline dependency graph:

```powershell
dvc dag
```

Check pipeline status:

```powershell
dvc status
```

Display tracked evaluation metrics:

```powershell
dvc metrics show
```

DVC may skip stages when their dependencies and outputs are already up to date. This is expected behavior.

## Evaluation Metrics

The evaluation stage writes metrics to `metrics.json`. The current reported metrics are:

| Metric | Score |
|---|---:|
| Accuracy | 0.68562 |
| ROC-AUC | 0.65295 |
| Macro Precision | 0.71096 |
| Macro Recall | 0.58792 |

These values are a snapshot, not a guarantee that every run will produce identical results. Performance depends on the input data, preprocessing, feature generation, model configuration, and evaluation procedure.

For a fuller evaluation, review a confusion matrix, per-class precision/recall/F1 scores, class balance, and the choice of positive class used for ROC-AUC. Do not judge model quality from accuracy alone.

## Git and DVC: What Is Stored Where?

- **Git/GitHub:** source code, pipeline definitions, configuration, and DVC metadata.
- **DVC:** versioned data and model/pipeline artifacts, backed by a configured DVC remote.
- **Local working directory:** files generated when pipeline stages execute.

A successful `git push` does not upload DVC data artifacts to a DVC remote. Likewise, `dvc push` uploads artifacts to the configured DVC remote, not to GitHub.

Before sharing this repository, check that the remote configuration does not contain a machine-specific path that other contributors cannot access.

## Troubleshooting

### `dvc repro` skips stages

This usually means DVC considers the stage dependencies and outputs unchanged. Use `dvc status` to check the pipeline or `dvc repro --force` to rerun every stage.

### `dvc pull` cannot find artifacts

Check that the DVC remote is configured and accessible, and that the required artifacts were pushed to that remote:

```powershell
dvc remote list
dvc status
dvc pull
```

### Missing Python packages or NLP resources

Activate the correct virtual environment, install project dependencies, and make sure the required NLTK resources are available for the preprocessing code.

### Git shows generated data as untracked

The `data/.gitignore` file is intended to keep generated/raw data directories out of ordinary Git tracking because DVC manages those artifacts. Check `git status --short --untracked-files=all` before staging files; do not blindly force-add datasets or model artifacts.

## Future Improvements

- Add MLflow for experiment tracking and model comparison.
- Add automated tests and data validation.
- Improve model performance through error analysis and systematic experiments.
- Add a CI workflow to validate pipeline code on changes.
- Configure a shared cloud-backed DVC remote.
- Package and serve the model through an API, then containerize it if deployment is required.

## Repository

GitHub: https://github.com/hemant7102/ML-PIPELINE-DEMO

## Disclaimer

This is a learning/demo project. The reported metrics should be independently validated before any real-world use.
