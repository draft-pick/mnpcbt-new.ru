from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from employees.models import Employees


@admin.register(Employees)
class EmployeesAdmin(ImportExportModelAdmin):
    list_display = (
        "surname", "name", "patronymic", "post", "units", "formation", "accreditation", "speciality", "degree",
        "speciality_akk", "qualification", "mos_doc")
    pass
