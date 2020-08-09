test:
	python manage.py test
lint:
	flake8 .

frontend:
	yarn build

migrate:
	python manage.py migrate

serve:
	yarn build && python manage.py runserver

deploy:
	gcloud builds submit . --config cloudbuild.yml --project optimum-surface-285007 
	gcloud --project optimum-surface-285007 run deploy llamma --image eu.gcr.io/optimum-surface-285007/llammabbs --platform managed --region europe-west1 --quiet
