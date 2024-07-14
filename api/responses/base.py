from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel):
    pass


class BaseResponse(Base):
    created_at: datetime
    updated_at: datetime
