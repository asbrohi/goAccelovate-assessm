from pydantic import BaseModel
from typing import Optional

class JobSearchCriteria(BaseModel):
    position: str
    location: str
    experience: Optional[str] = None
    salary: Optional[str] = None
    jobNature: Optional[str] = None
    skills: Optional[str] = None