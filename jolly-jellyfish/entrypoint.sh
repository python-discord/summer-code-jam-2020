#!/bin/bash
set -e

if [ "$1" = 'runserver' ]; then
    python manage.py migrate
    cat | python manage.py shell <<_EOF_
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@myproject.com', '$ADMIN_PASSWORD')
_EOF_
    python manage.py loaddata initial-themes.yaml
fi

exec python manage.py "$@"