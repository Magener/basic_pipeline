from typing import List, Dict, Any


def parse_to_dict(rows, description) -> List[Dict[str, Any]]:
    columns = [desc[0] for desc in description]

    return [dict(zip(columns, row)) for row in rows]