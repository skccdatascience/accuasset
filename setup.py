import setuptools
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.install import install
import warnings

try:
    from accuasset import __prop__
    prop = __prop__.__dict__
except ImportError:
    prop = dict()
    exec(open("accuasset/__prop__.py").read(), prop)

with open("README.md", "r") as fh:
    long_description = fh.read()



class move_ttf(install):
    def run(self):
        """
        Performs the usual install process and then copies the True Type fonts
        that come with clearplot into matplotlib's True Type font directory,
        and deletes the matplotlib fontList.cache
        """
        #Perform the usual install process
        install.run(self)
        #Try to install custom fonts
        try:
            import os, shutil
            import matplotlib as mpl
            import clearplot as cp

            #Find where matplotlib stores its True Type fonts
            mpl_data_dir = os.path.dirname(mpl.matplotlib_fname())
            mpl_ttf_dir = os.path.join(mpl_data_dir, 'fonts', 'ttf')

            #Copy the font files to matplotlib's True Type font directory
            #(I originally tried to move the font files instead of copy them,
            #but it did not seem to work, so I gave up.)
            cp_ttf_dir = os.path.join(os.path.dirname(cp.__file__), 'true_type_fonts')
            for file_name in os.listdir(cp_ttf_dir):
                if file_name[-4:] == '.ttf':
                    old_path = os.path.join(cp_ttf_dir, file_name)
                    new_path = os.path.join(mpl_ttf_dir, file_name)
                    shutil.copyfile(old_path, new_path)
                    print ("Copying " + old_path + " -> " + new_path)

            #Try to delete matplotlib's fontList cache
            mpl_cache_dir = mpl.get_cachedir()
            mpl_cache_dir_ls = os.listdir(mpl_cache_dir)
            if 'fontList.cache' in mpl_cache_dir_ls:
                fontList_path = os.path.join(mpl_cache_dir, 'fontList.cache')
                os.remove(fontList_path)
                print ("Deleted the matplotlib fontList.cache")
        except:
            warnings.warn("WARNING: An issue occured while installing the custom fonts for clearplot.")



setuptools.setup(
    name="accuasset",
    version=prop['__version__'],
    author="hyeonsangjeon",
    author_email="wingnut0310@gmail.com",
    description=prop['__desc__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=prop['__url__'],
    packages=find_packages(),
    install_requires=Path("requirements.txt").read_text().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License"
    ],
    #package_data = {'' : ['color_maps/*.csv', 'font/*.ttf']},
    package_data = {'' : ['accuasset/font/*.ttf']},
    #Specify the custom install class
    cmdclass={'install' : move_ttf}
)
