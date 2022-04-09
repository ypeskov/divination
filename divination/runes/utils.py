import json


def prepare_for_json(answers):
    items = []
    for answer in answers:
        json_str = items.append({
            'rune_order': answer['rune'].order,
            'rune_title': answer['rune'].title,
            'rune_position': answer['is_inverted_str'],
        })

    return items
