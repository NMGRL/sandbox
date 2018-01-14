# ===============================================================================
# Copyright 2012 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= enthought library imports =======================
# ============= standard library imports ========================
# ============= local library imports  ==========================
SPECTROMETER_PROTOCOL = 'pychron.spectrometer.base_spectrometer_manager.BaseSpectrometerManager'
ION_OPTICS_PROTOCOL = 'pychron.spectrometer.ion_optics_manager.IonOpticsManager'
SCAN_PROTOCOL = 'pychron.spectrometer.scan_manager.ScanManager'
EL_PROTOCOL = 'pychron.extraction_line.extraction_line_manager.ExtractionLineManager'
DVC_PROTOCOL = 'pychron.dvc.dvc.DVC'
FURNACE_PROTOCOL = 'pychron.furnace.furnace_manager.BaseFurnaceManager'

FONTS = ['Helvetica', 'Arial', 'Courier', 'Menlo', 'Consolas']  # 'Courier','Times-Roman']#['modern', 'arial']
SIZES = [10, 6, 8, 9, 10, 11, 12, 14, 15, 18, 24, 36]

PLUSMINUS = u'\u00b1'
try:
    # PLUSMINUS_ERR = PLUSMINUS + 'Err.'
    PLUSMINUS_ERR = u'{}Err.'.format(PLUSMINUS)
except UnicodeEncodeError:
    PLUSMINUS = '+/-'
    PLUSMINUS_ERR = '{}Err.'.format(PLUSMINUS)

SIGMA = u'\u03c3'

PLUSMINUS_NSIGMA = u'{}{{}}{}'.format(PLUSMINUS, SIGMA)
PLUSMINUS_ONE_SIGMA = PLUSMINUS_NSIGMA.format(1)
# PLUSMINUS_ONE_SIGMA = u'{}1{}'.format(PLUSMINUS, SIGMA)
PLUSMINUS_PERCENT = u'{}%  '.format(PLUSMINUS)

NULL_STR = '---'
LINE_STR = '---------'
SCRIPT_KEYS = ['measurement', 'post_measurement', 'extraction', 'post_equilibration']
SCRIPT_NAMES = ['{}_script'.format(si) for si in SCRIPT_KEYS]

FIT_TYPES = ['Linear', 'Parabolic', 'Cubic',
             'Average', 'Weighted Mean']
FIT_ERROR_TYPES = ['SD', 'SEM', 'CI']

SD = 'SD'
SEM = 'SEM'
MSEM = 'SEM, but if MSWD>1 use SEM * sqrt(MSWD)'
ERROR_TYPES = [MSEM, SEM, SD]

INTERPOLATE_TYPES = ['Preceding', 'Bracketing Interpolate', 'Bracketing Average']
FIT_TYPES_INTERPOLATE = FIT_TYPES + INTERPOLATE_TYPES
DELIMITERS = {',': 'comma', '\t': 'tab', ' ': 'space'}
AGE_SCALARS = {'Ga': 1e9, 'Ma': 1e6, 'ka': 1e3, 'a': 1}
AGE_MA_SCALARS = {'Ma': 1, 'ka': 1e-3, 'a': 1e-6, 'Ga': 1e3}

OMIT_KEYS = ('omit_ideo', 'omit_spec', 'omit_iso', 'omit_series')

UNKNOWN = 'unknown'
COCKTAIL = 'cocktail'
BLANK = 'blank'
DETECTOR_IC = 'detector_ic'

SNIFF = 'sniff'
SIGNAL = 'signal'
BASELINE = 'baseline'
WHIFF = 'whiff'

EXTRACT_DEVICE = 'Extract Device'
NO_EXTRACT_DEVICE = 'No Extract Device'

import string

seeds = string.ascii_uppercase
ALPHAS = [a for a in seeds] + ['{}{}'.format(a, b)
                               for a in seeds
                               for b in seeds]


def alpha_to_int(s):
    return ALPHAS.index(s)


def alphas(idx):
    """
        idx should be 0-base ie. idx=0 ==>A
    """
    if idx < 26:
        return seeds[idx]
    else:
        a = idx / 26 - 1
        b = idx % 26
        return '{}{}'.format(seeds[a], seeds[b])


