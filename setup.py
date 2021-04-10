from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
  name = 'dendrogram_ts',
  packages = ['dendrogram_ts'],
  version = '0.1.0-beta.7',
  license='MIT',
  description = "Plotting time-series graphs in scipy's dendrogram",
  long_description = readme,
  author = 'Jake Teo',
  author_email = 'mapattacker@gmail.com',
  url = 'https://github.com/mapattacker/dendrogram-ts',
  download_url = 'https://github.com/mapattacker/dendrogram-ts/archive/refs/tags/v0.1.0-beta.7.tar.gz',
  keywords = ['dendrogram', 'agglomerative clustering', 'timeseries'],
  install_requires=[
            'pandas==1.2.*',
            'numpy==1.20.*',
            'matplotlib==3.4.*',
            'scipy==1.6.*',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)