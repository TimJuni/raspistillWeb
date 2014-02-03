# -*- coding: utf-8 -*- 
<%inherit file="home-layout.mako"/>

<div class="container">
  % if timelapse:
    <div class="row">
      <div class="col-md-12">
        <div class="alert alert-danger alert-dismissable">
          <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
          <strong>Timelapse in progress.</strong> Currently it is not possible to take a photo. You can stop the timelapse if you follow <a href="/timelapse" class="alert-link">this link</a>.
        </div>
      </div>
    </div>
  % endif
  <div class="row">
    <div class="col-md-8">
      <div class="well">
        <a href="${request.static_url('raspistillweb:pictures/')}${imagedata['filename']}">
          <img src="${request.static_url('raspistillweb:pictures/')}${imagedata['filename']}" class="img-responsive">
        </a>
      </div>
    </div>
    <div class="col-md-4">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">Image metadata</h3>
        </div>
        <div class="panel-body">
          <dl>
            <dt>Date</dt>
            <dd>${imagedata['date']}</dd>
            <dt>Filesize</dt>
            <dd>${imagedata['filesize']}</dd>
            <dt>Image Resolution</dt>
            <dd>${imagedata['resolution']}</dd>
            <dt>ISO</dt>
            <dd>${imagedata['ISO']}</dd>
            <dt>Exposure Time</dt>
            <dd>${imagedata['exposure_time']}</dd>
            <dt>Image Exposure Mode</dt>
            <dd>${imagedata['exposure_mode']}</dd>
            <dt>Image Effect</dt>
            <dd>${imagedata['image_effect']}</dd>
            <dt>AWB Mode</dt>
            <dd>${imagedata['awb_mode']}</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>  
</div>
  	

