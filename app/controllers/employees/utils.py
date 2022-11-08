import csv
import io

from app.models import Company


def extract_employees(file):
    match file.filename.split('.')[-1]:
        case 'txt' | 'csv':
            return from_text(file)
        case 'xlsx':
            return from_xlsx(file)


def from_text(file):
    data = file.stream.read()
    stream = io.StringIO(data.decode("UTF8"), newline=None)
    reader = csv.reader(stream)
    next(reader)
    keys = ['id', 'name', 'war_name', 'role', 'identification', 'admission']

    employees = []
    for row in stream:
        values = row.split(';')
        company = values[-1][:-1] if '\n' in values[-1] else values[-1]
        values = values[:-1]

        employee_data = {key: value for key, value in zip(keys, values)}
        employee_data['company_id'] = Company.query.filter_by(name=company).first().id
        
        employees.append(employee_data)
    return employees


def from_xlsx(file):
    ...