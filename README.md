# GCP Data Pipeline Project

## 📌 Overview

This project demonstrates an end-to-end data pipeline built using Python and Google Cloud Platform (GCP). The pipeline processes raw customer data, performs advanced transformations, and loads curated data into BigQuery for analytical querying.

---

## 🏗️ Architecture

Raw Data → Google Cloud Storage (GCS) → Python Processing → GCS (Processed) → BigQuery → SQL Analysis

---

## 🛠️ Tools & Technologies

* Python (Pandas)
* Google Cloud Storage (GCS)
* BigQuery
* SQL

---

## ⚙️ Key Features

* Data cleaning and transformation using Python
* Schema standardization (column formatting, data consistency)
* Feature engineering:

  * Full name generation
  * Email domain extraction
  * Subscription year and quarter
  * Customer tenure calculation
  * Customer segmentation
* Multi-layer data design approach (raw → curated → business-ready)
* SQL-based analysis for business insights

---

## 🔄 Project Workflow

1. Raw customer dataset uploaded to GCS
2. Data cleaned and transformed using Python (Colab)
3. Processed dataset stored in GCS
4. Curated data loaded into BigQuery
5. SQL queries used to generate insights

---

## 📊 Sample Analysis

* Customer segmentation based on tenure
* Region-wise customer distribution
* Email domain analysis

---

## 📸 Outputs

Screenshots of:

* GCS buckets
* Data cleaning (before and after)
* BigQuery tables
* SQL query results

(Refer to the `screenshots/` folder)

---

## 💡 Summary

This project simulates a real-world data engineering pipeline, demonstrating data ingestion, transformation, and analytical processing using cloud-based tools.

---

## 🚀 Future Improvements

* Automate pipeline using Cloud Functions / Workflows
* Add scheduling for periodic data ingestion
* Integrate with dashboards (e.g., reporting tools)

---
