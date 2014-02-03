# -*- coding: utf-8 -*- 
<%inherit file="timelapse-layout.mako"/>

<div class="container">
  <div class="row">
    % if timelapse:
      <div class="col-md-12">
        <div class="alert alert-danger alert-dismissable">
          <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
          <strong>Timelapse in Progress.</strong> Please wait until the timelapse process has finished.          
        </div>
      </div>
    % else:
    <div class="col-md-12">
      <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">Timelapse</h3>
          </div>
          <div class="panel-body">
            There is currently no timelapse in progress. You can start a timelapse with the folowing preferences or edit these settings on the <a href="/settings"><strong>settings page.</strong></a>
            <dl>
              <dt>Interval</dt>
              <dd>${timelapseInterval}ms</dd>
              <dt>Time</dt>
              <dd>${timelapseTime}ms</dd>
            </dl>
            <form method="post">
              <input type="button" class="btn btn-danger btn-lg" value="Start Timelapse" onclick="location.href='/timelapse_start'">
            </form>
          </div>
      </div>
    </div>
    % endif    
  </div>
  <div class="row">
  % for file in timelapseDatabase:     
    <div class="col-xs-6 col-sm-4 col-md-3">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">${file['timeStart']}</h3>
        </div>
        <div class="panel-body">
          <dl>
            <dt>Image Effect</dt>
            <dd>${file['image_effect']}</dd>
            <dt>Exposure Mode</dt>
            <dd>${file['exposure_mode']}</dd>
            <dt>AWB Mode</dt>
            <dd>${file['awb_mode']}</dd>
            <dt>Start</dt>
            <dd>${file['timeStart']}</dd>
            <dt>End</dt>
            <dd>${file['timeEnd']}</dd>
          </dl>
          <a href="${request.static_url('raspistillweb:time-lapse/')}${file['filename']}.tar.gz"><button type="button" class="btn btn-success btn-sm btn-block">Download</button></a>
        </div>
      </div>     
    </div>   
  % endfor  
  </div>  
</div>
  	

