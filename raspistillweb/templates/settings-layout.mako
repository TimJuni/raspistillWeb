# -*- coding: utf-8 -*- 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>${project}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="${request.static_url('raspistillweb:static/css/bootstrap.css')}" rel="stylesheet" media="screen">
    <link href="${request.static_url('raspistillweb:static/css/bootstrap-responsive.css')}" rel="stylesheet">
    
  </head>
  <body>

    <div class="navbar navbar-inverse navbar-static-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">raspistillWeb</a>
        </div>
        <div class="navbar-collapse collapse" style="height: 1px;">
          <ul class="nav navbar-nav">
            <li><a href="/">Home</a></li>
            <li class="active"><a href="/settings">Settings</a></li>
            <li><a href="/archive">Archive</a></li>
            <li><a href="/timelapse">Time Lapse</a></li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li>
              <form method="post">
                <input type="button" class="btn btn-danger navbar-btn" value="Take Photo" onclick="location.href='/photo'">
              </form>
            </li>
          </ul>
        </div>
      </div>
    </div>
    
    ${next.body()} 
  	
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="${request.static_url('raspistillweb:static/js/bootstrap.min.js')}"></script>
  
  </body>
</html>
