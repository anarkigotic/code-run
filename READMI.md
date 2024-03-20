docker build --platform linux/amd64 -t image_juan .

docker tag image_juan gcr.io/test-docker-416523/image_juan

docker push gcr.io/test-docker-416523/image_juan

gcloud run deploy --image gcr.io/test-docker-416523/image_juan --platform managed --region us-central1

 
 #  asociar mi repositorio a code buold
 gcloud builds triggers create github \
--repo-name=code-run \
--repo-owner=anarkigotic \
--branch-pattern=".*" \
--build-config=cloudbuild.yaml