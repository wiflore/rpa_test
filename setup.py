from distutils.core import setup
setup(
  name = 'mypackage',
  packages = ['mypackage'], # this must be the same as the name above
  version = '0.1',
  description = 'A random test lib',
  long_description = long_description,
  author = 'William Florez',
  author_email = 'williamflorezmaestre@gmail.com',
  url = 'https://github.com/wiflore/rpa_test/tree/master/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/wiflore/rpa_test/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'rpa', 'example'], # arbitrary keywords
  install_requires=['PyAutoGUI>=0.9.36', 'pywinauto>=0.6.3']
  classifiers = [],
)
