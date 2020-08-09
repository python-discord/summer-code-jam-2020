import importlib
import time

from django.core.management.base import BaseCommand
from django_q.models import Schedule


class Command(BaseCommand):
    help = "Run all scheduled tasks"

    def handle(self, *args, **options):
        tasks = Schedule.objects.all()
        while True:
            for i, task in enumerate(tasks, start=1):
                task: Schedule

                module, func_name = task.func.rsplit(".", 1)
                module_obj = importlib.import_module(module)
                func = getattr(module_obj, func_name)
                print(f"Now running {task.func} {i}/{len(tasks)}")
                start = time.time()
                func()
                end = time.time()
                print(f"Finished the task in {end-start:.2f} seconds")