INTERFERENCE_KEYS = ('K4039', 'K3839', 'K3739', 'Ca3937', 'Ca3837', 'Ca3637', 'Cl3638')
RATIO_KEYS = ('Ca_K', 'Cl_K')

AR40 = 'Ar40'
AR39 = 'Ar39'
AR38 = 'Ar38'
AR37 = 'Ar37'
AR36 = 'Ar36'

ARGON_KEYS = (AR40, AR39, AR38, AR37, AR36)
ISOTOPES = ARGON_KEYS


def set_isotope_names(isos):
    global ISOTOPES
    ISOTOPES = isos


IRRADIATION_KEYS = [('k4039', 'K_40_Over_39'),
                    ('k3839', 'K_38_Over_39'),
                    ('k3739', 'K_37_Over_39'),
                    ('ca3937', 'Ca_39_Over_37'),
                    ('ca3837', 'Ca_38_Over_37'),
                    ('ca3637', 'Ca_36_Over_37'),
                    ('cl3638', 'P36Cl_Over_38Cl')]

DECAY_KEYS = [('a37decayfactor', '37_Decay'),
              ('a39decayfactor', '39_Decay')]

MEASUREMENT_COLOR = '#FF7EDF'  # magenta
EXTRACTION_COLOR = '#FFFF66'
SUCCESS_COLOR = '#66FF33'  # light green
SKIP_COLOR = '#33CCFF'
CANCELED_COLOR = '#FF9999'
TRUNCATED_COLOR = 'orange'
FAILED_COLOR = 'red'
END_AFTER_COLOR = 'gray'
NOT_EXECUTABLE_COLOR = 'red'

LIGHT_RED = '#FF7373'
LIGHT_YELLOW = '#F7F6D0'
LIGHT_GREEN = '#99FF99'

DETECTOR_ORDER = ['H2', 'H1', 'AX', 'L1', 'L2', 'CDD']
DETECTOR_MAP = {o: i for i, o in enumerate(DETECTOR_ORDER)}

IC_ANALYSIS_TYPE_MAP = {'air': 0, 'cocktail': 1}

QTEGRA_INTEGRATION_TIMES = [0.065536, 0.131072, 0.262144, 0.524288,
                            1.048576, 2.097152, 4.194304, 8.388608,
                            16.777216, 33.554432, 67.108864]
QTEGRA_DEFAULT_INTEGRATION_TIME = 1.048576
DEFAULT_INTEGRATION_TIME = 1

ISOTOPX_INTEGRATION_TIMES = [1, 2, 3]
ISOTOPX_DEFAULT_INTEGRATION_TIME = 1
DEFAULT_INTEGRATION_TIME = 1

K_DECAY_CONSTANTS = {'Min et al., 2000': (5.80e-11, 0, 4.884e-10, 0),
                     'Steiger & Jager 1977': (5.81e-11, 0, 4.962e-10, 0)}

FLUX_CONSTANTS = {'Min et al., 2000': (5.80e-11, 0, 4.884e-10, 0, 28.201),
                  'Steiger & Jager 1977': (5.81e-11, 0, 4.962e-10, 0, 28.02)}

AR_AR = 'Ar/Ar'
# MINNA_BLUFF_IRRADIATIONS = [('NM-205', ['E', 'F' , 'G', 'H', 'O']),
# ('NM-213', ['A', 'C', 'I', 'J', 'K', 'L']),
# ('NM-216', ['C', 'D', 'E', 'F']),
# ('NM-220', ['L', 'M', 'N', 'O']),
# ('NM-222', ['A', 'B', 'C', 'D']),
# ('NM-256', ['E', 'F'])]

QTEGRA_SOURCE_KEYS = ('extraction_lens', 'ysymmetry', 'zsymmetry', 'zfocus')
QTEGRA_SOURCE_NAMES = ('ExtractionLens', 'Y-Symmetry', 'Z-Symmetry', 'Z-Focus')

ANALYSIS_TYPES = ['Unknown', 'Air', 'Cocktail', 'Blank Unknown', 'Blank Air', 'Blank Cocktail', 'Blank']
# ============= EOF =============================================
