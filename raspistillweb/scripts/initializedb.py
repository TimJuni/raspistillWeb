import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Picture,
    Settings,
    Timelapse,
    Base,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        picture = Picture(
                        filename = '1',
                        image_effect = '1',
                        exposure_mode = '1',
                        awb_mode = '1',
                        resolution = '1',
                        ISO = 1,
                        exposure_time ='1',
                        date = '1',
                        timestamp = '1',
                        filesize = '1'
                        )
        DBSession.add(picture)

        app_settings = Settings(
                        image_width = 800,
                        image_height = 600,
                        timelapse_interval = 4000,
                        timelapse_time = 20000,
                        exposure_mode = 'auto',
                        image_effect = 'none',
                        awb_mode = 'auto',
                        image_ISO = 'auto',
                        image_rotation = '0'
                        )
        DBSession.add(app_settings)

        timelapse = Timelapse(
                        filename = 'test',
                        timeStart = 'test',
                        image_effect = 'test',
                        exposure_mode = 'test',
                        awb_mode = 'auto',
                        timeEnd = 'none'
                        )

        DBSession.add(timelapse)
