from typing import List, Dict


def is_valid_query(query: Dict[str, str]):
    return "key" in query and "value" in query


def stringify_query(query: Dict[str, str]):
    return f"{query['key']}:{query['value']}"


def build_search_query(queries: List[Dict[str, str]]):
    return " AND ".join(
        [stringify_query(query) for query in queries if is_valid_query(query)]
    )
