# raspistillWeb

Small Python web interface for raspistill to take photos with the RaspberryPi in the browser. I used the [pyramid framework](http://www.pylonsproject.org/) for site generation and [bootstrap](http://getbootstrap.com/) for fancy mobile-first layouts. 

![alt text](https://raw.github.com/TimJuni/raspistillWeb/master/raspistillweb/pictures/preview.jpg "raspistillWeb preview")

## Requirements

For a successful installation you need:
* a RaspberryPi with [raspbian](http://www.raspbian.org) installed (other os not tested, but should work too)
* a RaspberryPi Camera Kit

## Installation Notes

I'll provide a guide to install raspistillWeb based on the tutorial from the [pyramid framework](http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/narr/install.html) to install raspistillWeb in a seperate python environment, so that your systems python environment is not effected.

1. Make sure that your raspbian and your camera is working. Try to make a photo with raspistill to verify that your camera is working. 

2. Install python2.7-dev (if not already on your system), virtualenv, setuptools and exif:
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

## Example Configurations

### Running raspistillWeb over ssh
If you run raspistillWeb over ssh, you cannot quit your ssh session, because the raspistillWeb process will be killed. One easy way to start raspistillWeb (and let it run even when you are logged off) is to use `screen`:

1. Install screen
  * `sudo apt-get install screen`

2. Create a new screen
  * `screen -S cam`

3. Start raspistillWeb
  * `../bin/pserve development.ini`

4. Detatch the screen
  * simply hit ctrl + a + d 

At this point you can quit your ssh session and raspistillWeb will continue serving files. If you later want stop raspistillWeb, you can attach to the screen by: `screen -r cam`

### Running raspistillWeb behind a Reverse Proxy (with Authentification)
TODO

### Run raspistillWeb on startup
TODO

## Future Work
This is my first project with python and pyramid. Feel free to leave a commend or a feature request.
