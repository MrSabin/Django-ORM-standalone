import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    visits = Visit.objects.all()
    print(visits)
