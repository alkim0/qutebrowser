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

"""APIs related to cookies."""

from typing import Optional

from qutebrowser.utils import usertypes


class AbstractCookieJar:

    """A class to interact with backend cookie jars."""

    def id(self) -> str:
        """A unique identifier for each cookie jar."""
        raise NotImplementedError

    def set_cookie(self, cookie: usertypes.Cookie) -> None:
        """Adds a cookie to the cookie jar."""
        raise NotImplementedError

    def delete_cookie(self, cookie: usertypes.Cookie) -> None:
        """Removes the cookie from the cookie jar."""
        raise NotImplementedError


_default_cookie_jar: Optional[AbstractCookieJar] = None
_private_cookie_jar: Optional[AbstractCookieJar] = None


def default_cookie_jar() -> Optional[AbstractCookieJar]:
    return _default_cookie_jar


def private_cookie_jar() -> Optional[AbstractCookieJar]:
    return _private_cookie_jar


def set_default_cookie_jar(cookie_jar: AbstractCookieJar) -> None:
    global _default_cookie_jar
    _default_cookie_jar = cookie_jar


def set_private_cookie_jar(cookie_jar: AbstractCookieJar) -> None:
    global _private_cookie_jar
    _private_cookie_jar = cookie_jar
