from os import makedirs
from os.path import abspath, dirname, exists, join

BASE_DIR = join(dirname(abspath(__file__)), "../")
DATA_DIR = join(BASE_DIR, "data/")
IMAGE_DIR = join(DATA_DIR, "images")
LABEL_DIR = join(DATA_DIR, "labels")

if not exists(IMAGE_DIR):
    makedirs(IMAGE_DIR)

if not exists(LABEL_DIR):
    makedirs(LABEL_DIR)
