# Heimdal-CTF
An extensible platform for collaborative CTF challenges of all sorts - although best suited for cybersecurity training.

# Installation
> These instructions are written for Linux, and will work with most distributions, although the installation process may vary between systems
1. Ensure `python 3` is installed
2. Clone Heimdal using git: `git clone https://github.com/dellitsni/Heimdal-CTF`
3. Install virtualenv using your package manager:
  - Arch (from AUR): `yay -S python-virtualenv`
  - Debian, Ubuntu, Mint and others: `apt-get install virtualenv`
  - For other distros, the truth is out there
4. Create a new virtual environment, preferably in the project folder: `virtualenv venv -p python3`
5. Active virtualenv: `source venv/bin/activate`, and install dependencies: `pip install -r requirements.txt`
6. Initialize database: `flask db init`
7. Apply migrations and initialize database file: `flask db upgrade`
8. **Start the development server: `flask run`**
# Contributing
If you've made changes to Heimdal that you'd like to have merged, feel free to open a new pull request!
If you're looking for somewhere to start, check out the issues.
If you're holding on to a good idea, but don't have the time or skill required to give it life, open up a new issue and we'll get to it.
# Resources
If you're looking to learn flask, [Miguel's flask tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) is the way to go.
