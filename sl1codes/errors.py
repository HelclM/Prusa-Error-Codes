# This file is part of the SL1 firmware
# Copyright (C) 2020 Prusa Research a.s. - www.prusa3d.com
# SPDX-License-Identifier: GPL-3.0-or-later

"""
SL1 error codes

Warning: The codes has not yet been officially approved.
"""


from sl1codes.codes import Code, Class, unique_codes, Codes


@unique_codes
class Errors(Codes):
    """
    Error and exception identification codes

    TODO: @!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!
    TODO: WARNING, these codes are based on draft of the specification.
    TODO: Remove this warning once the source document is accepted.
    TODO: @!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!
    """

    # Basic error codes
    NONE = Code(Class.SYSTEM, 0, "No problem")
    UNKNOWN = Code(Class.SYSTEM, 1, "An unknown error has occurred")

    # General error codes
    GENERAL_TILT_HOME_FAILURE = Code(Class.MECHANICAL, 1, None)
    GENERAL_TOWER_HOME_FAILURE = Code(Class.MECHANICAL, 2, None)
    GENERAL_CONFIG_EXCEPTION = Code(Class.SYSTEM, 5, None)
    GENERAL_MOTION_CONTROLLER_EXCEPTION = Code(Class.ELECTRICAL, 6, None)
    GENERAL_NOT_AVAILABLE_IN_STATE = Code(Class.SYSTEM, 6, None)
    GENERAL_DBUS_MAPPING_EXCEPTION = Code(Class.SYSTEM, 7, None)
    GENERAL_REPRINT_WITHOUT_HISTORY = Code(Class.SYSTEM, 8, None)
    GENERAL_MISSING_WIZARD_DATA = Code(Class.SYSTEM, 9, None)
    GENERAL_MISSING_CALIBRATION_DATA = Code(Class.SYSTEM, 10, None)
    GENERAL_MISSING_UVCALIBRATION_DATA = Code(Class.SYSTEM, 11, None)
    GENERAL_MISSING_UVPWM_SETTINGS = Code(Class.SYSTEM, 12, None)
    GENERAL_FAILED_TO_MQTT_SEND = Code(Class.CONNECTIVITY, 1, None)
    GENERAL_FAILED_UPDATE_CHANNEL_SET = Code(Class.SYSTEM, 13, None)
    GENERAL_FAILED_UPDATE_CHANNEL_GET = Code(Class.SYSTEM, 14, None)
    GENERAL_NOT_CONNECTED_TO_NETWORK = Code(Class.CONNECTIVITY, 2, None)
    GENERAL_CONNECTION_FAILED = Code(Class.CONNECTIVITY, 3, None)
    GENERAL_DOWNLOAD_FAILED = Code(Class.CONNECTIVITY, 4, None)
    GENERAL_NOT_ENOUGH_INTERNAL_SPACE = Code(Class.SYSTEM, 16, None)
    GENERAL_ADMIN_NOT_AVAILABLE = Code(Class.SYSTEM, 17, None)

    # Exposure error codes
    EXPOSURE_TILT_FAILURE = Code(Class.MECHANICAL, 10, None)
    EXPOSURE_TOWER_FAILURE = Code(Class.MECHANICAL, 12, None)
    EXPOSURE_TOWER_MOVE_FAILURE = Code(Class.MECHANICAL, 3, None)
    EXPOSURE_PROJECT_FAILURE = Code(Class.SYSTEM, 4, None)
    EXPOSURE_TEMP_SENSOR_FAILURE = Code(Class.TEMPERATURE, 5, None)
    EXPOSURE_FAN_FAILURE = Code(Class.MECHANICAL, 6, None)
    EXPOSURE_RESIN_SENSOR_FAILURE = Code(Class.ELECTRICAL, 7, None)
    EXPOSURE_RESIN_TOO_LOW = Code(Class.MECHANICAL, 8, None)
    EXPOSURE_RESIN_TOO_HIGH = Code(Class.MECHANICAL, 9, None)
    EXPOSURE_WARNING_ESCALATION = Code(Class.SYSTEM, 15, None)
