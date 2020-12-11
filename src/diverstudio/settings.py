import os
import random

from pathlib import Path


RANDOM_SEED = 1234567890
random.seed(RANDOM_SEED)

APP_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
SRC_DIRECTORY = Path(APP_DIRECTORY).parent
ROOT_DIRECTORY = Path(SRC_DIRECTORY).parent
DATA_DIRECTORY = os.path.join(ROOT_DIRECTORY, "data")
COMPOSITION_DIRECTORY = os.path.join(APP_DIRECTORY, "presets", "compositions")

# composition names
UNIFORM = os.path.join(COMPOSITION_DIRECTORY, "uniform.json")
X2_MALE = os.path.join(COMPOSITION_DIRECTORY, "2x_male.json")
X2_FEMALE = os.path.join(COMPOSITION_DIRECTORY, "2x_female.json")
X3_MALE = os.path.join(COMPOSITION_DIRECTORY, "3x_male.json")
X3_FEMALE = os.path.join(COMPOSITION_DIRECTORY, "3x_female.json")
