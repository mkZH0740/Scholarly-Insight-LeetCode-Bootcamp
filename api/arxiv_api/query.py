from flask import request
from flask_restful import Resource

from typing import Any, List

from urllib.parse import urlencode
from urllib.request import urlopen

from .utils import build_search_query, parse_arxiv_feed


def make_err(message: str):
    return {"status": False, "error": message}


def make_ok(value: Any):
    return {"status": True, "value": value}


class ArxivQuery(Resource):
    _base_url = "http://export.arxiv.org/api/query?"
    _default_query = []
    _default_start = 0
    _default_max_results = 10

    def post(self):
        body: dict | None = request.get_json(silent=True)

        if body is None:
            return make_err("request body is not supported")

        queries: List = body.get("queries", self._default_query)
        search_query = build_search_query(queries)

        start: int = body.get("start", self._default_start)

        max_results: int = body.get("max_results", self._default_max_results)

        endpoint = self._base_url + urlencode(
            {
                "search_query": search_query,
                "start": start,
                "max_results": max_results,
            }
        )

        with urlopen(endpoint) as query_request:
            feed = query_request.read().decode(
                query_request.headers.get_content_charset()
            )

        status, result = parse_arxiv_feed(feed)

        if status:
            return make_ok(value=[entry.to_dict() for entry in result])
        else:
            return make_err(message=result)
