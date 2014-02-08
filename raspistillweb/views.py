# raspistillWeb - web interface for raspistill
# Copyright (C) 2013 Tim Jungnickel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
import exifread
import os
import thread
import tarfile
from subprocess import call
from time import gmtime, strftime, localtime, asctime, mktime
from stat import *
from datetime import *


# Modify these lines to change the directory where the pictures and thumbnails
# are stored. Make sure that the directories exist and the user who runs this
# program has write access to the directories. 
RASPISTILL_DIRECTORY = 'raspistillweb/pictures/' # Example: /home/pi/pics/
THUMBNAIL_DIRECTORY = 'raspistillweb/thumbnails/' # Example: /home/pi/thumbs/
TIMELAPSE_DIRECTORY = 'raspistillweb/time-lapse/'

IMAGE_EFFECTS = [
    'none', 'negative', 'solarise', 'sketch', 'denoise', 'emboss', 'oilpaint', 
    'hatch', 'gpen', 'pastel', 'watercolour', 'film', 'blur', 'saturation', 
    'colourswap', 'washedout', 'posterise', 'colourpoint', 'colourbalance', 
    'cartoon'
    ]

EXPOSURE_MODES = [
    'auto', 'night', 'nightpreview', 'backlight', 'spotlight', 'sports',
    'snow', 'beach', 'verylong', 'fixedfps', 'antishake', 'fireworks'
    ]
    
AWB_MODES = [
    'off', 'auto', 'sun', 'cloud', 'shade', 'tungsten', 'fluorescent',
    'incandescent', 'flash', 'horizon'
    ]

ISO_OPTIONS = [
    'auto', '100', '150', '200', '250', '300', '400', '500', 
    '600', '700', '800'
    ]
    
IMAGE_HEIGHT_ALERT = 'Please enter an image height between 0 and 1945.'
IMAGE_WIDTH_ALERT = 'Please enter an image width between 0 and 2593.'
IMAGE_EFFECT_ALERT = 'Please enter a valid image effect.'
EXPOSURE_MODE_ALERT = 'Please enter a valid exposure mode.'
AWB_MODE_ALERT = 'Please enter a valid awb mode.'
ISO_OPTION_ALERT = 'Please enter a valid ISO option.'
IMAGE_ROTATION_ALERT = 'Please enter a valid image rotation option.'

THUMBNAIL_SIZE = '240:160:80'

database = []
timelapse_database = []

timelapse = False

preferences_fail_alert = []
preferences_success_alert = False

# image parameter commands
image_width = 800
image_height = 600
image_effect = 'none'
exposure_mode = 'auto'
awb_mode = 'off'
timelapse_interval = 4000
timelapse_time = 20000
image_ISO = 'auto'
image_rotation = '0'

# not implemented yet
image_quality = '100'
image_sharpness = '0'
image_contrast = '0'
image_brightness = '50'
image_saturation = '0'


###############################################################################
################################### Views #####################################
###############################################################################


# View for the /settings site
@view_config(route_name='settings', renderer='settings.mako')
def settings_view(request):
    global preferences_fail_alert, preferences_success_alert
        
    preferences_fail_alert_temp = []    
    if preferences_fail_alert is not []:
        preferences_fail_alert_temp = preferences_fail_alert
        preferences_fail_alert = []
     
    preferences_success_alert_temp = False  
    if preferences_success_alert:
        preferences_success_alert_temp = True
        preferences_success_alert = False
        
    return {'project' : 'raspistillWeb',
            'image_effect' : image_effect,
            'exposure_mode' : exposure_mode,
            'awb_mode' : awb_mode,
            'image_effects' : IMAGE_EFFECTS,
            'exposure_modes' : EXPOSURE_MODES,
            'awb_modes' : AWB_MODES,
            'image_width' : image_width,
            'image_height' : image_height,
            'image_iso' : image_ISO,
            'iso_options' :  ISO_OPTIONS, 
            'timelapse_interval' : timelapse_interval,
            'timelapse_time' : timelapse_time,
            'preferences_fail_alert' : preferences_fail_alert_temp,
            'preferences_success_alert' : preferences_success_alert_temp,
            'image_rotation' : image_rotation
            } 
            
