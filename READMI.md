docker build --platform linux/amd64 -t image_juan .

docker tag image_juan gcr.io/test-docker-416523/image_juan

docker push gcr.io/test-docker-416523/image_juan

gcloud run deploy --image gcr.io/test-docker-416523/image_juan --platform managed --region us-central1

 
 # asociar mi repositorio a code build 
 gcloud builds triggers create github \
--repo-name=code-run \
--repo-owner=anarkigotic \
--branch-pattern=".*" \
--build-config=cloudbuild.yaml


gcloud projects add-iam-policy-binding test-docker-416523 \
    --member=serviceAccount:782634242133@cloudbuild.gserviceaccount.com \
    --role=roles/run.admin

gcloud iam service-accounts add-iam-policy-binding 782634242133-compute@developer.gserviceaccount.com \
    --member=serviceAccount:782634242133@cloudbuild.gserviceaccount.com \
    --role=roles/iam.serviceAccountUser