# raspistillWeb

Small Python web interface for raspistill to take photos with the RaspberryPi in the browser. I used the [pyramid framework](http://www.pylonsproject.org/) for site generation and [bootstrap](http://getbootstrap.com/) for fancy mobile-first layouts. 

![alt text](https://raw.github.com/TimJuni/raspistillWeb/master/raspistillweb/pictures/preview.jpg "raspistillWeb preview")

## Requirements

For a successful installation you need:
* a RaspberryPi with [raspbian](http://www.raspbian.org) installed (other os not tested, but should work too)
* a RaspberryPi Camera Kit

## Installation Notes

I'll provide a guide to install raspistillWeb based on the tutorial from the [pyramid framework](http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/narr/install.html) to install raspistillWeb in a seperate python environment, so that your systems python environment is not effected.

1. Make sure that your raspbian and you camera is working. Try to make a photo with raspistill to verify that your camera is working. 

2. Install python2.7-dev (if not already on your system), virtualenv and setuptools:
  * `sudo apt-get install python2.7-dev python-virtualenv python-setuptools exif`

3. Create a virtual environment for python (sudo not required and not recommended):
  * `mkdir ~/Development` (Or another directory)
  * `cd ~/Development`
  * `virtualenv --no-site-packages env`
  * `cd env`

4. Install raspistillWeb
  * `git clone https://github.com/TimJuni/raspistillWeb.git`
  * `cd raspistillWeb`
  * `../bin/python setup.py develop`

5. Run raspistillWeb
  * `../bin/pserve development.ini`
  * surf `http://<adress of your pi>:6543`

## Updates
To update your Version of raspistillWeb, simply go into the raspistillWeb Directory and type:
  * `git pull`
  * `../bin/python setup.py develop`

Please notice, that you may need to install new dependencies (for example exif via apt-get)

## Future Work
This is my first project with python and pyramid. Feel free to leave a commend or a feature request.
