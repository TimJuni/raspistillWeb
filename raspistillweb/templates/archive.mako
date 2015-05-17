# -*- coding: utf-8 -*- 
<%inherit file="archive-layout.mako"/>

<div class="container">
  <div class="row">
  % for file in database:     
    <div class="col-xs-6 col-sm-4 col-md-3">
      <div class="panel panel-default">
        <div class="panel-heading">
          <form action="delete_picture" method="POST">
            <button type="submit" name="id" value="${file['id']}" class="close">&times;</button>
          </form>
          <h3 class="panel-title">${file['date']}</h3>
        </div>
        <div class="panel-body">
          <a href="${request.static_url('raspistillweb:pictures/')}${file['filename']}" class="thumbnail img-rounded">
            <img src="${request.static_url('raspistillweb:thumbnails/')}${file['filename']}" alt="${file['filename']}">
          </a> 
          <dl>
            <dt>Resolution</dt>
            <dd>${file['resolution']}</dd>
            <dt>Filesize</dt>
            <dd>${file['filesize']}</dd>
          </dl>
        </div>
      </div>     
    </div>   
  % endfor 
  </div>
</div>
