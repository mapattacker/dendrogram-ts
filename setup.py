from distutils.core import setup
setup(
  name = 'dendrogram_ts',         # How you named your package folder (MyLib)
  packages = ['YOURPACKAGENAME'],   # Chose the same as "name"
  version = '0.1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Plotting time-series graphs in scipy''s dendrogram',   # Give a short description about your library
  author = 'Jake Teo',                   # Type in your name
  author_email = 'mapattacker@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/mapattacker/dendrogram-ts',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['dendrogram', 'agglomerative clustering', 'timeseries'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
            'pandas==1.2.3'
            'numpy==1.20.2',
            'matplotlib==3.4.1',
            'scipy==1.6.2',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',    # Specify which python versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)