import math
import operator
from loguru import logger
import numpy as np
from collections import defaultdict
from urllib.parse import urljoin
from ..utils.cluster import cluster_dict


LIST_MIN_NUMBER = 5
LIST_MIN_LENGTH = 8
LIST_MAX_LENGTH = 44
SIMILARITY_THRESHOLD = 0.8