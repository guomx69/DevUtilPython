 1)list the versions of installed python
   ls -1 /usr/bin/python* | grep '.*[2-3]\(.[0-9]\+\)\?$'
   find /usr/bin/python* ! -type l
 2)

 sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.6 4
 sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
 sudo update-alternatives --config python

 alias python3='/usr/bin/python3.9'
 
 whereis python3.9 vs dpkg -S python3.9
         
 apt install python3.9-venv
 python -m venv ./.py3.9.5 --prompt=py3.9.5 #create local version 3.9.5
 . ./.py3.9.5/bin/activate                  #activate local env
 pip3 install -r requirements.txt (pip3 freeze > requirements.txt)


 #build unified dev environment.
    cd pythonDev &&   python3 -V  &&    python3 -m venv .env3.9 --prompt=env3.9
    . ./.env3.9/bin/activate  &&    pip install -r requirements.txt  #pip3 freeze > ./requirements.txt
    #pip3 install termcolor
    