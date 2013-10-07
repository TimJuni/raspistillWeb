# raspistillWeb

Small Python web interface for raspistill to take photos with the RaspberryPi with the browser. We use the [pyramid framework](http://www.pylonsproject.org/) for site generation and [bootstrap](http://getbootstrap.com/) for fancy layouts. 

### Requirements

For a successful installation you need:
* a RaspberryPi with raspbian installed (other os not tested, but should work too)
* a RaspberryPi Camera Kit

### Installation Notes

We use the tutorial from hte [pyramid framework](http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/narr/install.html) to install raspistillWeb in a seperate python environment, so that your systems python environment is not effected.

1. Make sure that your raspbian and you camera is working. Try to make a photo with raspistill to verify that your camera is working. 

2. Install python2.7-dev (if not already on your system), virtualenv and setuptools:
`sudo apt-get install python2.7-dev python-virtualenv python-setuptools`

3. Create a virtual environment for python (sudo not required and not recommended):
`mkdir ~/Development`
`cd ~/Development`
`virtualenv --no-site-packages env`
`cd env`

4. Install raspistillWeb
`git clone https://github.com/TimJuni/raspistillWeb.git`
`cd raspistillWeb`
`../bin/python setup.py develop`

5. Run raspistillWeb
`../bin/pserve development.ini`
surf http://<adress of your pi>:6543




4. 

