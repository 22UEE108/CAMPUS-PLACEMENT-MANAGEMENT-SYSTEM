from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .models import Student, Company, Application
from .schemas import (
StudentCreate,
LoginRequest,
CompanyCreate,
ApplicationCreate
)
from .auth import (
hash_password,
verify_password,
create_access_token
)

router = APIRouter()

@router.post("/register")
def register_student(
student: StudentCreate,
db: Session = Depends(get_db)
):
existing_user = (
db.query(Student)
.filter(Student.email == student.email)
.first()
)

```
if existing_user:
    raise HTTPException(
        status_code=400,
        detail="Email already registered"
    )

new_student = Student(
    name=student.name,
    email=student.email,
    password=hash_password(student.password)
)

db.add(new_student)
db.commit()
db.refresh(new_student)

return {
    "message": "Student registered successfully"
}
```

@router.post("/login")
def login(
login_data: LoginRequest,
db: Session = Depends(get_db)
):
student = (
db.query(Student)
.filter(Student.email == login_data.email)
.first()
)

```
if not student:
    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )

if not verify_password(
    login_data.password,
    student.password
):
    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )

token = create_access_token(
    {
        "sub": student.email,
        "student_id": student.id
    }
)

return {
    "access_token": token,
    "token_type": "bearer"
}
```

@router.post("/companies")
def create_company(
company: CompanyCreate,
db: Session = Depends(get_db)
):
new_company = Company(
company_name=company.company_name,
role=company.role,
deadline=company.deadline,
oa_date=company.oa_date
)

```
db.add(new_company)
db.commit()
db.refresh(new_company)

return {
    "message": "Company created successfully"
}
```

@router.get("/companies")
def get_companies(
db: Session = Depends(get_db)
):
companies = db.query(Company).all()

```
return companies
```

@router.post("/apply")
def apply_to_company(
application: ApplicationCreate,
db: Session = Depends(get_db)
):
student = (
db.query(Student)
.filter(
Student.id == application.student_id
)
.first()
)

```
if not student:
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

company = (
    db.query(Company)
    .filter(
        Company.id == application.company_id
    )
    .first()
)

if not company:
    raise HTTPException(
        status_code=404,
        detail="Company not found"
    )

existing_application = (
    db.query(Application)
    .filter(
        Application.student_id
        == application.student_id,
        Application.company_id
        == application.company_id
    )
    .first()
)

if existing_application:
    raise HTTPException(
        status_code=400,
        detail="Already applied"
    )

new_application = Application(
    student_id=application.student_id,
    company_id=application.company_id
)

db.add(new_application)
db.commit()
db.refresh(new_application)

return {
    "message": "Application submitted"
}
```

@router.get("/applications")
def get_applications(
db: Session = Depends(get_db)
):
applications = (
db.query(Application)
.all()
)

```
return applications
```
