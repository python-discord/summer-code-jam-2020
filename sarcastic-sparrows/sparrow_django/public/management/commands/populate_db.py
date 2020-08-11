from django.core.management.base import BaseCommand
from pathlib import Path
from ...models import Stock


class Command(BaseCommand):
    help = "Pre-loads DB data from a local directory"

    def add_arguments(self, parser):
        parser.add_argument("path", type=str, help="The path to the data to load")

    def handle(self, *args, **kwargs):
        path_arg = kwargs["path"]
        path = Path(path_arg).resolve()
        Stock.objects.all().delete()
        for x in path.iterdir():
            self.stdout.write(x.name)
            with open(x, "r") as f:
                lines = f.readlines()
                model_objs = []
                for line in lines:
                    stock_record = line.split(sep=",")
                    if stock_record[0] != "Date":
                        model_objs.append(
                            Stock(
                                date=stock_record[0],
                                ticker_symbol=x.name.split(sep=".")[0],
                                open=stock_record[1],
                                high=stock_record[2],
                                low=stock_record[3],
                                close=stock_record[4],
                                volume=stock_record[5],
                            )
                        )
                Stock.objects.bulk_create(model_objs)
