# ===============================================================================
# Copyright 2018 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
import string

from traits.api import HasTraits, List, Int, Property
# from traitsui.editors import TabularEditor
from traitsui.api import UItem, View
from traitsui.tabular_adapter import TabularAdapter

from automated_run_adapter import AutomatedRunSpecAdapter
from automated_run_spec import AutomatedRunSpec
from my_tabular_editor import TabularEditor, myTabularEditor


class ShortRow(HasTraits):
    idx = Int
    a = Int


class Row(ShortRow):
    b = Int
    c = Int
    d = Int
    e = Int
    f = Int
    g = Int
    h = Int
    i = Int
    j = Int
    k = Int
    l = Int
    m = Int
    n = Int
    o = Int
    p = Int
    q = Int
    r = Int
    s = Int
    t = Int
    u = Int
    v = Int
    w = Int
    x = Int
    y = Int
    z = Int


class Demo(HasTraits):
    rows = List
    short_rows = List
    runs = List

    def _runs_default(self):
        return [AutomatedRunSpec(idx=i) for i in xrange(400)]

    def _short_rows_default(self):
        return [ShortRow(idx=i) for i in xrange(400)]

    def _rows_default(self):
        return [Row(idx=i) for i in xrange(400)]


class RowsAdapter(TabularAdapter):
    columns = [('Idx', 'idx'), ('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e'),
               ('F', 'f'), ('G', 'g'), ('H', 'h'), ('I', 'i'), ('J', 'j'),
               ('K', 'k'), ('L', 'l'), ('M', 'm'), ('N', 'n'), ('O', 'o'),
               ('P', 'p'), ('Q', 'q'), ('R', 'r'), ('S', 's'), ('T', 't'),
               ('U', 'u'), ('V', 'v'), ('W', 'w'), ('X', 'x'), ('Y', 'y'), ('Z', 'z')]


class ShortRowsAdapter(TabularAdapter):
    columns = [('Idx', 'idx'),
               ('A', 'a')]


view = View(UItem('rows',
                  editor=TabularEditor(adapter=RowsAdapter())),
            UItem('short_rows',
                  editor=TabularEditor(adapter=ShortRowsAdapter())),
            UItem('runs', editor=myTabularEditor(adapter=AutomatedRunSpecAdapter())),
            resizable=True)

if __name__ == '__main__':
    d = Demo()
    d.configure_traits(view=view)
# ============= EOF =============================================
