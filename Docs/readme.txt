#######GIT###############
--------add a local git repository to github-------------
git init -b main #above 2.28
git init && git symbolic-ref HEAD refs/heads/main #git version below 2.28
git add . && git commit -m "boilderplate for python"
------create a new repository on the command line-------
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/guomx69/pythonDev.git
git push -u origin main

-------push an existing repository from the command line
git remote add origin https://github.com/guomx69/pythonDev.git
git branch -M main
git push -u origin main


###########Python########################
-------------check python###list the versions of installed python---------
   ls -1 /usr/bin/python* | grep '.*[2-3]\(.[0-9]\+\)\?$'
   find /usr/bin/python* ! -type l
----------------install python-------------------
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.11

     whereis python3.11 vs dpkg -S python3.11

----------------two ways to switch the python version----------------
    1)
    sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.6 4
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
    sudo update-alternatives --config python
    
    2)
    alias python3='/usr/bin/python3.11' VS echo "alias python3='/usr/bin/python3.11'" >> .bashrc

---------install the following additional extras-------------------------
  "python3.11-venv" to localize the  app dev environment

  one by one installation extras :
         sudo apt install python3.11-venv &&  sudo apt install python3.11-dev && sudo apt install python3.11-dbg .... more
  one step installation extras :
         sudo apt install python3.11-full

------------Install PIP with Python ----------------
  sudo apt install python3-pip

  pip --version  &&   pip3 --version
  https://www.linuxcapable.com/how-to-install-python-3-11-on-ubuntu-linux/


###########check repository##############
 apt-cache policy   ppa:deadsnakes/ppa
 apt-cache search distutils

    