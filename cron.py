from django_cron import CronJobBase, Schedule


class YourCronJob(CronJobBase):
    RUN_EVERY_MINS = 24 * 60  # выполнение каждый день

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.meteo.py'

    def do(self):
        # Ваш код для выполнения ежедневной задачи
        import os

        # Set the DJANGO_SETTINGS_MODULE environment variable
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

        # Now you can import Django modules
        import django
        django.setup()

        # Your Django-related code here
        from basic_app.models import DataHashorot
        from basic_app.models import data

        def get_statistica_values():
            # Retrieve all instances
            data = DataHashorot.objects.all()

            # Extract the 'statistica' field from each instance
            statistica_values = [entry.statistica for entry in data]

            return statistica_values

        temp = 0

        statistica_values = get_statistica_values()
        for x in statistica_values:
            a = x.split(' ', 1)[0]
            temp += float(a)

        summa = 550 / temp
        if summa > 100:
            summa == 100

        eggs = 50 / temp
        if eggs > 100:
            eggs == 100

        lichinka = 200 / temp
        if lichinka > 100:
            lichinka == 100

        zrelix = 300 / temp
        if zrelix > 100:
            zrelix == 100
        data_entry = {
            'summa': f'{summa} %',
            'eggs': f'{eggs} %',
            'lichinka': f"{lichinka} %",
            'dlyazrelix': f"{zrelix} %",

        }
        data_instance = data.objects.create(**data_entry)
