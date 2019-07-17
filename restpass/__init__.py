PAYLOAD = {
    "name": "restpass",
    "version": "1.1.3",
    "install_requires": ["seedrandom==1.4.1", "npyscreen", "pyperclip"],
    "packages": ("restpass", ),
    "entry_points": {
        "console_scripts": [
            "restpass = restpass.main:main"
        ]
    },

    # Metadata for PyPi
    "author": "BananaLoaf",
    "author_email": "bananaloaf@protonmail.com",
    "maintainer": "BananaLoaf",
    "maintainer_email": "bananaloaf@protonmail.com",
    "license": "MIT",

    "description": None,
    "long_description": None,
    "long_description_content_type": "text/markdown",
    "keywords": ["generator", "password", "passphrase", "hash", "restore"],
    "data_files": [
        ("share/applications", ["misc/restpass.desktop", ])
    ],

    "url": "https://github.com/BananaLoaf/restpass",
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Security",
        "Topic :: Utilities"
    ]
}
