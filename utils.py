import json


def get_candidates(path):
    with open(path, 'r', encoding='UTF-8') as candidates:
        return json.load(candidates)


def format_candidates(candidates_list):
    result = '<pre>'
    for candidate in candidates_list:
        result += (
            '<pre>'
            f'Имя кандидата - {candidate["name"]}\n'
            f'Позиция кандидата - {candidate["position"]}\n'
            f'Навыки через запятую - {candidate["skills"]}\n'
        )

    result += '</pre>'
    return result
