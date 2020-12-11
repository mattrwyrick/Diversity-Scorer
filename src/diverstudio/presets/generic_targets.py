import json

from diverstudio.tools import ProbValue


def load_target_from_composition_all_fields(path):
    """
    Return the target items for a scoring object that aims for a uniform demographic
    :parma path:
    :return:
    """
    with open(path, "r") as f:
        data = json.load(f)

    target_keys = [key for key in data[0] if key != "amount"]

    target_demo = []
    for demo in data:

        amount = demo["amount"]
        value = {key: demo[key] for key in target_keys}
        pv = ProbValue(amount, value)
        target_demo.append(pv)

    return target_demo, target_keys
