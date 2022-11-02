# Customer Churn Project

Customer churn refers to the process of identifying customer/ clients who will terminate their relations with an organization. It is very important aspect of an organization as it helps to measure the growth of the company. Hence, The purpose of this project is to build a predictive model to determine if a given customer will churn or not based on the customers historical data available, using various machine learning algorithms and techniques <br><br>

## Data Description

- The data for this project will be obtained from a public data bank source - Kaggle.com and can be found [here](https://www.kaggle.com/blastchar/telco-customer-churn)
- Data will contain about 50,000 observations and some 30 features to explore.
- One individual row in the data signifies one unique observation of a customer's behavior (features)
- Tha data will be stored in a SQL database for faster and easy accessibility

## Test the Api:

The finished api can be found on docker hub via this [link](docker.io/phade160/customer-churn) or can be directly pulled with the following commands:<br>

<h3>Pull:</h3>

    docker push phade160/customer-churn:latest

<h3>run the image in a container:</h3>

    docker run [--detach] -p 80:80 phade160/customer-churn

<h3>Web browser</h3>

    http://0.0.0.0/docs



## Project Structure

    ├── README.md               <- The top-level README for developers using this project.
    ├── data
    │   ├── external            <- Data from third party sources.
    │   ├── interim             <- Intermediate data that has been transformed.
    │   ├── processed           <- The final, canonical data sets for modeling.
    │   └── raw                 <- The original, immutable data dump.
    │
    ├── logs                    <- Log API requests (e.g. input, response, stdout, stderr information)
    │
    ├── docs                    <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models                  <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                              the creator's initials, and a short `-` delimited description, e.g.
    │                              `1.0-sa-initial-data-exploration`.
    │
    ├── references              <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures             <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
    │                              generated with `pip freeze > requirements.txt`
    │
    │
    ├── tests                   <- Test scripts for unit testing (e.g. using pytest),
    │                              performance and load testing of the API
    │
    ├── app                     <- Contains all files and logic related to api building. eg. a main.py and BaseModel class extension
    │   └── main.py             <- Fastapi Api file
    │
    └── .gitignore

### Installing development requirements

---

    pip install -r requirements.txt

### Build documentation using Sphinx

---

    cd docs/
    make html

---

<p><small>Project created using the <a target="_blank" href="https://github.com/sujitahirrao/flask-ai-api-template">Flask AI API Template</a>.</small></p>
