from importlib.metadata import version, PackageNotFoundError

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
