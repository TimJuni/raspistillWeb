# -*- coding: utf-8 -*- 
<%inherit file="settings-layout.mako"/>

<div class="container">
  % if preferences_success_alert:
    <div class="row">
      <div class="col-md-10 col-md-offset-1">
        <div class="alert alert-success alert-dismissable">
          <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
          <strong>Success!</strong> Settings saved. Please follow <a href="/" class="alert-link">this link</a> to take a photo.
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
      	    <div class="form-group">
              <label for="imageWidth1" class="col-lg-2 control-label">Image Width</label>
              <div class="col-lg-10">
                <input type="number" class="form-control" id="ImageWidth1" name="imageWidth" placeholder="${image_width}">
              </div>
            </div>
            <div class="form-group">
              <label for="imageHeight1" class="col-lg-2 control-label">Image Height</label>
              <div class="col-lg-10">
                <input type="number" class="form-control" id="ImageHeight1" name="imageHeight" placeholder="${image_height}">
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
