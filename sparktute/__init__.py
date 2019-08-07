import sys
import logging


ROOT = logging.getLogger()
ROOT.setLevel(logging.INFO)

if not ROOT.hasHandlers():
    HANDLER = logging.StreamHandler(sys.stdout)
    HANDLER.setLevel(logging.INFO)
    FORMATTER = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s')
    HANDLER.setFormatter(FORMATTER)
    ROOT.addHandler(HANDLER)
