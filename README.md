# Run locally using Flask
pip install -U flask
setx FLASK_APP web
python -m flask run

# Run locally using WSGI
python web/wsgi.py

# Run in Docker

## Manually
docker image rm flask-sample
docker build -t flask-sample:latest . --build-arg PORT=5000
docker run -d -p 5000:5000 flask-sample

## Usinng Docker Compose
docker-compose up

# Run in GCP
Install SDK: https://cloud.google.com/sdk/docs/install

## Deploy manually
gcloud config set run/region us-central1
gcloud builds submit --tag gcr.io/team-trev/flask-sample
gcloud run deploy flask-sample --platform managed --image gcr.io/team-trev/flask-sample

## Deploy using YAML file
gcloud builds submit --config cloudbuild.yml .

### Secutity permissions for Cloud Build using a YAML file
gcloud projects list

Grant the Cloud Run Admin role to the Cloud Build service account:
gcloud projects add-iam-policy-binding team-trev --member "serviceAccount:319727886036@cloudbuild.gserviceaccount.com" --role roles/run.admin

Grant the IAM Service Account User role to the Cloud Build service account on the Cloud Run runtime service account:
gcloud iam service-accounts add-iam-policy-binding 319727886036-compute@developer.gserviceaccount.com --member="serviceAccount:319727886036@cloudbuild.gserviceaccount.com" --role="roles/iam.serviceAccountUser"

## List delpoyed endpoints
gcloud run services list --platform managed
