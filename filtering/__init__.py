import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version, PackageNotFoundError
else:
    # importlib.metadata was added in Python 3.8; use the backport on 3.7
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version("lagrangian-filtering")
except PackageNotFoundError:
    # Fall back to the version file written by setuptools_scm at build time
    try:
        from filtering._version import version as __version__
    except ImportError:
        __version__ = "unknown"

from filtering.filtering import LagrangeFilter
import filtering.analysis
import filtering.filter
