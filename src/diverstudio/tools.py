import random


class ProbValue(object):

    def __init__(self, amount, value):
        """
        Creates a container for representing a probabilistic value
        :param amount: int
        :param value: any
        """
        self.amount = amount
        self.value = value

    @staticmethod
    def get_probability_list(pvs):
        """
        Create a list that represents probabilistic likelihood of choosing a value
        :param pvs: list of ProbValue
        :return: list of ProbValue.value
        """
        probability = []
        for pv in pvs:
            amount = pv.amount
            value = pv.value
            for i in range(amount):
                probability.append(value)
        random.shuffle(probability)
        return probability

    @staticmethod
    def get_value_from_probability_list(pvs, total):
        """
        Return a value from the list of probabilities
        :param pvs:
        :param total:
        :return:
        """
        if total < 1:
            return None
        n = random.randint(0, total-1)
        return pvs[n]


class ScoringAid(object):

    def __init__(self, pv_attrs, target_keys, employee):
        self.target_keys = target_keys
        self.pv_attrs = pv_attrs
        self.demographic_keys = self._get_all_demographic_keys()

        self.target_distribution = self.get_target_distribution()
        self.populate_employee_demographic_distribution(employee)
        self.actual_distribution = employee.distribution
        self.ceo = employee
        self.score = None  # up to scoring subclass to override with a meaningful number

    def get_target_distribution(self):
        """
        Get the target distribution from the prob values
        :return:
        """
        total = 0
        distribution_dict = dict()

        for pv in self.pv_attrs:
            total += pv.amount

        for pv in self.pv_attrs:
            demographic_key = "-".join([pv.value[key] for key in self.target_keys])
            distribution_dict[demographic_key] = pv.amount / total

        return distribution_dict

    def _get_all_demographic_keys(self):
        """
        Return a list of all demographic keys
        :return:
        """
        keys = []
        for pv in self.pv_attrs:
            demographic_key = "-".join([pv.value[key] for key in self.target_keys])
            keys.append(demographic_key)
        return keys

    def get_demographic_key_from_employee(self, e):
        """
        Get the demographic key from an employee
        :param e: Employee
        :return:
        """
        demographic_key = "-".join([e.attrs[key] for key in self.target_keys])
        return demographic_key

    def get_empty_demographics_counter(self):
        """
        Return a dictionary with the amount of each demographic
        :return:
        """
        demographics = dict()
        for key in self.demographic_keys:
            demographics[key] = 0
        return demographics

    def populate_employee_demographic_distribution(self, employee):
        """
        Iterate the organizational tree and populate the demographic counter with each employee's demographic
        :param employee:
        :return:
        """
        manages_demographics = []
        if len(employee.manages) > 0:
            for subordinate in employee.manages:
                manages_demographics.append(self.populate_employee_demographic_distribution(subordinate))

        edemographic_counter = self.get_empty_demographics_counter()
        for mdemographic_counter in manages_demographics:
            for key in mdemographic_counter:
                edemographic_counter[key] += mdemographic_counter[key]

        edemographic_key = self.get_demographic_key_from_employee(employee)
        edemographic_counter[edemographic_key] += 1
        employee.distribution = self.get_distribution_from_counter(edemographic_counter)
        return edemographic_counter

    @staticmethod
    def get_distribution_from_counter(counter):
        """
        Return a distribution (%s) of the amounts in the counter
        :param counter: dict of str:int
        :return:
        """
        total = 0
        for key in counter:
            total += counter[key]

        distribution = dict()
        for key in counter:
            distribution[key] = counter[key] / total

        return distribution




