"""Custom component for Fuel Station Sensor."""
import logging
from homeassistant.core import HomeAssistant  # Updated import
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "fuel_station_sensor"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Fuel Station Sensor component."""
    _LOGGER.info("Setting up Fuel Station Sensor")
    return True  # Return True to indicate successful setup
