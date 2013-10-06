from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_mako')
    #settings['mako.directories'] = os.path.join(here, 'templates')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('pictures', 'pictures', cache_max_age=3600)
    config.add_route('home','/')
    config.add_route('settings','/settings')
    config.add_route('save','/save')
    config.scan()
    return config.make_wsgi_app()
