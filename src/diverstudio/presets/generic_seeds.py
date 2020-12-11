from diverstudio.settings import UNIFORM, X2_MALE, X2_FEMALE, X3_MALE, X3_FEMALE
from diverstudio.tools import ProbValue
from diverstudio.models.employee import load_attribute_generator_from_composition
from diverstudio.models.organization import Seed, OrganizationMaker


PV_0 = [ProbValue(1, 0)]  # 100% chance for value of 0 (depth this means 1 level, breadth this means no expansion)
PV_1 = [ProbValue(1, 8)]  # 100% chance for value of 5
PV_2 = [ProbValue(1, 2), ProbValue(2, 3), ProbValue(2, 4)]  # 20% chance for value of 2, 40% for 3 and 40% for  4


def get_uniform_organization_v1():
    """
    Create a uniform composition organization that is mostly symmetric.
    :return:
    """
    stop_percent = 5  # percent given as a whole number
    generator = load_attribute_generator_from_composition(UNIFORM)
    seed = Seed(attr_gen=generator, pv_depths=PV_1, pv_breadths=PV_2, pv_seeds=[], random_stop=stop_percent)
    organization = OrganizationMaker(seed)
    return organization


def get_2x_male_organization_v1():
    """
    Create a 2x male composition organization that is mostly symmetric.
    :return:
    """
    stop_percent = 5  # percent given as a whole number
    generator = load_attribute_generator_from_composition(X2_MALE)
    seed = Seed(attr_gen=generator, pv_depths=PV_1, pv_breadths=PV_2, pv_seeds=[], random_stop=stop_percent)
    organization = OrganizationMaker(seed)
    return organization


def get_2x_female_organization_v1():
    """
    Create a 2x female composition organization that is mostly symmetric.
    :return:
    """
    stop_percent = 5  # percent given as a whole number
    generator = load_attribute_generator_from_composition(X2_FEMALE)
    seed = Seed(attr_gen=generator, pv_depths=PV_1, pv_breadths=PV_2, pv_seeds=[], random_stop=stop_percent)
    organization = OrganizationMaker(seed)
    return organization


def get_3x_male_organization_v1():
    """
    Create a 3x male composition organization that is mostly symmetric.
    :return:
    """
    stop_percent = 5  # percent given as a whole number
    generator = load_attribute_generator_from_composition(X3_MALE)
    seed = Seed(attr_gen=generator, pv_depths=PV_1, pv_breadths=PV_2, pv_seeds=[], random_stop=stop_percent)
    organization = OrganizationMaker(seed)
    return organization


def get_3x_female_organization_v1():
    """
    Create a 3x female composition organization that is mostly symmetric.
    :return:
    """
    stop_percent = 5  # percent given as a whole number
    generator = load_attribute_generator_from_composition(X3_FEMALE)
    seed = Seed(attr_gen=generator, pv_depths=PV_1, pv_breadths=PV_2, pv_seeds=[], random_stop=stop_percent)
    organization = OrganizationMaker(seed)
    return organization
