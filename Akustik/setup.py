try:
    from setuptools import setup
except ImportError:
    from distutil.core import setup

config = {
    'description' : 'Calculate and simulate speakers',
    'author' : 'Joakim Alexander Svensson',
    'url' : 'URL to get it at',
    'download_url' : 'Where to download it',
    'author_email' : 'joaksv87@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['Akustik'],
    'scripts' : [],
    'name' : 'Akustik'
}

setup(**config)
