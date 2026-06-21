from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Student(Base):
**tablename** = "students"

```
id = Column(Integer, primary_key=True, index=True)
name = Column(String, nullable=False)
email = Column(String, unique=True, nullable=False)
password = Column(String, nullable=False)

applications = relationship(
    "Application",
    back_populates="student"
)
```

class Company(Base):
**tablename** = "companies"

```
id = Column(Integer, primary_key=True, index=True)
company_name = Column(String, nullable=False)
role = Column(String, nullable=False)
deadline = Column(String)
oa_date = Column(String)

applications = relationship(
    "Application",
    back_populates="company"
)
```

class Application(Base):
**tablename** = "applications"

```
id = Column(Integer, primary_key=True, index=True)

student_id = Column(
    Integer,
    ForeignKey("students.id")
)

company_id = Column(
    Integer,
    ForeignKey("companies.id")
)

status = Column(
    String,
    default="Applied"
)

student = relationship(
    "Student",
    back_populates="applications"
)

company = relationship(
    "Company",
    back_populates="applications"
)
```
