import setuptools

setuptools.setup(
     name='ecpb',  
     version='1.2',
     author="Hugo Neves de Carvalho",
     author_email="hugonvsc@gmail.com",
     description="Upload code and get into your clipboard",
     url="https://github.com/hugonxc/ecpb",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    packages=['ecpb'],
    install_requires=["clipboard", "requests"],
 )