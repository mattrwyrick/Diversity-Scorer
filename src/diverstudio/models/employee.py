import json

from diverstudio.tools import ProbValue


def load_attribute_generator_from_composition(path):
    """
    Load a composition json file into memory and create the generator from it
    :param name: path
    :return:
    """
    with open(path, "r") as f:
        data = json.load(f)

    composition = []
    for item in data:
        amount = item["amount"]
        value = {key: item[key] for key in item if key != "amount"}  # all attributes besides "amount"
        pv = ProbValue(amount, value)
        composition.append(pv)
    generator = AttributeGenerator(composition)
    return generator


class Employee(object):

    def __init__(self, eid, attributes, manages):
        """
        Create an Employee object for a tree organizational structure
        :param eid: int
        :param attributes: dict of str: str
        :param manages: list of Employee
        """
        self.id = eid
        self.manages = manages
        self.size = sum([m.size for m in manages]) + 1 if len(manages) > 0 else 1
        self.attrs = attributes

        # Assigned during scoring
        self.distribution = None  # Demographic distribution (includes this employee + those managed underneath)
        self.score = None  # Diversity score (this could remain none for some employees depending on the scoring method)


class AttributeGenerator(object):

    def __init__(self, composition):
        """
        Create a generator for returns a set of attributes with the specified probability
        :param composition: list of ProbVal(int, dict of attributes)
        """
        self.attrs = ProbValue.get_probability_list(composition)
        self.total = len(self.attrs)

    def __next__(self):
        """
        Return a dict of attributes from the given probabilities
        :return:
        """
        return ProbValue.get_value_from_probability_list(self.attrs, self.total)



