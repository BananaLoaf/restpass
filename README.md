# restpass
Terminal based graphical utility for generating restorable passwords

![UI](misc/ui.png?raw=true)
```bash
pip install restpass
or
pip install git+https://github.com/BananaLoaf/restpass
```
### Usage
The core principle is simple - **for the same input you get the same output**. 
The input consist of input string, salt, length and used alphabet (either constructed from rules or custom).
Output is the generated password. In case of forgetting the password, you can always come back and restore it (if you remember the input, of course).
##### Recommendations
1. Use memorable phrases (favorite quotes, song lyrics, etc) for input string and salt (not required by default).
2. Salt is used in cases when you want to reuse input string, but have different password. For example, you can use the same input string for your desktop and laptop, but different salt.
3. Minimum recommended length is 15. According to [howsecureismypassword.net](howsecureismypassword.net), it would take a computer about **558 QUADRILLION YEARS** to crack your password.
4. Using symbols or custom alphabet is the last thing to consider.