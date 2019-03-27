import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='loginpkg',  
     version='0.1',
     scripts=['loginpkg'] ,
     author="jondhc",
     author_email="jonathandaniel.heca@gmail.com",
     description="A login system for the web",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/jondhc/RSLoginSystem",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "Operating System :: OS Independent",
     ],
 )
