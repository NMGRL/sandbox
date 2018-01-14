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
from pyface.action.menu_manager import MenuManager
from pyface.image_resource import ImageResource
from traits.has_traits import HasTraits
from traits.trait_types import List, Int, Dict
from traits.traits import Property
from traitsui.menu import Action
from traitsui.tabular_adapter import TabularAdapter

from identifier import make_aliquot_step

GRAY_BALL = ImageResource('gray_ball')
GREEN_BALL = ImageResource('green_ball')
ORANGE_BALL = ImageResource('orange_ball')

COLORS = {'success': 'white',
          'extraction': 'white',
          'measurement': 'white',
          'canceled': 'white',
          'truncated': 'white',
          'failed': 'white',
          'end_after': 'white',
          'invalid': 'red',
          'aborted': 'orange'}


def to_bool(a):
    """
        a: a str or bool object

        if a is string
            'true', 't', 'yes', 'y', '1', 'ok' ==> True
            'false', 'f', 'no', 'n', '0' ==> False
    """

    if isinstance(a, bool):
        return a
    elif a is None:
        return False
    elif isinstance(a, (int, float)):
        return bool(a)

    tks = ['true', 't', 'yes', 'y', '1', 'ok', 'open']
    fks = ['false', 'f', 'no', 'n', '0', 'closed']

    # if a is not None:
    #     a = str(a).strip().lower()

    a = str(a).strip().lower()
    if a in tks:
        return True
    elif a in fks:
        return False


class ConfigurableMixin(HasTraits):
    all_columns = List
    all_columns_dict = Property

    def _get_all_columns_dict(self):
        return dict(self.all_columns)