# View for the /archive site
@view_config(route_name='archive', renderer='archive.mako')
def archive_view(request):
    return {'project' : 'raspistillWeb',
            'database' : database
            }
                    
# View for the / site
@view_config(route_name='home', renderer='home.mako')
def home_view(request):
    if database == []:
        return HTTPFound(location='/photo')
    elif timelapse:
        return {'project': 'raspistillWeb',
                'imagedata' : database[0],
                'timelapse' : timelapse,
                }
    elif (mktime(localtime()) - mktime(database[0]['timestamp'])) > 1800: 
        return HTTPFound(location='/photo') 
    else:
        return {'project': 'raspistillWeb',
                'imagedata' : database[0],
                'timelapse' : timelapse,
                }

# View for the /timelapse site        
@view_config(route_name='timelapse', renderer='timelapse.mako')
def timelapse_view(request):
    return {'project': 'raspistillWeb',
            'timelapse' : timelapse,
            'timelapseInterval' : timelapse_interval,
            'timelapseTime' : timelapse_time,
            'timelapseDatabase' : timelapse_database
            }
            
# View for the timelapse start - no site will be generated
@view_config(route_name='timelapse_start')
def timelapse_start_view(request):
    global timelapse
    timelapse = True
    filename = strftime("%Y-%m-%d.%H.%M.%S", localtime())
    thread.start_new_thread( take_timelapse, (filename, ) )
    return HTTPFound(location='/timelapse') 


# View to take a photo - no site will be generated
@view_config(route_name='photo')
def photo_view(request):
    global database
    if timelapse:
        return HTTPFound(location='/') 
    else:
        filename = strftime("%Y-%m-%d.%H.%M.%S.jpg", localtime())
        take_photo(filename)
        f = open(RASPISTILL_DIRECTORY + filename,'rb')
        exif = extract_exif(exifread.process_file(f))    
        filedata = extract_filedata(os.stat(RASPISTILL_DIRECTORY + filename))  
        imagedata = dict(filedata.items() + exif.items())
        imagedata['filename'] = filename
        imagedata['image_effect'] = image_effect
        imagedata['exposure_mode'] = exposure_mode
        imagedata['awb_mode'] = awb_mode
        database.insert(0,imagedata)
        return HTTPFound(location='/')  
         
# View for the archive delete - no site will be generated
@view_config(route_name='delete')
def delete_view(request):
    global database
    database.pop(int(request.params['id']))
    return HTTPFound(location='/archive') 

# View for settings form data - no site will be generated      
@view_config(route_name='save')
def save_view(request):
    global exposure_mode, image_effect, image_width, preferences_success_alert
    global image_height, preferences_fail_alert, awb_mode, timelapse_interval
    global timelapse_time, image_ISO, image_rotation

    image_width_temp = request.params['imageWidth']
    image_height_temp = request.params['imageHeight']
    timelapse_interval_temp = request.params['timelapseInterval']
    timelapse_time_temp = request.params['timelapseTime']
    exposure_mode_temp = request.params['exposureMode']
    image_effect_temp = request.params['imageEffect']
    awb_mode_temp = request.params['awbMode']
    image_ISO_temp = request.params['isoOption']
    image_rotation_temp = request.params['imageRotation']
    
    if image_width_temp:
        if 0 < int(image_width_temp) < 2593:
            image_width = image_width_temp
        else:
            preferences_fail_alert.append(IMAGE_WIDTH_ALERT)
    
    if image_height_temp:
        if 0 < int(image_height_temp) < 1945:
            image_height = image_height_temp
        else:
            preferences_fail_alert.append(IMAGE_HEIGHT_ALERT)
            
    if timelapse_interval_temp:
        timelapse_interval = timelapse_interval_temp
        
    if timelapse_time_temp:
        timelapse_time = timelapse_time_temp
    
    if exposure_mode_temp and exposure_mode_temp in EXPOSURE_MODES:
        exposure_mode = exposure_mode_temp
    else:
        preferences_fail_alert.append(EXPOSURE_MODE_ALERT)
        
    if image_effect_temp and image_effect_temp in IMAGE_EFFECTS:
        image_effect = image_effect_temp
    else:
        preferences_fail_alert.append(IMAGE_EFFECT_ALERT)
        
    if awb_mode_temp and awb_mode_temp in AWB_MODES:
        awb_mode = awb_mode_temp
    else:
        preferences_fail_alert.append(AWB_MODE_ALERT)
        
    if image_ISO_temp and image_ISO_temp in ISO_OPTIONS:
        image_ISO = image_ISO_temp
    else:
        preferences_fail_alert.append(ISO_OPTION_ALERT)
        
    if image_rotation_temp and image_rotation_temp in ['0','90','180','270']:
        image_rotation = image_rotation_temp
    else:
        preferences_fail_alert.append(IMAGE_ROTATION_ALERT)  
        
    if preferences_fail_alert == []:
        preferences_success_alert = True 
            
    return HTTPFound(location='/settings')  

