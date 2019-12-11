# coding=utf-8

import sys

__all__ = ['BytesIO']

PY2 = sys.version_info[0] == 2

if PY2:
    import StringIO
    BytesIO = StringIO.StringIO
else:
    import io
    BytesIO = io.BytesIO
