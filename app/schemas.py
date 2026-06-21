from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
name: str
email: EmailStr
password: str

class StudentResponse(BaseModel):
id: int
name: str
email: EmailStr

```
class Config:
    from_attributes = True
```

class LoginRequest(BaseModel):
email: EmailStr
password: str

class CompanyCreate(BaseModel):
company_name: str
role: str
deadline: str
oa_date: str | None = None

class CompanyResponse(BaseModel):
id: int
company_name: str
role: str
deadline: str
oa_date: str | None = None

```
class Config:
    from_attributes = True
```

class ApplicationCreate(BaseModel):
student_id: int
company_id: int

class ApplicationResponse(BaseModel):
id: int
student_id: int
company_id: int
status: str

```
class Config:
    from_attributes = True
```
