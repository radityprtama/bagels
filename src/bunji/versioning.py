from pathlib import Path
import tomllib
import requests
from packaging import version
from importlib.metadata import PackageNotFoundError, metadata


def get_project_metadata():
    try:
        meta = metadata("bunji")
        return {"Name": meta["Name"], "Version": meta["Version"]}
    except PackageNotFoundError:
        pyproject = Path(__file__).resolve().parents[2] / "pyproject.toml"
        with pyproject.open("rb") as file:
            project = tomllib.load(file)["project"]
        return {"Name": project["name"], "Version": project["version"]}


def get_pypi_version():
    """Fetch the latest version from PyPI."""
    try:
        response = requests.get("https://pypi.org/pypi/bunji/json")
        return response.json()["info"]["version"]
    except Exception:
        return None


def get_current_version():
    return get_project_metadata()["Version"]


def needs_update():
    """Check if the current version needs an update."""
    pypi_version = get_pypi_version()
    current_version = get_current_version()
    if not pypi_version:
        return False

    return version.parse(pypi_version) > version.parse(current_version)
