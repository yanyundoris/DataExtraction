from setuptools import setup

# setup(
#     name='DataExtraction',   # This is the name of your PyPI-package.\
#      version='0.1',                          # Update the version number for new releases
#      scripts=['DataExtractionTool']                  # The name of your scipt, and also the command you'll be using for calling it
#  )

import codecs
import os
import sys

#sys.path.append('/Users/yanyunliu/PycharmProjects/CourseraCrawl/DiscussionForumJava/DataExtraction')

try:
    from setuptools import setup
except:
    from distutils.core import setup



def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = 'DataExtraction'

#DataExtractionTool", ]

DESCRIPTION = "this is a test package."


LONG_DESCRIPTION = read("README.rst")

KEYWORDS = "test python package"

AUTHOR = "YanyunDoris"

AUTHOR_EMAIL = "dorisliu9318@gmail.com"

#
URL = "https://github.com/yanyundoris/eLearning_yyliu/"


VERSION = "1.0.3"


LICENSE = "MIT"


setup(
    name=NAME,
    scripts=['DataExtractionTool'],
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url= URL,
    #packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
