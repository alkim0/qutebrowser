# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2018-2021 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <https://www.gnu.org/licenses/>.

"""Wrappers around Qt/PyQt code."""

# pylint: disable=unused-import
import importlib
from dataclasses import dataclass


@dataclass
class _Machinery:
    IS_QT6: bool
    IS_QT5: bool
    PACKAGE: str


PyQt5 = PyQt6 = False
try:
    import PyQt5 as pyqt  # noqa: N813

    PyQt5 = True
    machinery = _Machinery(
        IS_QT6=False,
        IS_QT5=True,
        PACKAGE="PyQt5",
    )
except ImportError:
    import PyQt6 as pyqt  # type: ignore[import, no-redef] # noqa: N813

    PyQt6 = True
    machinery = _Machinery(
        IS_QT6=True,
        IS_QT5=False,
        PACKAGE="PyQt6",
    )

# While upstream recommends using PyQt5.sip ever since PyQt5 5.11, some distributions
# still package later versions of PyQt5 with a top-level "sip" rather than "PyQt5.sip".
try:
    if PyQt5:
        from PyQt5 import sip
    elif PyQt6:
        from PyQt6 import sip  # type: ignore[no-redef]
except ImportError:
    import sip  # type: ignore[import, no-redef]

# pylint: disable=ungrouped-imports
if PyQt5:
    from PyQt5 import QtCore as core  # type: ignore[no-redef]
    from PyQt5 import QtDBus as dbus  # type: ignore[no-redef]
    from PyQt5 import QtGui as gui  # type: ignore[no-redef]
    from PyQt5 import QtNetwork as network  # type: ignore[no-redef]
    from PyQt5 import QtPrintSupport as printsupport  # type: ignore[no-redef]
    from PyQt5 import QtQml as qml  # type: ignore[no-redef]
    from PyQt5 import QtSql as sql  # type: ignore[no-redef]
    from PyQt5 import QtTest as test  # type: ignore[no-redef]
    from PyQt5 import QtWidgets as widgets  # type: ignore[no-redef]
    opengl = gui  # for QOpenGLVersionProfile
    gui.QFileSystemModel = widgets.QFileSystemModel
    del widgets.QFileSystemModel
elif PyQt6:
    from PyQt6 import QtCore as core  # type: ignore[no-redef]
    from PyQt6 import QtDBus as dbus  # type: ignore[no-redef]
    from PyQt6 import QtGui as gui  # type: ignore[no-redef]
    from PyQt6 import QtNetwork as network  # type: ignore[no-redef]
    from PyQt6 import QtPrintSupport as printsupport  # type: ignore[no-redef]
    from PyQt6 import QtQml as qml  # type: ignore[no-redef]
    from PyQt6 import QtSql as sql  # type: ignore[no-redef]
    from PyQt6 import QtTest as test  # type: ignore[no-redef]
    from PyQt6 import QtWidgets as widgets  # type: ignore[no-redef]
    from PyQt6 import QtOpenGL as opengl  # type: ignore[no-redef]

try:
    if PyQt5:
        from PyQt5 import QtWebEngineCore as webenginecore  # type: ignore[no-redef]
        from PyQt5 import QtWebEngineWidgets as webenginewidgets  # type: ignore[no-redef]
        # Some stuff moved from widgets to core in Qt6
        for attr in [
            "QWebEngineSettings",
            "QWebEngineProfile",
            "QWebEngineDownloadItem",
            "QWebEnginePage",
            "QWebEngineCertificateError",
            "QWebEngineScript",
            "QWebEngineHistory",
            "QWebEngineHistoryItem",
            "QWebEngineScriptCollection",
            "QWebEngineClientCertificateSelection",
            "QWebEngineFullScreenRequest",
            "QWebEngineContextMenuData",
        ]:
            setattr(webenginecore, attr, getattr(webenginewidgets, attr))
            delattr(webenginewidgets, attr)
        webenginecore.QWebEngineDownloadRequest = getattr(  # noqa: B009
            webenginecore,
            "QWebEngineDownloadItem",
        )
        from PyQt5 import QtWebEngine
        for attr in [
            "PYQT_WEBENGINE_VERSION",
            "PYQT_WEBENGINE_VERSION_STR",
        ]:
            setattr(webenginecore, attr, getattr(QtWebEngine, attr))
            delattr(QtWebEngine, attr)
    elif PyQt6:
        from PyQt6 import QtWebEngineCore as webenginecore  # type: ignore[no-redef]
        from PyQt6 import QtWebEngineWidgets as webenginewidgets  # type: ignore[no-redef]
except ImportError:
    webenginecore = None  # type: ignore[assignment]
    webenginewidgets = None  # type: ignore[assignment]

try:
    if PyQt5:
        from PyQt5 import QtWebKit as webkit  # type: ignore[no-redef]
        from PyQt5 import QtWebKitWidgets as webkitwidgets  # type: ignore[no-redef]
    elif PyQt6:
        webkit = None  # type: ignore[assignment]
        webkitwidgets = None  # type: ignore[assignment]
except ImportError:
    webkit = None  # type: ignore[assignment]
    webkitwidgets = None  # type: ignore[assignment]
