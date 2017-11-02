from setuptools import setup, find_packages
import pkg_resources

install_requires = ['cairocffi']

def package_installed(pkg):
    """Check if package is installed"""
    req = pkg_resources.Requirement.parse(pkg)
    try:
        pkg_resources.get_provider(req)
    except pkg_resources.DistributionNotFound:
        return False
    else:
        return True

# depend in Pillow if it is installed, otherwise
# depend on PIL if it is installed, otherwise
# require Pillow
if package_installed('Pillow'):
    install_requires.append('Pillow !=2.4.0')
elif package_installed('PIL'):
    install_requires.append('PIL>=1.1.6,<1.2.99')
else:
    install_requires.append('Pillow !=2.4.0')

version = "0.3"
setup(
        name = "scurve",
        version = version,
        description = "A collection of space-filling curves and related algorithms.",
        author = "Aldo Cortesi",
        author_email = "aldo@corte.si",
        packages = ["scurve"],
        scripts = ["colormap", "cube", "drawcurve", "gray", "testpattern", "binvis"],
        install_requires = install_requires
)
