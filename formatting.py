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
import math
from functools import partial


# ============= local library imports  ==========================
from uncertainties import std_dev, nominal_value


def uformat_percent_error(u, *args, **kw):
    return format_percent_error(nominal_value(u), std_dev(u), *args, **kw)


def format_percent_error(v, e, n=2, include_percent_sign=False):
    p = calc_percent_error(v, e)
    if not p == 'NaN':
        sigpee = '{{:0.{}f}}'.format(n).format(p)
        if include_percent_sign:
            sigpee = '{}%'.format(sigpee)
    else:
        sigpee = 'NaN'
    return sigpee


def calc_percent_error(v, e, scale=100):
    try:
        return abs(e / v * scale)
    except (ZeroDivisionError, TypeError):
        return 'NaN'


def errorfmt(v, e):
    pe = format_percent_error(v, e)
    return '{} ({}%)'.format(floatfmt(e), pe)


def floatfmt(f, n=4, s=4, max_width=None, default='NaN', use_scientific=False):
    """
        f: value to format
        n: number of sig figs

        use scientific notation
        if f<10^-n (e.g n=#.## f=0.00001)
        or
        f>10^(s+1) (e.g  s=### f=3001)

    """
    if isinstance(f, str):
        return f
    if f is None:
        return default

    absf = abs(f)
    if absf < 1e-20:
        v = '0.0'
    else:
        if absf < math.pow(10, -n) or absf > math.pow(10, s + 1):
            if use_scientific:
                fmt = '{{:0.{}E}}'.format(s)
            else:
                if absf < math.pow(10, s + 1):
                    # f = Decimal(f)
                    # n = int(math.ceil(abs(math.log10(absf))))
                    n = int(round(abs(math.log10(absf))))

                fmt = '{{:0.{}f}}'.format(n)

        else:
            fmt = '{{:0.{}f}}'.format(n)

        v = fmt.format(f)
        if max_width:
            if len(v) > max_width:
                v = v[:max_width]

    return v


def pfloatfmt(**kw):
    return partial(floatfmt, **kw)

# ============= EOF =============================================
