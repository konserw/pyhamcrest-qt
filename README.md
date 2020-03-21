# pyhamcrest-qt
PyHamcrest extensions for use with Qt (either pyside2 or PyQt5)

## Installation
Install form PyPI:

`pip install pyhamcrest-qt`

## Available Matchers
* `has_item_flags` for comparing QtCore.Qt.ItemFlags
* `has_window_type` for comparing WindowTypes (WIP)

## Usage example
```
from Qt5 import QtCore, QtWidgets
from hamcrest import assert_that
from qtmatchers import has_item_flags

class TestSample:
    def test_fail(self):
        item = QtWidgets.QListWidgetItem()
        assert_that(item.flags(), has_item_flags(QtCore.Qt.ItemIsEnabled))
```
