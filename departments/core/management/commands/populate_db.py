import random
from faker import Faker
from django.core.management.base import BaseCommand
from core.models import Department, Position, Employee, Project, ProjectExecution

faker = Faker("uk_UA")  # Українська локаль для генерації даних


class Command(BaseCommand):
    help = "Заповнює базу даних фейковими даними"

    def handle(self, *args, **kwargs):
        self.stdout.write("Заповнення бази даних...")

        # 1. Створення відділів
        departments = []
        for _ in range(3):  # Наприклад, 3 відділи
            dep = Department.objects.create(
                name=faker.job(),
                phone=faker.phone_number(),
                room_number=random.randint(701, 710),
            )
            departments.append(dep)
        self.stdout.write(f"Створено {len(departments)} відділи.")

        # 2. Створення посад
        positions = []
        for _ in range(5):  # Наприклад, 5 посад
            pos = Position.objects.create(
                name=faker.word(),
                salary=random.randint(1500, 5000),
                bonus_percent=random.randint(5, 20),
            )
            positions.append(pos)
        self.stdout.write(f"Створено {len(positions)} посад.")

        # 3. Створення працівників
        employees = []
        for _ in range(17):  # Наприклад, 17 працівників
            emp = Employee.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                middle_name=faker.first_name(),
                address=faker.address(),
                phone=faker.phone_number(),
                education=random.choice(["спеціальна", "середня", "вища"]),
                department=random.choice(departments),
                position=random.choice(positions),
            )
            employees.append(emp)
        self.stdout.write(f"Створено {len(employees)} працівників.")

        # 4. Створення проектів
        projects = []
        for _ in range(8):  # Наприклад, 8 проектів
            proj = Project.objects.create(
                name=faker.bs(),
                deadline=faker.date_between(start_date="today", end_date="+2y"),
                budget=random.randint(100000, 500000),
            )
            projects.append(proj)
        self.stdout.write(f"Створено {len(projects)} проектів.")

        # 5. Створення виконання проектів
        executions = []
        for _ in range(12):  # Наприклад, 12 записів про виконання
            exec = ProjectExecution.objects.create(
                project=random.choice(projects),
                department=random.choice(departments),
                start_date=faker.date_between(start_date="-2y", end_date="today"),
            )
            executions.append(exec)
        self.stdout.write(f"Створено {len(executions)} записів про виконання проектів.")

        self.stdout.write("Заповнення завершено!")
