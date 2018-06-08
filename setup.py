import codecs
import os
import re
from setuptools import find_packages, setup


class SetupError(RuntimeError):
    pass


###############################################################################

NAME = 'argmanager'
META_PATH = os.path.join('src', 'argmanager', '__init__.py')
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

###############################################################################

HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """
    Builds an absolute path from *parts* and returns the
    contents of resulting file. Assumes UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf8') as f:
        return f.read()

META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
            r'''__{}__ = ['"](.*?)['"]'''.format(meta),
            META_FILE,
            re.M)
    if meta_match:
        return meta_match.group(1)
    raise SetupError('Unable to find __{}__ string.'.format(meta))


def find_version(path):
    from re import match
    with open(path) as f:
        for line in f:
            match_object = match(
                    '''__version__ = ['"](.*?)['"]''',
                    line)
            if match_object:
                return match_object.group(1)

args = {'name': NAME,
        'classifiers': CLASSIFIERS,
        'package_dir': {'': 'src'},
        'packages': find_packages(where='src'),
        'python_requires': '>=3',
        'long_description': read('README.rst')
        }
for meta in 'version url description license author email'.split():
    args[meta] = find_meta(meta)

setup(**args)
