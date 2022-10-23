from app.ext.database import db


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(140), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'<Employee(id={self.id}, name={self.name})>'


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(140), nullable=False)
    employ = db.orm.relationship("Employee", backref="company", uselist=True)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'Company(id={self.id}, name={self.name})'
