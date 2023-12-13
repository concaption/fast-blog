from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import field_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @field_validator("slug")
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: date

    class Config:
        from_attributes = True


class UpdateBlog(CreateBlog):
    pass
