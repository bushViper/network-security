# Network Security: Phishing Website Classification

A Python machine-learning project for preparing phishing website data and training a classifier. The repository contains a staged pipeline for data ingestion, schema and drift validation, feature transformation, and model training. The target column is `Result`; the expected feature schema is documented in [`data_schema/schema.yaml`](data_schema/schema.yaml).


## Repository contents

- `Network_Data/phisingData.csv` — included phishing dataset (the filename uses this spelling).
- `push_data.py` — converts the CSV to records and inserts them into MongoDB.
- `main.py` — runs ingestion, validation, transformation, and model training.
- `networksecurity/components/` — implementations of the pipeline stages.
- `data_schema/schema.yaml` — expected data columns and types.
- `requirements.txt` and `setup.py` — Python dependencies and package metadata.

## Requirements

- Python 3.10 or newer
- A MongoDB deployment reachable from this machine

The pipeline reads MongoDB credentials from `MONGO_DB_URL`. Keep credentials out of source control.

## Setup

From the repository root, create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the project and its dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

Set `MONGO_DB_URL` to your MongoDB connection string in the current shell, or place it in a local `.env` file in the repository root:

```text
MONGO_DB_URL=mongodb+srv://<username>:<password>@<cluster>/<options>
```

## Load the dataset and run the pipeline

The data loader expects `Network_Data/phisingData.csv` and writes its records to database `network_data`, collection `NetworkData`:

```bash
python push_data.py
```

After the data is available in MongoDB, start the training pipeline:

```bash
python main.py
```

The pipeline reads from that database and collection, splits the data into training and test sets, validates the data, transforms features, and trains candidate classifiers. Generated artifacts are written under `Artifacts/`; model files are written under `final_model/`.

## Notes

- `test_mongodb.py` checks connectivity using the configured MongoDB URI; it is a standalone script, not a complete automated test suite.
- Model training logs metrics and models with MLflow. Check the MLflow version and scikit-learn compatibility if model logging fails.
- This repository does not include a standalone inference API or deployment service.
