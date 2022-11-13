from app.models import Employee
from sqlalchemy import or_


def filter_by_name_or_id(search):
    query = Employee.query.filter(
        or_(
            Employee.name.ilike(f'%{search}%'),
            Employee.id.ilike(f'%{search}%')
        )
    )
    return query