###############################################################################
############ Helper functions to keep the code clean ##########################
###############################################################################

def take_photo(filename):
    if image_ISO == 'auto':
        iso_call = ''
    else:
        iso_call = ' -ISO ' + str(image_ISO)
    call (
        ['raspistill -t 500'
        + ' -w ' + str(image_width)
        + ' -h ' + str(image_height)
        + ' -ex ' + exposure_mode
        + ' -awb ' + awb_mode
        + ' -rot ' + str(image_rotation)
        + ' -ifx ' + image_effect
        + iso_call
        + ' -th ' + THUMBNAIL_SIZE 
        + ' -o ' + RASPISTILL_DIRECTORY + filename], shell=True
        )
    if not (RASPISTILL_DIRECTORY == 'raspistillweb/pictures/'):
        call (
            ['ln -s ' + RASPISTILL_DIRECTORY + filename
            + ' raspistillweb/pictures/' + filename], shell=True
            )
    generate_thumbnail(filename)
    return
    
def take_timelapse(filename):
    global timelapse, timelapse_database
    timelapsedata = {'filename' :  filename}
    timelapsedata['timeStart'] = str(asctime(localtime()))
    os.makedirs(TIMELAPSE_DIRECTORY + filename)
    call (
        ['raspistill'
        + ' -w ' + str(image_width)
        + ' -h ' + str(image_height)
        + ' -ex ' + exposure_mode
        + ' -awb ' + awb_mode
        + ' -ifx ' + image_effect
        + ' -th ' + THUMBNAIL_SIZE
        + ' -tl ' + str(timelapse_interval)
        + ' -t ' + str(timelapse_time) 
        + ' -o ' + TIMELAPSE_DIRECTORY + filename + '/'
        + filename + '_%04d.jpg'], shell=True
        )    
    timelapsedata['image_effect'] = image_effect
    timelapsedata['exposure_mode'] = exposure_mode
    timelapsedata['awb_mode'] = awb_mode
    timelapsedata['timeEnd'] = str(asctime(localtime()))
    with tarfile.open(TIMELAPSE_DIRECTORY + filename + '.tar.gz', "w:gz") as tar:
        tar.add(TIMELAPSE_DIRECTORY + filename, arcname=os.path.basename(TIMELAPSE_DIRECTORY + filename))
    timelapse_database.insert(0,timelapsedata)
    timelapse = False
    
    return

def generate_thumbnail(filename):
    call (
        ['exif -e ' + RASPISTILL_DIRECTORY + filename
        + ' -o ' + THUMBNAIL_DIRECTORY + filename], shell=True
    )
    if not (THUMBNAIL_DIRECTORY == 'raspistillweb/thumbnails/'):
        call (
            ['ln -s ' + THUMBNAIL_DIRECTORY + filename 
            + ' raspistillweb/thumbnails/' + filename], shell=True
            )
    return

def extract_exif(tags):
    return {
        'resolution' : str(tags['Image ImageWidth']) 
        + ' x ' + str(tags['Image ImageLength']),
        'ISO' : str(tags['EXIF ISOSpeedRatings']),
        'exposure_time' : str(tags['EXIF ExposureTime'])
            }
        
    
def extract_filedata(st):
    return {
        'date' : str(asctime(localtime(st[ST_MTIME]))),
        'timestamp' : localtime(),
        'filesize': str((st[ST_SIZE])/1000) + ' kB'
            }
            

