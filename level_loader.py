import sys
import os
import json


def load_map():
    global current_map, current_map_bounds
    with open("Assets/levels/main/$map.json", "r") as reader:
        current_map_bounds = {
            "top": 0,
            "bottom": 0,
            "left": 0,
            "right": 0
        }
        data = json.load(reader)
        id_dict = {}
        for level in data["map"]:
            if "links" in level.keys():
                for link in level["links"]:
                    orig = link["origin"]
                    if orig in id_dict.keys():
                        link["origin"] = id_dict[orig]
                    else:
                        raise Exception(f"Incorrect link order from {orig} to {level['id']}")
            id_dict[level["id"]] = level
            with open(f"Assets/levels/main/{level['id']}.h.json", "r") as level_head:
                level_head_data = json.load(level_head)
                level["head"] = level_head_data
            current_map_bounds["left"] = min(current_map_bounds["left"], level["position"][0])
            current_map_bounds["right"] = max(current_map_bounds["right"], level["position"][0])
            current_map_bounds["top"] = min(current_map_bounds["top"], level["position"][1])
            current_map_bounds["bottom"] = max(current_map_bounds["bottom"], level["position"][1])
        current_map = data
        return data
    return None


current_map = load_map()


current_map_bounds = {
    "top": 0,
    "bottom": 0,
    "left": 0,
    "right": 0
}


def get_map():
    return current_map


def get_map_bounds():
    return current_map_bounds


def get_level_by_id(level_id):
    global current_map
    return next(filter(lambda l: l["id"] == level_id, current_map["map"]), None)


def get_rank(level_id, get_locked=True):  # -1 locked, 0 default (uncompleted), 1 E, 2 D, 3 C, 4 B, 5 A, 6 S, 7 SS
    global current_map
    level = get_level_by_id(level_id)
    level_prog = next(filter(lambda l: l["id"] == level_id, current_map["progress"]), None)
    if level_prog:
        rank = 0
        while rank < 7 and level["head"]["ranks"][rank] >= level_prog["best_time"]:
            rank += 1
        return rank  # TODO replace with filter (or that enumerate gimmick)
    if get_locked:
        for req in level["reqs"]:
            for req_level in req["levels"]:
                if get_rank(req_level, False) < req["rank"]:
                    return -1
        return 0
    else:
        return 0
