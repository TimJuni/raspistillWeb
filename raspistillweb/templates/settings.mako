# -*- coding: utf-8 -*- 
<%inherit file="settings-layout.mako"/>

<div class="container">
  % if preferences_success_alert:
    <div class="row">
      <div class="col-md-10 col-md-offset-1">
        <div class="alert alert-success alert-dismissable">
          <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
          <strong>Success!</strong> Settings saved. Please follow <a href="/photo" class="alert-link">this link</a> to take a photo.
        </div>
      </div>
    </div>
  % endif
  % if preferences_fail_alert != []: 
    <div class="row">
      <div class="col-md-10 col-md-offset-1">
        <div class="alert alert-danger alert-dismissable">
          <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
          <strong>Error!</strong> <br>
          <ul>
            % for alert in preferences_fail_alert:
              <li>${alert}</li>  
            % endfor
          </ul>
        </div>
      </div>
    </div>
  % endif
  <div class="row">
    <div class="col-md-10 col-md-offset-1">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">Preferences</h3>
        </div>
        <div class="panel-body">
      	  <form action="save" method="POST" class="form-horizontal" role="form">
            <span class="help-block">Image preferences:</span>            
            <div class="form-group">
              <label for="imageResolution1" class="col-lg-2 control-label">Image Resolution</label>
              <div class="col-sm-3">
                <select name="imageResolution" class="form-control" id="imageResolution1">
                      <option selected>${image_width}x${image_height}</option>
                  % for resolution in image_resolutions:
                    % if resolution != image_width + 'x' + image_height:                               
                      <option>${resolution}</option>
                      % endif
                  % endfor
                </select>
              </div>
              <div class="col-sm-1">
                <label for="imageResolution2" class="control-label">or</label>
              </div>
                            
              
              <div class="col-md-4 col-lg-3 col-sm-4">
                <div class="input-group">
                  <span class="input-group-addon">width</span>
                  <input type="number" class="form-control" name="imageWidth" placeholder="${image_width}">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-sm-4">
                <div class="input-group">
                  <span class="input-group-addon">height</span>
                  <input type="number" class="form-control" name="imageHeight" placeholder="${image_height}">
                </div>                
              </div>
            </div>
            
            
            
            <div class="form-group">
              <label for="isoOption1" class="col-lg-2 control-label">ISO Option</label>
              <div class="col-lg-10">
                <select name="isoOption" class="form-control" id="isoOption1">
                  % for option in iso_options:
                    % if option == image_iso:
                      <option selected>${option}</option>
                    % else:
                      <option>${option}</option>
                    % endif
                  % endfor
                </select>
              </div>
            </div>
            
            
            
            <div class="form-group">
              <label for="exposureMode1" class="col-lg-2 control-label">Exposure Mode</label>
              <div class="col-lg-10">
                <select name="exposureMode" class="form-control" id="exposureMode1">
                  % for mode in exposure_modes:
                    % if mode == exposure_mode:
                      <option selected>${mode}</option>
                    % else:
                      <option>${mode}</option>
                    % endif
                  % endfor
                </select>
              </div>
            </div>
            <div class="form-group">
              <label for="imageEffect1" class="col-lg-2 control-label">Image Effect</label>
              <div class="col-lg-10">
                <select name="imageEffect" class="form-control" id="imageEffect1">             
                  % for effect in image_effects:
                    % if effect == image_effect:
                      <option selected>${effect}</option>
                    % else:
                      <option>${effect}</option>
                    % endif
                  % endfor
                </select>
              </div>  
            </div>
            <div class="form-group">
              <label for="awbMode1" class="col-lg-2 control-label">AWB Mode</label>
              <div class="col-lg-10">
                <select name="awbMode" class="form-control" id="awbMode1">             
                  % for mode in awb_modes:
                    % if mode == awb_mode:
                      <option selected>${mode}</option>
                    % else:
                      <option>${mode}</option>
                    % endif
                  % endfor
                </select>
              </div>  
            </div>
            <div class="form-group">
              <label for="imageRotation1" class="col-lg-2 control-label">Image Rotation</label>
              <div class="col-lg-10">
                <div class="btn-group" data-toggle="buttons">
                  <label class="btn btn-default ${'active' if image_rotation == '0' else ''}">
                    <input type="radio" name="imageRotation" value="0" ${'checked' if image_rotation == '0' else ''}><span class="glyphicon glyphicon-circle-arrow-up"></span> 0°
                   </label>
                  <label class="btn btn-default ${'active' if image_rotation == '90' else ''}">
                    <input type="radio" name="imageRotation" value="90" ${'checked' if image_rotation == '90' else ''}><span class="glyphicon glyphicon-circle-arrow-right"></span> 90°
                  </label>
                  <label class="btn btn-default ${'active' if image_rotation == '180' else ''}">
                    <input type="radio" name="imageRotation" value="180" ${'checked' if image_rotation == '180' else ''}><span class="glyphicon glyphicon-circle-arrow-down"></span> 180°
                  </label>
                  <label class="btn btn-default ${'active' if image_rotation == '270' else ''}">
                    <input type="radio" name="imageRotation" value="270" ${'checked' if image_rotation == '270' else ''}><span class="glyphicon glyphicon-circle-arrow-left"></span> 270°
                  </label>
                </div>
              </div>  
            </div>
            <span class="help-block">Timelapse preferences:</span>
      	    <div class="form-group">
              <label for="TimelapseInterval1" class="col-lg-2 control-label">Timelapse Interval (ms)</label>
              <div class="col-lg-10">
                <input type="number" class="form-control" id="TimelapseInterval1" name="timelapseInterval" placeholder="${timelapse_interval}">
              </div>
            </div>
      	    <div class="form-group">
              <label for="TimelapseTime1" class="col-lg-2 control-label">Timelapse Time (ms)</label>
              <div class="col-lg-10">
                <input type="number" class="form-control" id="TimelapseTime1" name="timelapseTime" placeholder="${timelapse_time}">
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-offset-2 col-lg-10">
                <button type="submit" class="btn btn-primary">Save</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div> 
</div>
