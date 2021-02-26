Heart Disease Prediction
==============================

BITS Pilani Capstone Project - Group 2

<p>
  <a href="https://www.linkedin.com/in/nithin-rajan/" target="_blank">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> Nithin
  </a> &nbsp;
  <a href="https://www.linkedin.com/in/dhanya-purushothaman-b088267/">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> Dhanya
  </a> &nbsp;
  <a href="https://www.linkedin.com/in/neema-srivastava-3927619a/">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> Neema
  </a> &nbsp; 
  <a href="https://www.linkedin.com/in/lalitha-l-4521185/">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> Lalitha
  </a> &nbsp; 
  <a href="https://www.linkedin.com/in/moorthy-setty-aab25313/">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> Moorthy
  </a> &nbsp; 
</p>

Local Execution
------------
Change the dataset path in tox.ini  
Model Training  
  python3 main.py trainModel  
Model Prediction  
  streamlit run main.py predictModel  


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── Dockerfile         <- Model Containerization
    |
    ├── k8s                <- Kubernetes supporting files
    |
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


---------