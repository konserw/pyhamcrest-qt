from Qt5 import QtCore, QtWidgets
from hamcrest import assert_that, is_

from qtmatchers import has_item_flags, enabled


class TestSample:
    def test_pass(self):
        item = QtWidgets.QListWidgetItem()
        assert_that(item.flags(), has_item_flags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsSelectable))

    def test_fail(self):
        item = QtWidgets.QListWidgetItem()
        assert_that(item.flags(), has_item_flags(QtCore.Qt.ItemIsEnabled))