class ExecutedAutomatedRunSpecAdapter(TabularAdapter, ConfigurableMixin):
    all_columns = [('Idx', 'idx'),
                   ('-', 'result'),
                   ('Labnumber', 'labnumber'),
                   ('Aliquot', 'aliquot'),
                   ('Sample', 'sample'),
                   ('Project', 'project'),
                   ('Material', 'material'),
                   ('RepositoryID', 'repository_identifier'),
                   ('Position', 'position'),
                   ('Extract', 'extract_value'),
                   ('Units', 'extract_units'),
                   ('Ramp (s)', 'ramp_duration'),
                   ('Duration (s)', 'duration'),
                   ('Cleanup (s)', 'cleanup'),
                   ('Overlap (s)', 'overlap'),
                   ('Beam (mm)', 'beam_diameter'),
                   ('Pattern', 'pattern'),
                   ('Extraction', 'extraction_script'),
                   ('T_o Offset', 'collection_time_zero_offset'),
                   ('Measurement', 'measurement_script'),
                   ('Conditionals', 'conditionals'),
                   ('SynExtraction', 'syn_extraction'),
                   ('CDDWarm', 'use_cdd_warming'),
                   ('Post Eq.', 'post_equilibration_script'),
                   ('Post Meas.', 'post_measurement_script'),
                   ('Options', 'script_options'),
                   ('Comment', 'comment'),
                   ('Delay After', 'delay_after')]

    columns = [('Idx', 'idx'),
               ('-', 'result'),
               ('Labnumber', 'labnumber'),
               ('Aliquot', 'aliquot'),
               ('Sample', 'sample'),
               ('Project', 'project'),
               ('Material', 'material'),
               ('RepositoryID', 'repository_identifier'),
               ('Position', 'position'),
               ('Extract', 'extract_value'),
               ('Units', 'extract_units'),
               ('Ramp (s)', 'ramp_duration'),
               ('Duration (s)', 'duration'),
               ('Cleanup (s)', 'cleanup'),
               ('Overlap (s)', 'overlap'),
               ('Beam (mm)', 'beam_diameter'),
               ('Pattern', 'pattern'),
               ('Extraction', 'extraction_script'),
               ('T_o Offset', 'collection_time_zero_offset'),
               ('Measurement', 'measurement_script'),
               ('Conditionals', 'conditionals'),
               ('SynExtraction', 'syn_extraction'),
               ('CDDWarm', 'use_cdd_warming'),
               ('Post Eq.', 'post_equilibration_script'),
               ('Post Meas.', 'post_measurement_script'),
               ('Options', 'script_options'),
               ('Comment', 'comment'),
               ('Delay After', 'delay_after')]
    font = 'arial 10'
    # all_columns = List
    # all_columns_dict = Dict
    # ===========================================================================
    # widths
    # ===========================================================================
    result_width = Int(25)
    repository_identifier_width = Int(90)
    labnumber_width = Int(80)
    aliquot_width = Int(60)
    sample_width = Int(50)
    position_width = Int(50)
    extract_value_width = Int(50)
    extract_units_width = Int(40)
    duration_width = Int(70)
    ramp_duration_width = Int(50)
    cleanup_width = Int(70)
    pattern_width = Int(80)
    beam_diameter_width = Int(65)

    overlap_width = Int(50)
    # autocenter_width = Int(70)
    #    extract_device_width = Int(125)
    extraction_script_width = Int(80)
    measurement_script_width = Int(90)
    conditionals_width = Int(80)
    syn_extraction_width = Int(80)
    use_cdd_warming_width = Int(80)
    post_measurement_script_width = Int(90)
    post_equilibration_script_width = Int(90)

    position_text = Property
    comment_width = Int(125)
    # ===========================================================================
    # number values
    # ===========================================================================
    ramp_duration_text = Property
    extract_value_text = Property
    beam_diameter_text = Property
    duration_text = Property
    cleanup_text = Property

    aliquot_text = Property
    overlap_text = Property

    # ===========================================================================
    # non cell editable
    # ===========================================================================
    labnumber_text = Property
    result_text = Property
    extraction_script_text = Property
    measurement_script_text = Property
    post_measurement_script_text = Property
    post_equilibration_script_text = Property
    sample_text = Property
    use_cdd_warming_text = Property
    colors = Dict(COLORS)

    image = Property
    menu = Property
    tooltip = Property

    def _get_tooltip(self):
        name = self.column_id
        item = self.item
        if name == 'result':
            if item.state in ('success', 'truncated'):
                return item.result.summary
        else:
            return '{}= {}\nstate= {}'.format(name, getattr(item, name), item.state)

    # def get_tooltip(self, obj, trait, row, column):
    #     name = self.column_map[column]
    #     item = getattr(obj, trait)[row]
    #     if name == 'result':
    #         if item.state in ('success', 'truncated'):
    #             return item.result.summary
    #     else:
    #         return '{}= {}\nstate= {}'.format(name, getattr(item, name), item.state)

    # def get_row_label(self, section, obj=None):
    #     return section + 1

    def get_bg_color(self, obj, trait, row, column=0):
        # item = self.item
        item = getattr(obj, trait)[row]
        # print item.identifier, item.state, item.executable
        if not item.executable:
            color = 'red'
        else:
            if item.skip:
                color = 'blue'  # '#33CCFF'  # light blue
            elif item.state in self.colors:
                color = self.colors[item.state]
            elif item.end_after:
                color = 'grey'
            else:
                if row % 2 == 0:
                    # color = 'white'
                    # color = self.even_bg_color
                    color = self.even_bg_color
                else:
                    color = self.odd_bg_color  # '#E6F2FF'  # light gray blue
                    # print row, color, self.odd_bg_color, self.even_bg_color

        return color

    def _get_image(self):
        if self.column_id == 'result':
            if self.item.state == 'success':
                return GREEN_BALL
            elif self.item.state == 'truncated':
                return ORANGE_BALL

    # def get_image(self, obj, trait, row, column):
    #     name = self.column_map[column]
    #     if name == 'result':
    #         item = getattr(obj, trait)[row]
    #         if item.state == 'success':
    #             return GREEN_BALL
    #         elif item.state == 'truncated':
    #             return ORANGE_BALL
    def _get_menu(self):
        item = self.item
        if item.state in ('success', 'truncated'):

            evo_actions = [Action(name='Show All', action='show_evolutions'),
                           Action(name='Show All w/Equilibration', action='show_evolutions_w_eq'),
                           Action(name='Show All w/Equilibration+Baseline', action='show_evolutions_w_eq_bs'),
                           Action(name='Show All w/Baseline', action='show_evolutions_w_bs')]
            for iso in item.result.isotope_group.iter_isotopes():
                actions = [Action(name='Signal', action='show_evolution_{}'.format(iso.name)),
                           Action(name='Equilibration/Signal', action='show_evolution_eq_{}'.format(iso.name)),
                           Action(name='Equilibration/Signal/Baseline',
                                  action='show_evolution_eq_bs_{}'.format(iso.name)),
                           Action(name='Signal/Baseline', action='show_evolution_bs_{}'.format(iso.name))]
                m = MenuManager(*actions, name=iso.name)
                evo_actions.append(m)

            evo = MenuManager(*evo_actions, name='Evolutions')

            success = MenuManager(Action(name='Summary', action='show_summary'),
                                  evo)
            return success

    # def get_menu(self, obj, trait, row, column):
    #     item = getattr(obj, trait)[row]
    #     if item.state in ('success', 'truncated'):
    #
    #         evo_actions = [Action(name='Show All', action='show_evolutions'),
    #                        Action(name='Show All w/Equilibration', action='show_evolutions_w_eq'),
    #                        Action(name='Show All w/Equilibration+Baseline', action='show_evolutions_w_eq_bs'),
    #                        Action(name='Show All w/Baseline', action='show_evolutions_w_bs')]
    #         for iso in item.result.isotope_group.iter_isotopes():
    #             actions = [Action(name='Signal', action='show_evolution_{}'.format(iso.name)),
    #                        Action(name='Equilibration/Signal', action='show_evolution_eq_{}'.format(iso.name)),
    #                        Action(name='Equilibration/Signal/Baseline',
    #                               action='show_evolution_eq_bs_{}'.format(iso.name)),
    #                        Action(name='Signal/Baseline', action='show_evolution_bs_{}'.format(iso.name))]
    #             m = MenuManager(*actions, name=iso.name)
    #             evo_actions.append(m)
    #
    #         evo = MenuManager(*evo_actions, name='Evolutions')
    #
    #         success = MenuManager(Action(name='Summary', action='show_summary'),
    #                               evo)
    #         return success

    # ============ non cell editable ============
    def _get_result_text(self):
        return ''

    def _set_result_text(self, v):
        pass

    def _get_position_text(self):
        at = self.item.analysis_type
        p = self.item.position
        if at not in ('unknown', 'degas'):
            if at == 'blank_unknown':
                if ',' not in p:
                    p = ''
            else:
                p = ''
        return p

    def _get_labnumber_text(self):
        return self.item.labnumber

    def _set_labnumber_text(self, v):
        pass

    def _set_sample_text(self, v):
        pass

    def _get_sample_text(self):
        return self.item.sample

    def _get_extraction_script_text(self):
        return self.item.extraction_script

    def _get_measurement_script_text(self):
        return self.item.measurement_script

    def _get_post_measurement_script_text(self):
        return self.item.post_measurement_script

    def _get_post_equilibration_script_text(self):
        return self.item.post_equilibration_script

    def _set_extraction_script_text(self, v):
        pass

    def _set_measurement_script_text(self, v):
        pass

    def _set_post_measurement_script_text(self, v):
        pass

    def _set_post_equilibration_script_text(self, v):
        pass

    def _set_position_text(self, v):
        pass

    # ============================================

    def _get_overlap_text(self):
        o, m = self.item.overlap
        if m:
            return '{},{}'.format(o, m)
        else:
            if int(o):
                return '{}'.format(o)
        return ''

    def _get_aliquot_text(self):
        al = ''
        it = self.item
        if it.aliquot != 0:
            al = make_aliquot_step(it.aliquot, it.step)

        return al

    def _get_ramp_duration_text(self):
        return self._get_number('ramp_duration', fmt='{:n}')

    def _get_beam_diameter_text(self):
        return self._get_number('beam_diameter')

    def _get_extract_value_text(self):
        return self._get_number('extract_value')

    def _get_duration_text(self):
        return self._get_number('duration')

    def _get_cleanup_text(self):
        return self._get_number('cleanup')

    def _get_use_cdd_warming_text(self):
        return 'Yes' if self.item.use_cdd_warming else 'No'

    # ===============set================
    def _set_ramp_duration_text(self, v):
        self._set_number(v, 'ramp_duration')

    def _set_beam_diameter_text(self, v):
        self._set_number(v, 'beam_diameter')

    def _set_extract_value_text(self, v):
        self._set_number(v, 'extract_value')

    def _set_duration_text(self, v):
        self._set_number(v, 'duration')

    def _set_cleanup_text(self, v):
        self._set_number(v, 'cleanup')

    def _set_use_cdd_warming_text(self, v):
        self.item.use_cdd_warming = to_bool(v)

    def _set_aliquot_text(self, v):
        self.item.user_defined_aliquot = int(v)

    # ==============validate================
    def _validate_aliquot_text(self, v):
        return self._validate_number(v, 'aliquot', kind=int)

    def _validate_extract_value_text(self, v):
        return self._validate_number(v, 'extract_value')

    def _validate_ramp_duration_text(self, v):
        return self._validate_number(v, 'ramp_duration')

    def _validate_beam_diameter_text(self, v):
        return self._validate_number(v, 'beam_diameter')

    def _validate_extract_value_text(self, v):
        return self._validate_number(v, 'extract_value')

    def _validate_duration_text(self, v):
        return self._validate_number(v, 'duration')

    def _validate_cleanup_text(self, v):
        return self._validate_number(v, 'cleanup')

    # ==========helpers==============
    def _set_number(self, v, attr):
        setattr(self.item, attr, v)

    def _validate_number(self, v, attr, kind=float):
        try:
            return kind(v)
        except ValueError:
            return getattr(self.item, attr)

    def _get_number(self, attr, fmt='{:0.2f}'):
        """
            dont display 0.0's
        """
        v = getattr(self.item, attr)
        if v:
            if isinstance(v, str):
                v = float(v)

            return fmt.format(v)
        else:
            return ''


