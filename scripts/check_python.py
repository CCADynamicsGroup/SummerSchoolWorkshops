from importlib import import_module
from packaging.version import parse

pkg_minversions = {
    'astroquery': '0.4',
    'astropy': '4.2',
    'gala': '1.4',
    'galpy': '1.5',
    'IPython': '7.16',
    'jupyter_client': '6.0',
    'matplotlib': '3.2',
    'numpy': '1.19',
    'pyia': '1.3',
    'scipy': '1.5',
    'sympy': '1.5',
}

update_or_install = []
for pkg_name, min_str in pkg_minversions.items():
    minversion = parse(min_str)
    try:
        pkg = import_module(pkg_name)
        version = pkg.__version__
    except ImportError:
        version = 'not installed'

    if parse(version) >= minversion and version != 'not installed':
        goodbad = '✅'
    else:
        goodbad = '❌'
        update_or_install.append(pkg_name)

    print(f"{goodbad} {pkg_name}: {version!s}")

print("")

if len(update_or_install) > 0:
    print(
        "You are missing some packages, or some require updating. If you use "
        "pip, run this command to update your environment:\n\n\t"
        f"pip install --upgrade {' '.join(update_or_install)}\n\b"
        "\nOr, if you use conda, run this command:\n\n\t"
        f"conda update {' '.join(update_or_install)}\n\b"
    )

else:
    print("Everything looks good -- you're all set up!")
