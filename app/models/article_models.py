from pydantic import BaseModel
from typing import List


class Section(BaseModel):
    heading: str
    subheadings: List[str] = []


class Outline(BaseModel):
    title: str
    sections: List[Section]


class InternalLink(BaseModel):
    anchor: str
    target_page: str


class ExternalReference(BaseModel):
    source: str
    url: str
    placement_context: str


class SEOData(BaseModel):
    title_tag: str
    meta_description: str
    primary_keyword: str
    secondary_keywords: List[str]