import logging
import re
import os
from datetime import date
from django.conf import settings

LOGGER = logging.getLogger(__name__)


def keyboard(request):
    """**Configura variable de entorno para teclaod personalizado**
    """
    return {'KEYBOARD': settings.KEYBOARD}


def languages(request):
    """**Configura variables de entorno de las lenguas**"""
    return {'L1': settings.L1, 'L2': settings.L2}


def colors(request):
    """**Configura variables de entorno para los colores**"""
    return {'COLORS': settings.COLORS}


def project_info(request):
    """**Configura variables de entorno con información del proyecto**

    La información que se establece es *nombre*, *nombre de la organización*,
    *colaboradoras* y *redes sociales*. Las últimas dos son listas de python.
    """
    current_year = date.today().year
    banner_path = os.path.join(settings.STATICFILES_DIRS[0],
                               'user/img/banner.png')
    if os.path.isfile(banner_path):
        banner_path = 'user/img/banner.png'
    else:
        banner_path = 'img/banner.png'
    return {'PROJECT_NAME': settings.NAME, 'ORG_NAME': settings.ORG_NAME,
            'COLABS': settings.COLABS, 'LINKS': settings.LINKS,
            'META_DESC': settings.META_DESC, 'YEAR': current_year,
            'BANNER': banner_path}


def google_analytics(request):
    """**Configura variables de entorno de google analytics**"""
    return settings.GOOGLE_ANALYTICS


def user_templates(request):
    views = ["about", "help", "links", "participants"]
    regex = re.compile("[\w+\.\\n+\b+]$", re.MULTILINE)
    user_views = {}
    for view in views:
        path = f"{settings.BASE_DIR}/templates/user/{view}-user.html"
        try:
            with open(path, 'r') as html:
                html_view = html.read()
                html_view = regex.sub("<br>", html_view)
                html_view += "<br>"
        except FileNotFoundError:
            LOGGER.error(f"No se encontró el template de usuario {view}")
            html_view = ""
        name = view.upper() + "_USER"
        user_views[name] = html_view
    return user_views


def api(request):
    """**Configuraciones de los l+imites para la API**"""
    return {"API": settings.API}
