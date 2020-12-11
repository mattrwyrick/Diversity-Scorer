import os
import random

from diverstudio.settings import DATA_DIRECTORY, UNIFORM
from diverstudio.models.score import SimpleScore
from diverstudio.presets.generic_targets import load_target_from_composition_all_fields

from diverstudio.presets.generic_seeds import (
    get_uniform_organization_v1,
    get_2x_male_organization_v1,
    get_2x_female_organization_v1,
    get_3x_male_organization_v1,
    get_3x_female_organization_v1
)


def score_generics_from_target_composition_multiprocessing(args):
    """
    Call this method to pack the parameters into one object to allow for multriprocessing
    :param args: list of [str, str, int]
    :return:
    """
    return score_generics_from_target_composition(*args)


def score_generics_from_target_composition(Score, composition_path, run_tag="", random_seed=None):
    """
    Score all the generics on a target composition
    :param Score: Class <ScoringAid Subclass>
    :param composition_path: str
    :param run_tag: str (use this to differentiate file names for runs)
    :param random_seed: int
    :return:
    """
    if random_seed:
        random.seed(random_seed)

    target_demo, target_keys = load_target_from_composition_all_fields(composition_path)

    uniform_organization = get_uniform_organization_v1()
    male_2x_organization = get_2x_male_organization_v1()
    female_2x_organization = get_2x_female_organization_v1()
    male_3x_organization = get_3x_male_organization_v1()
    female_3x_organization = get_3x_female_organization_v1()

    uniform_score_obj = Score(target_demo, target_keys, uniform_organization.ceo)
    male_2x_score_obj = Score(target_demo, target_keys, male_2x_organization.ceo)
    female_2x_score_obj = Score(target_demo, target_keys, female_2x_organization.ceo)
    male_3x_score_obj = Score(target_demo, target_keys, male_3x_organization.ceo)
    female_3x_score_obj = Score(target_demo, target_keys, female_3x_organization.ceo)

    uniform_score = uniform_score_obj.score
    male_2x_score = male_2x_score_obj.score
    female_2x_score = female_2x_score_obj.score
    male_3x_score = male_3x_score_obj.score
    female_3x_score = female_3x_score_obj.score

    uniform_output_path = os.path.join(DATA_DIRECTORY, f"{run_tag}_org_uniform.txt")
    male_2x_output_path = os.path.join(DATA_DIRECTORY, f"{run_tag}_org_male_2x.txt")
    female_2x_output_path = os.path.join(DATA_DIRECTORY, f"{run_tag}_org_female_2x.txt")
    male_3x_output_path = os.path.join(DATA_DIRECTORY, f"{run_tag}_org_male_3x.txt")
    female_3x_output_path = os.path.join(DATA_DIRECTORY, f"{run_tag}_female_3x.txt")

    uniform_organization.write_out_txt(uniform_output_path, org_score=uniform_score)
    male_2x_organization.write_out_txt(male_2x_output_path, org_score=male_2x_score)
    female_2x_organization.write_out_txt(female_2x_output_path, org_score=female_2x_score)
    male_3x_organization.write_out_txt(male_3x_output_path, org_score=male_3x_score)
    female_3x_organization.write_out_txt(female_3x_output_path, org_score=female_3x_score)

    print(f"{run_tag} organization scores")
    print(f"{uniform_score} uniform")
    print(f"{male_2x_score} male 2x")
    print(f"{female_2x_score} female 2x")
    print(f"{male_3x_score} male 3x")
    print(f"{female_3x_score} female 3x")
    print()

    return uniform_score, male_2x_score, female_2x_score, male_3x_score, female_3x_score

