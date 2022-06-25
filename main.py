import os

import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit, Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    visits = Visit.objects.all()
    visiter = Passcard.objects.get(owner_name=f'Ashley Bartlett')
    filtered = Visit.objects.filter(passcard=visiter)
    long_visits = []
    longest_visits = []

    for visit in filtered:
        entered = timezone.localtime(visit.entered_at)
        leaved = (
            timezone.localtime(visit.leaved_at)
            if visit.leaved_at else timezone.localtime()
        )
        passed = leaved - entered
        passed_mins = passed.seconds // 60

        if passed_mins > 1000:
            longest_visits.append(visit)
        elif passed_mins > 10:
            long_visits.append(visit)

    print(f'Визиты дольше 10 минут: {long_visits}')
    print(f'Визиты дольше 1000 минут: {longest_visits}')

    opened_visits = Visit.objects.filter(leaved_at=None)
    for visit in opened_visits:
        time_passed = (
            timezone.localtime() - timezone.localtime(visit.entered_at)
        )
        passed_hours = time_passed.days * 24 + time_passed.seconds // 3600
        passed_minutes = (time_passed.seconds % 3600) // 60
        passed_seconds = (time_passed.seconds % 60)
        print(visit.passcard)
        print("Зашел в хранилище, время по Москве:")
        print(timezone.localtime(visit.entered_at))
        print("Находится в хранилище:")
        print(f"{passed_hours}:{passed_minutes}:{passed_seconds}")
