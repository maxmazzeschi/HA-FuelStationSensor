from station import FuelStation
import logging
from datetime import timedelta
import voluptuous as vol

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "fuel_station_sensor"
CONF_SCAN_INTERVAL = "scan_interval"

DEFAULT_NAME = "Fuel Station"
DEFAULT_SCAN_INTERVAL = 10  # Default polling time in seconds

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
                vol.Optional(
                    CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL
                ): cv.positive_int,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)


def setup_platform(
    hass,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    _LOGGER.info("setup_platform")
    """Set up the sensor platform."""
    name = config.get(CONF_NAME)
    scan_interval = config.get(CONF_SCAN_INTERVAL)

    add_entities([FuelStationSensor(name, scan_interval)], True)


class FuelStationSensor(SensorEntity):
    _LOGGER.info("FuelStationSensor")
    """Sensor for tracking fuel station prices."""

    def __init__(self, name: str, scan_interval: int) -> None:
        """Initialize the sensor."""
        self._attr_name = name
        self._attr_state = None  # We can use the name or a count of fuels
        self._station = FuelStation(name)
        self._scan_interval = timedelta(seconds=scan_interval)

    @property
    def scan_interval(self) -> timedelta:
        """Return the polling interval."""
        return self._scan_interval

    @property
    def extra_state_attributes(self) -> dict:
        """Return additional sensor attributes (fuel prices)."""
        return self._station.get_fuel_data()

    def update(self) -> None:
        _LOGGER.info("update")
        """Fetch new state data."""
        self._station = FuelStation(self._attr_name)
        self._attr_state = len(
            self._station.fuels
        )  # Example: number of fuels available
        _LOGGER.info("Updated %s with %s fuel types",
                     self._attr_name, self._attr_state)
