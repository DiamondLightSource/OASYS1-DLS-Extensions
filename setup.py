#
# Memorandum:
#
# Install from sources:
#     git clone https://github.com/.../OASYS1-DLS-Extensions
#     cd OASYS1-DLS-Extensions
#     python -m pip install -e . --no-deps --no-binary :all:
#
# Upload to pypi (when uploading, increment the version number):
#     python setup.py register (only once, not longer needed)
#     python setup.py sdist
#     python -m twine upload dist/...
#
# Install from pypi:
#     pip install OASYS1-DLS-Extensions
#

import os

try:
    from setuptools import find_packages, setup
except AttributeError:
    from setuptools import find_packages, setup

NAME = 'OASYS1-DLS-Extensions'
VERSION = '0.0.01'
ISRELEASED = True

DESCRIPTION = 'OASYS extension for the DLS'
README_FILE = os.path.join(os.path.dirname(__file__), 'README.md')
LONG_DESCRIPTION = open(README_FILE).read()
AUTHOR = 'AW, ...,  and Manuel Sanchez del Rio'
AUTHOR_EMAIL = 'andrew.walters@diamond.ac.uk'
URL = 'https://github.com/DiamondLightSource/OASYS1-DLS-Extensions'
DOWNLOAD_URL = 'https://github.com/DiamondLightSource/OASYS1-DLS-Extensions'
LICENSE = 'GPLv3'

KEYWORDS = (
    'raytracing',
    'simulator',
    'oasys1',
)

CLASSIFIERS = (
    'Development Status :: 4 - Beta',
    'Environment :: X11 Applications :: Qt',
    'Environment :: Console',
    'Environment :: Plugins',
    'Programming Language :: Python :: 3',
    'Intended Audience :: Science/Research',
)

SETUP_REQUIRES = (
    'setuptools',
)

INSTALL_REQUIRES = (
    'setuptools',
)

PACKAGES = find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests'))

PACKAGE_DATA = {
    "orangecontrib.dls.oasys.widgets.extension":["icons/*.png", "icons/*.jpg"],
    "orangecontrib.dls.wofry.widgets.extension":["icons/*.png", "icons/*.jpg"],
    "orangecontrib.dls.xoppy.widgets.extension": ["icons/*.png", "icons/*.jpg"],
    "orangecontrib.dls.syned.widgets.extension":["icons/*.png", "icons/*.jpg"],
    "orangecontrib.dls.shadow.widgets.extension":["icons/*.png", "icons/*.jpg", "miscellanea/*.txt"],
    "orangecontrib.dls.srw.widgets.extension":["icons/*.png", "icons/*.jpg"],
}

NAMESPACE_PACAKGES = ["orangecontrib",
                      "orangecontrib.dls",
                      "orangecontrib.dls.oasys",
                      "orangecontrib.dls.wofry",
                      "orangecontrib.dls.xoppy",
                      "orangecontrib.dls.syned",
                      "orangecontrib.dls.shadow",
                      "orangecontrib.dls.srw",
                      "orangecontrib.dls.oasys.widgets",
                      "orangecontrib.dls.wofry.widgets",
                      "orangecontrib.dls.xoppy.widgets",
                      "orangecontrib.dls.syned.widgets",
                      "orangecontrib.dls.shadow.widgets",
                      "orangecontrib.dls.srw.widgets",
                      ]

ENTRY_POINTS = {
    'oasys.addons' : ("Oasys DLS Extension = orangecontrib.dls.oasys",
                      "Wofry DLS Extension = orangecontrib.dls.wofry",
                      "XOPPY DLS Extension = orangecontrib.dls.xoppy",
                      "Syned DLS Extension = orangecontrib.dls.syned",
                      "Shadow DLS Extension = orangecontrib.dls.shadow",
                      "SRW DLS Extension = orangecontrib.dls.srw",
                      ),
    'oasys.widgets' : (
        "Oasys DLS Extension = orangecontrib.dls.oasys.widgets.extension",
        "Wofry DLS Extension = orangecontrib.dls.wofry.widgets.extension",
        "XOPPY DLS Extension = orangecontrib.dls.xoppy.widgets.extension",
        "Syned DLS Extension = orangecontrib.dls.syned.widgets.extension",
        "Shadow DLS Extension = orangecontrib.dls.shadow.widgets.extension",
        "SRW DLS Extension = orangecontrib.dls.srw.widgets.extension",
    ),
    'oasys.menus' : ("dlsoasysmenu = orangecontrib.dls.menu",)
}

if __name__ == '__main__':
    try:
        import PyMca5, PyQt4

        raise NotImplementedError("This version of DLS Oasys Extensions doesn't work with Oasys1 beta.\nPlease install OASYS1 final release: http://www.elettra.eu/oasys.html")
    except:
        setup(
              name = NAME,
              version = VERSION,
              description = DESCRIPTION,
              long_description = LONG_DESCRIPTION,
              author = AUTHOR,
              author_email = AUTHOR_EMAIL,
              url = URL,
              download_url = DOWNLOAD_URL,
              license = LICENSE,
              keywords = KEYWORDS,
              classifiers = CLASSIFIERS,
              packages = PACKAGES,
              package_data = PACKAGE_DATA,
              #          py_modules = PY_MODULES,
              setup_requires = SETUP_REQUIRES,
              install_requires = INSTALL_REQUIRES,
              #extras_require = EXTRAS_REQUIRE,
              #dependency_links = DEPENDENCY_LINKS,
              entry_points = ENTRY_POINTS,
              namespace_packages=NAMESPACE_PACAKGES,
              include_package_data = True,
              zip_safe = False,
              )
