try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'A bitmapped game wherein a player attempts to collect all the snowmen sprites and avoid robot sprites.',
    'author':'Zach Trembly',
    'url':'github.com/ZATGit',
    'download_url':'https://github.com/ZATGit/Snowman-Defender-Pygame',
    'author_email':'mail@zachtrembly.com',
    'version':'1.2',
    'license':'MIT',
    'install_requires':['pygame', 'nose'],
    'packages':['snowman_defender_pygame'],
    'scripts':[],
    'name':'Snowman Defender Pygame'
}

setup(**config)