# Flask Docker App

A Python Flask web application containerized with Docker, tested with pytest, and deployed via a CI/CD pipeline using GitHub Actions.

## Tech Stack

- Python / Flask
- Docker + Docker Compose
- pytest
- GitHub Actions (CI/CD)

## Project Structure

```text
flask-docker-app/
│
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD pipeline
│
├── app.py                      # Main Flask application
├── test_app.py                 # pytest test cases
├── Dockerfile                  # Docker image configuration
├── docker-compose.yml          # Multi-container orchestration
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```


## How to Run Locally

**Without Docker:**
```bash
pip install -r requirements.txt
python app.py
```

**With Docker:**
```bash
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app
```

**With Docker Compose:**
```bash
docker-compose up -d
```

Access the app at `http://localhost:5000`

## How to Run Tests

```bash
pip install pytest flask
pytest test_app.py -v
```

## CI/CD Pipeline

Every push to the `main` branch automatically triggers the GitHub Actions pipeline which:

1. Sets up Python environment
2. Installs dependencies
3. Runs pytest test suite
4. Builds Docker image

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Returns welcome message |
