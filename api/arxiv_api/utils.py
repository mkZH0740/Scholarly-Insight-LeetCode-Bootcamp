import xml.etree.ElementTree as ET
import datetime
from xml.etree.ElementTree import Element

from .models import ArxivArticleAuthor, ArxivArticleEntry

from typing import List, Dict, Tuple, Literal


arxiv_feed_namespace = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}


def is_valid_query(query: Dict[str, str]):
    return "key" in query and "value" in query


def stringify_query(query: Dict[str, str]):
    return f"{query['key']}:{query['value']}"


def build_search_query(queries: List[Dict[str, str]]):
    return " AND ".join(
        [stringify_query(query) for query in queries if is_valid_query(query)]
    )


def parse_author(author_element: Element):
    author_name = (
        author_element.find("atom:name", arxiv_feed_namespace).text or "unknown author"
    )
    author = ArxivArticleAuthor(name=author_name)

    affiliation_element = author_element.find("arxiv:affiliation")
    if affiliation_element is not None:
        author_affiliation = affiliation_element.text or "unknown affiliation"
        author.affiliation = author_affiliation

    return author


def parse_entry(entry_element: Element):
    id: str = entry_element.find("atom:id", arxiv_feed_namespace).text or "unknown id"
    title: str = (
        entry_element.find("atom:title", arxiv_feed_namespace).text or "unknown title"
    )
    published = datetime.datetime.fromisoformat(
        entry_element.find("atom:published", arxiv_feed_namespace).text
    )
    updated = datetime.datetime.fromisoformat(
        entry_element.find("atom:updated", arxiv_feed_namespace).text
    )
    summary: str = (
        entry_element.find("atom:summary", arxiv_feed_namespace).text
        or "unknown summary"
    )
    authors = [
        parse_author(author_element)
        for author_element in entry_element.findall("atom:author", arxiv_feed_namespace)
    ]
    categories = [
        category_element.get("term", "unknown category")
        for category_element in entry_element.findall(
            "atom:category", arxiv_feed_namespace
        )
    ]
    abstract_link = entry_element.find(
        "atom:link[@rel='alternate']", arxiv_feed_namespace
    ).get("href", "unknown abstract page url")
    pdf_link = entry_element.find(
        "atom:link[@rel='related'][@title='pdf']", arxiv_feed_namespace
    ).get("href", "unknown pdf page url")

    entry = ArxivArticleEntry(
        id=id,
        title=title,
        published=published,
        updated=updated,
        summary=summary,
        authors=authors,
        categories=categories,
        abstract_link=abstract_link,
        pdf_link=pdf_link,
    )

    # optional
    primary_category_element = entry_element.find(
        "arxiv:primary_category", arxiv_feed_namespace
    )
    if primary_category_element is not None:
        entry.primary_category = primary_category_element.get(
            "term", "unknown primary category term"
        )

    doi_link_element = entry_element.find(
        "atom:link[@rel='related'][@title='doi']", arxiv_feed_namespace
    )
    if doi_link_element is not None:
        entry.doi_link = doi_link_element.get("href", "unknown doi link url")

    comment_element = entry_element.find("arxiv:comment", arxiv_feed_namespace)
    if comment_element is not None:
        entry.comment = comment_element.text or "unknown comment"

    journal_reference_element = entry_element.find(
        "arxiv:journal_ref", arxiv_feed_namespace
    )
    if journal_reference_element is not None:
        entry.journal_reference = (
            journal_reference_element.text or "unknown journal reference"
        )

    doi_element = entry_element.find("arxiv:doi", arxiv_feed_namespace)
    if doi_element is not None:
        entry.doi = doi_element.text or "unknown doi"

    return entry


def parse_arxiv_feed(
    feed: str,
) -> Tuple[Literal[False], str] | Tuple[Literal[True], List[ArxivArticleEntry]]:
    root = ET.fromstring(feed)
    entries = root.findall("atom:entry", arxiv_feed_namespace)

    if len(entries) == 0:
        # is error feed, unknown reason
        return False, "unknown error occured"

    first_entry = entries[0]
    if len(first_entry.findall("atom:published", arxiv_feed_namespace)) == 0:
        # is error feed, extract error message
        return (
            False,
            first_entry.find("atom:summary", arxiv_feed_namespace).text
            or "unspecified error",
        )

    entries = [parse_entry(entry_element) for entry_element in entries]
    return True, entries
