# pyhamcrest-qt - PyHamcrest extensions for use with Qt (either pyside2 or PyQt5)
# Copyright (C) 2020 Kamil 'konserw' Strzempowicz, konserw@gmail.com
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License, or any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
import pytest
from Qt5 import QtWidgets
from hamcrest import assert_that, calling, raises, is_

from qtmatchers import enabled, disabled, checked, unchecked


@pytest.fixture
def enabled_widget(qtbot):
    widget = QtWidgets.QWidget()
    qtbot.addWidget(widget)
    return widget


@pytest.fixture
def disabled_widget(qtbot):
    widget = QtWidgets.QWidget()
    widget.setEnabled(False)
    qtbot.addWidget(widget)
    return widget


@pytest.fixture
def checked_radiobutton(qtbot):
    widget = QtWidgets.QRadioButton()
    widget.setChecked(True)
    qtbot.addWidget(widget)
    return widget


@pytest.fixture
def unchecked_radiobutton(qtbot):
    widget = QtWidgets.QRadioButton()
    widget.setChecked(False)
    qtbot.addWidget(widget)
    return widget


class TestProperties:
    def test_enabled_passing(self, enabled_widget):
        # this should not rise
        assert_that(enabled_widget, is_(enabled()))

    def test_disabled_passing(self, disabled_widget):
        # this should not rise
        assert_that(disabled_widget, is_(disabled()))

    def test_enabled_failing(self, disabled_widget):
        assert_that(
            calling(assert_that).with_args(disabled_widget, is_(enabled())),
            raises(AssertionError, r"Expected: widget to be enabled.\n"
                                   r"\s*but: was disabled"
                   )
        )

    def test_disabled_failing(self, enabled_widget):
        assert_that(
            calling(assert_that).with_args(enabled_widget, is_(disabled())),
            raises(AssertionError, r"Expected: widget to be disabled.\n"
                                   r"\s*but: was enabled"
                   )
        )

    def test_checked_passing(self, checked_radiobutton):
        # this should not rise
        assert_that(checked_radiobutton, is_(checked()))

    def test_unchecked_passing(self, unchecked_radiobutton):
        # this should not rise
        assert_that(unchecked_radiobutton, is_(unchecked()))

    def test_checked_failing(self, unchecked_radiobutton):
        assert_that(
            calling(assert_that).with_args(unchecked_radiobutton, is_(checked())),
            raises(AssertionError, r"Expected: widget to be checked.\n"
                                   r"\s*but: was unchecked"
                   )
        )

    def test_unchecked_failing(self, checked_radiobutton):
        assert_that(
            calling(assert_that).with_args(checked_radiobutton, is_(unchecked())),
            raises(AssertionError, r"Expected: widget to be unchecked.\n"
                                   r"\s*but: was checked"
                   )
        )
