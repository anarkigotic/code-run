docker build --platform linux/amd64 -t image_juan .

docker tag image_juan gcr.io/test-docker-416523/image_juan

docker push gcr.io/test-docker-416523/image_juan

gcloud run deploy --image gcr.io/test-docker-416523/image_juan --platform managed --region us-central1

 