from api.config import PACKAGE_ROOT
from regression_model.config import config

with open(PACKAGE_ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()
