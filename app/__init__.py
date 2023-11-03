"""
Directorio principal que contiene los módulos de la aplicación.
----
This is the main directory containing the application's modules.
"""
from app.business.router import all_router
from app.common.core import get_api

api = get_api(routers=[all_router])