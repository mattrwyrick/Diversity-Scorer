import json
import random

from diverstudio.tools import ProbValue
from diverstudio.models.employee import Employee


class Seed(object):

    def __init__(self, attr_gen, pv_depths, pv_breadths, pv_seeds, random_stop):
        """
        Create a seed for growing an organization
        :param attr_gen: dict of str:str
        :param pv_depths: list of ProbVal(int, int)
        :param pv_breadths: list of ProbVal(int, int)
        :param pv_seeds: list of ProbVal(int, seed)
        :param random_stop: int [0, 100]
        """
        self.attr_generator = attr_gen
        self.stop = abs(random_stop % 101)

        self.depths = ProbValue.get_probability_list(pv_depths)
        self.depths_total = len(self.depths)

        self.breadths = ProbValue.get_probability_list(pv_breadths)
        self.breadths_total = len(self.breadths)

        self.seeds = ProbValue.get_probability_list(pv_seeds)
        self.seeds_total = len(self.seeds)

    def persist(self):
        """
        Determine if the seed should stop in the organization generation
        :return:
        """
        n = random.randint(1, 100)
        return n >= self.stop

    def get_attrs(self):
        """
        Return a probabilistic attribute from the generator
        :return:
        """
        return next(self.attr_generator)

    def get_new_seed(self):
        """
        Return a new seed from the given probabilities
        :return:
        """
        return ProbValue.get_value_from_probability_list(self.seeds, self.seeds_total)

    def get_depth(self):
        """
        Return a depth from the given probabilities
        :return:
        """
        return max(ProbValue.get_value_from_probability_list(self.depths, self.depths_total), 1)

    def get_breadth(self):
        """
        Return a breadth from the given probabilities
        :return:
        """
        return max(ProbValue.get_value_from_probability_list(self.breadths, self.depths_total), 0)


class OrganizationMaker(object):

    def __init__(self, seed):
        """
        Make an Organization
        :param seed:
        """
        self.total = 0
        max_depth = seed.get_depth()
        self.ceo = self.generate(seed, 0, max_depth)

    def generate(self, seed, curr_depth, max_depth):
        """
        Generate an organization by exercising the probabilistic seeds
        :param seed: Seed
        :param curr_depth: int
        :param max_depth: int
        :return: Employee
        """
        if seed is None:
            return []

        if curr_depth > max_depth:
            seed = seed.get_new_seed()
            if seed is None:
                return []
            max_depth = seed.get_depth()
            return self.generate(seed, 0, max_depth)

        if not seed.persist():
            seed = seed.get_new_seed()
            if seed is None:
                return []
            max_depth = seed.get_depth()
            return self.generate(seed, 0, max_depth)

        manages = []
        breadth = seed.get_breadth()
        for i in range(breadth):
            subordinate = self.generate(seed, curr_depth + 1, max_depth)
            if subordinate != []:
                manages.append(subordinate)

        self.total += 1
        attrs = seed.get_attrs()
        employee = Employee(self.total, attrs, manages)
        return employee

    def write_out_txt(self, path, org_score=None):
        """
        Write out the organization to the data folder in a text file
        :param path: str
        :param org_score: float or int
        :return:
        """
        with open(path, "w") as f:
            if org_score:
                f.write(f"Organization Score: {org_score}\n")
            self._write_out_txt_helper(f, self.ceo, "")
        return True

    def _write_out_txt_helper(self, f, e, buffer):
        """
        Write out to text file's recursive helper
        :param f: File
        :param e: Employee
        :param buffer: str
        :return:
        """
        demographic = json.dumps(e.attrs)
        line = f"{buffer}id:{e.id}-score:{e.score}-size:{e.size}-demographic:{demographic}\n"
        f.write(line)
        new_buffer = buffer+"    "
        for m in e.manages:
            self._write_out_txt_helper(f, m, new_buffer)


