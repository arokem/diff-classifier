from setuptools import setup, find_packages
import os

ver_file = os.path.join('diff_classifier', 'version.py')
with open(ver_file) as f:
    exec(f.read())

PACKAGES = find_packages()

opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            packages=PACKAGES,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            install_requires=REQUIRES,
            requires=REQUIRES,
            package_data=PACKAGE_DATA)


if __name__ == '__main__':
    setup(**opts)
