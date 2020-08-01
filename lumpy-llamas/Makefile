test:
	python manage.py test
lint:
	flake8 .

frontend:
	yarn build

migrate:
	python manage.py migrate

serve:
	python manage.py runserver

deploy:
	docker build . -t eu.gcr.io/optimum-surface-285007/llammabbs
	docker push eu.gcr.io/optimum-surface-285007/llammabbs
	gcloud --project optimum-surface-285007 run deploy llamma --image eu.gcr.io/optimum-surface-285007/llammabbs --platform managed --region europe-west1 --quiet
