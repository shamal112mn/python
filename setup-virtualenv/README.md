```
On Ubuntu -  How to Setup virtual environment

# install virtual environment:  
sudo apt-get update && sudo apt-get install python3-virtualenv

# create
virtualenv myproject

# activate environment
source myproject/bin/activate

# deactivate env
deactivate

# remove myproject
rm -rf myproject

# specific py version 
virtualenv  -p /usr/bin/python2.6  proj1_py26   
  
# put in file requirements
pip freeze --local > requirements.txt   

# install requirement packages from file 
pip install –r requirements.txt 


which python 
which pip
pip list 
pip install numpy 

```