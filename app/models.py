from app.ext.database import db


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))

    def __str__(self) -> str:
        return self.name
    
    def serializer(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name
        }