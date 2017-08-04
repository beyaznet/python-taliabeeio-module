from setuptools import setup

setup(
    name='taliabeeio',
    version='0.1.3',
    packages=['taliabeeio'],
    description='Python TaliaBeeIO module',
    url = 'https://github.com/beyaznet/python-taliabeeio-module',
    author = 'Beyaz R&D Team',
    author_email = 'arge@beyaz.net',
    license='MIT',
    keywords = 'raspberry pi medioex taliabee',
    install_requires=['requests'],
    python_requires='>=3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
