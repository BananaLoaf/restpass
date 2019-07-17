# restpass
Terminal based graphical utility for generating restorable passwords

[![Python Version](https://img.shields.io/pypi/pyversions/restpass.svg?color=yellow&style=flat-square)](https://www.python.org/downloads/)
[![GitHub Licence](https://img.shields.io/github/license/BananaLoaf/restpass.svg?color=blue&style=flat-square)](https://github.com/BananaLoaf/restpass/blob/master/LICENSE)
[![Package Version](https://img.shields.io/pypi/v/restpass.svg?color=green&style=flat-square)](https://pypi.org/project/restpass/)

![Demo](misc/demo.gif)
### Install
```bash
pip install restpass
```
### Usage
The core principle is simple - **for the same input you get the same output**. 
The input consist of input string, salt, length and alphabet.
Output is the generated password. In case of forgetting the password, it can always be restored (with the same input).
##### Recommendations
1. Use memorable phrases (favorite quotes, song lyrics, etc) for input string and salt (not required by default).
2. Use digits, lowercase and uppercase. Using symbols is the last thing to consider.
3. Salt is used in cases when you want to reuse input string, but have different password. For example, the same input string could be used for desktop and laptop, but used with different salt.
4. Minimum recommended length is 15. According to [howsecureismypassword.net](howsecureismypassword.net), it would take a computer about **558 QUADRILLION YEARS** to crack your password.
