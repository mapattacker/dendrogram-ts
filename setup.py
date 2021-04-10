try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from dendrogram_ts import __version__


with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
  name = 'dendrogram_ts',
  packages = ['dendrogram_ts'],
  version = __version__,
  license = 'MIT',
  description = "Plotting time-series graphs in scipy's dendrogram",
  long_description = readme,
  long_description_content_type = 'text/x-rst',
  author = 'Jake Teo',
  author_email = 'mapattacker@gmail.com',
  url = 'https://github.com/mapattacker/dendrogram-ts',
  download_url = 'https://github.com/mapattacker/dendrogram-ts/archive/refs/tags/v' + __version__ + '.tar.gz',
  keywords = ['dendrogram', 'agglomerative clustering', 'timeseries'],
  install_requires=[
            'pandas',
            'numpy',
            'matplotlib',
            'scipy',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)