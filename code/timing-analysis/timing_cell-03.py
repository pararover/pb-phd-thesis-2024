import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import pandas as pd
import os

from astropy.io import fits
from astropy.timeseries import LombScargle

from scipy.optimize import curve_fit