class AutomatedRunMixin(object):
    """
        mixin for table of automated runs that have not yet been executed
    """

    def get_menu(self, *args):
        jump = MenuManager(Action(name='Jump to End', action='jump_to_end'),
                           Action(name='Jump to Start', action='jump_to_start'),
                           name='Jump')

        move = MenuManager(Action(name='Move to Start', action='move_to_start'),
                           Action(name='Move to End', action='move_to_end'),
                           Action(name='Move to ...', action='move_to_row'),
                           name='Move')
        copy = MenuManager(Action(name='Copy to Start', action='copy_to_start'),
                           Action(name='Copy to End', action='copy_to_end'),
                           name='Copy')

        blocks = MenuManager(Action(name='Make Block', action='make_block'),
                             Action(name='Repeat Block', action='repeat_block'),
                             name='Blocks')
        selects = MenuManager(Action(name='Select Unknowns', action='select_unknowns'),
                              Action(name='Select Same Labnumber', action='select_same'),
                              Action(name='Select Same Attributes...', action='select_same_attr'),
                              name='Select')

        return MenuManager(move, copy, jump, blocks, selects,
                           Action(name='Unselect', action='unselect'),
                           Action(name='Toggle End After', action='toggle_end_after'),
                           Action(name='Toggle Skip', action='toggle_skip'))


class AutomatedRunSpecAdapter(AutomatedRunMixin, ExecutedAutomatedRunSpecAdapter):
    pass
# ============= EOF =============================================
