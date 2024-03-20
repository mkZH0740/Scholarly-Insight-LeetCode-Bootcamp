import json
from datetime import datetime as DateTime
from dataclasses import dataclass
from dataclasses import asdict
from typing import List, Optional


@dataclass
class ArxivArticleAuthor:
    # name of the author
    name: str
    # affiliation of the author (optional)
    affiliation: Optional[str] = None

    def to_dict(self):
        return asdict(self)


@dataclass
class ArxivArticleEntry:
    # url to the abstract page of the article
    id: str
    # title of the article
    title: str
    # date when first version of the article is published
    published: DateTime
    # date when this version of article is submitted
    updated: DateTime
    # summary of the article
    summary: str
    # authors of the article
    authors: List[ArxivArticleAuthor]
    # categories of the article
    categories: List[str]
    # abstract page link
    abstract_link: str
    # pdf page link
    pdf_link: str
    # primary category (optional)
    primary_category: Optional[str] = None
    # doi page link (optional)
    doi_link: Optional[str] = None
    # author comment (optional)
    comment: Optional[str] = None
    # journal reference of the article (optional)
    journal_reference: Optional[str] = None
    # doi (optional)
    doi: Optional[str] = None

    def to_dict(self):
        entry_dict = asdict(self)
        entry_dict["published"] = self.published.strftime("%Y-%m-%dT%H:%M:%SZ")
        entry_dict["updated"] = self.updated.strftime("%Y-%m-%dT%H:%M:%SZ")
        return entry_dict
