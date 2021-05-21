from setuptools import setup


setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='folderexplore',
    url='https://github.com/Suriyakumarjs/folderexplore',
    author='Suriya Kumar J S',
    author_email='suriyakumarjs97@gmail.com',
    # Needed to actually package something
    packages=['folderexplore'],
    # Needed for dependencies
    install_requires=['os','shutil'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A python package to organize your folder',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
