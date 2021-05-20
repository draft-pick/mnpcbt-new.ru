from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from employees.models import Employees


@admin.register(Employees)
class EmployeesAdmin(ImportExportModelAdmin):
    list_display = (
        "surname", "name", "patronymic", "post", "units", "branch", "formation", "speciality", "category", "degree",
        "rank", "mos_doc")
    pass
