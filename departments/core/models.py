from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва відділу")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    room_number = models.PositiveIntegerField(verbose_name="Номер кімнати")

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва посади")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Оклад")
    bonus_percent = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Відсоток премії"
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    middle_name = models.CharField(max_length=50, verbose_name="По батькові")
    address = models.TextField(verbose_name="Адреса")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    education = models.CharField(
        max_length=20,
        choices=[
            ("Special", "Спеціальна"),
            ("Secondary", "Середня"),
            ("Higher", "Вища"),
        ],
        verbose_name="Освіта",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="Відділ",
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="Посада",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва проекту")
    deadline = models.DateField(verbose_name="Термін виконання")
    budget = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Бюджет")

    def __str__(self):
        return self.name


class ProjectExecution(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="executions",
        verbose_name="Проект",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="executions",
        verbose_name="Відділ",
    )
    start_date = models.DateField(verbose_name="Дата початку")

    def __str__(self):
        return f"{self.project.name} ({self.department.name})"
