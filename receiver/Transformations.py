from typing import Dict


def transform_rating(extracted_rating_data) -> Dict:
    extracted_rating_data["score"] = extracted_rating_data["score"] / 2
    return extracted_rating_data
