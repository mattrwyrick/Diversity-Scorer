
from multiprocessing import Pool

from diverstudio.settings import RANDOM_SEED, UNIFORM, X2_MALE, X2_FEMALE, X3_MALE, X3_FEMALE
from diverstudio.models.score import SimpleScore, SimpleChiSqrScore
from diverstudio.presets.generic_interactions import (
    score_generics_from_target_composition,
    score_generics_from_target_composition_multiprocessing
)


Score = SimpleChiSqrScore
scorer_tag = "chi_sq_"
uniform_target_tag = scorer_tag + "uniform_target"
x2_male_target_tag = scorer_tag + "2x_male_target"
x2_female_target_tag = scorer_tag + "2x_female_target"

USE_MULTIPROCESSING = True


if __name__ == "__main__":

    if USE_MULTIPROCESSING:
        with Pool(3) as p:  # use 3 threads simultaneously for faster computation
            uniform_test_args = (Score, UNIFORM, uniform_target_tag, RANDOM_SEED)  # put params in a list for p.map
            x2_male_test_args = (Score, X2_MALE, x2_male_target_tag, RANDOM_SEED)
            x2_female_test_args = (Score, X2_FEMALE, x2_female_target_tag, RANDOM_SEED)
            tests_params = (uniform_test_args, x2_male_test_args, x2_female_test_args)
            p.map(score_generics_from_target_composition_multiprocessing, tests_params)
    else:
        score_generics_from_target_composition(Score, UNIFORM, uniform_target_tag, RANDOM_SEED)
        score_generics_from_target_composition(Score, X2_MALE, x2_male_target_tag, RANDOM_SEED)
        score_generics_from_target_composition(Score, X2_FEMALE, x2_female_target_tag, RANDOM_SEED)

    print("Done! Check /data/ folder for results!")
