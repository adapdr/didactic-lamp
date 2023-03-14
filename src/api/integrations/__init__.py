"""Module contains all API Integrations"""
from .zapper import ZapperIntegration


class IntegrationsContainer:
    """Holds all API Integrations"""
    Zapper = ZapperIntegration


Integrations = IntegrationsContainer()
