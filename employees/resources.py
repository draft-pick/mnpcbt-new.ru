from import_export import resources
from employees.models import Employees


class EmployeesResource(resources.ModelResource):
    class Meta:
        model = Employees
