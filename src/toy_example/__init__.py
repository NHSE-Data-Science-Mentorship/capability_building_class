from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("toy_example")
except PackageNotFoundError:
    # package is not installed
    pass
