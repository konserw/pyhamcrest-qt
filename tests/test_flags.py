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
from Qt5 import QtCore
from hamcrest import assert_that, calling, raises

from qtmatchers import has_item_flags


class TestItemFlags:
    def test_passing(self):
        # this should not rise
        assert_that(QtCore.Qt.ItemIsSelectable, has_item_flags(QtCore.Qt.ItemIsSelectable))

    def test_different_flag(self):
        assert_that(
            calling(assert_that).with_args(QtCore.Qt.ItemIsSelectable, has_item_flags(QtCore.Qt.ItemIsEnabled)),
            raises(AssertionError, r"Expected: flags: \( ItemIsEnabled \)\s*but: was \( ItemIsSelectable \)", ))

    def test_excess_flag(self):
        assert_that(
            calling(assert_that).with_args(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable, has_item_flags(QtCore.Qt.ItemIsEnabled)),
            raises(AssertionError, r"Expected: flags: \( ItemIsEnabled \)\s*but: was \( ItemIsSelectable | ItemIsEnabled \)", ))

    def test_missing_flag(self):
        assert_that(
            calling(assert_that).with_args(QtCore.Qt.ItemIsEnabled, has_item_flags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)),
            raises(AssertionError, r"Expected: flags: \( ItemIsSelectable | ItemIsEnabled \)\s*but: was \( ItemIsEnabled \)", ))
