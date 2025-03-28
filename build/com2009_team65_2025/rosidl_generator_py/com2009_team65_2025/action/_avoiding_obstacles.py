# generated from rosidl_generator_py/resource/_idl.py.em
# with input from com2009_team65_2025:action/AvoidingObstacles.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AvoidingObstacles_Goal(type):
    """Metaclass of message 'AvoidingObstacles_Goal'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__avoiding_obstacles__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__avoiding_obstacles__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__avoiding_obstacles__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__avoiding_obstacles__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__avoiding_obstacles__goal

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AvoidingObstacles_Goal(metaclass=Metaclass_AvoidingObstacles_Goal):
    """Message class 'AvoidingObstacles_Goal'."""

    __slots__ = [
        '_fwd_velocity',
        '_ang_velocity',
        '_stopping_distance',
    ]

    _fields_and_field_types = {
        'fwd_velocity': 'float',
        'ang_velocity': 'float',
        'stopping_distance': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.fwd_velocity = kwargs.get('fwd_velocity', float())
        self.ang_velocity = kwargs.get('ang_velocity', float())
        self.stopping_distance = kwargs.get('stopping_distance', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.fwd_velocity != other.fwd_velocity:
            return False
        if self.ang_velocity != other.ang_velocity:
            return False
        if self.stopping_distance != other.stopping_distance:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def fwd_velocity(self):
        """Message field 'fwd_velocity'."""
        return self._fwd_velocity

    @fwd_velocity.setter
    def fwd_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fwd_velocity' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'fwd_velocity' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._fwd_velocity = value

    @builtins.property
    def ang_velocity(self):
        """Message field 'ang_velocity'."""
        return self._ang_velocity

    @ang_velocity.setter
    def ang_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ang_velocity' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ang_velocity' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ang_velocity = value

    @builtins.property
    def stopping_distance(self):
        """Message field 'stopping_distance'."""
        return self._stopping_distance

    @stopping_distance.setter
    def stopping_distance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'stopping_distance' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'stopping_distance' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._stopping_distance = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_AvoidingObstacles_Result(type):
    """Metaclass of message 'AvoidingObstacles_Result'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__avoiding_obstacles__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__avoiding_obstacles__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__avoiding_obstacles__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__avoiding_obstacles__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__avoiding_obstacles__result

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AvoidingObstacles_Result(metaclass=Metaclass_AvoidingObstacles_Result):
    """Message class 'AvoidingObstacles_Result'."""

    __slots__ = [
        '_total_distance_travelled',
        '_closest_obstacle',
    ]

    _fields_and_field_types = {
        'total_distance_travelled': 'float',
        'closest_obstacle': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.total_distance_travelled = kwargs.get('total_distance_travelled', float())
        self.closest_obstacle = kwargs.get('closest_obstacle', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.total_distance_travelled != other.total_distance_travelled:
            return False
        if self.closest_obstacle != other.closest_obstacle:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def total_distance_travelled(self):
        """Message field 'total_distance_travelled'."""
        return self._total_distance_travelled

    @total_distance_travelled.setter
    def total_distance_travelled(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'total_distance_travelled' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'total_distance_travelled' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._total_distance_travelled = value

    @builtins.property
    def closest_obstacle(self):
        """Message field 'closest_obstacle'."""
        return self._closest_obstacle

    @closest_obstacle.setter
    def closest_obstacle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'closest_obstacle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'closest_obstacle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._closest_obstacle = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_AvoidingObstacles_Feedback(type):
    """Metaclass of message 'AvoidingObstacles_Feedback'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__avoiding_obstacles__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__avoiding_obstacles__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__avoiding_obstacles__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__avoiding_obstacles__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__avoiding_obstacles__feedback

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AvoidingObstacles_Feedback(metaclass=Metaclass_AvoidingObstacles_Feedback):
    """Message class 'AvoidingObstacles_Feedback'."""

    __slots__ = [
        '_current_distance_travelled',
        '_current_orientation',
    ]

    _fields_and_field_types = {
        'current_distance_travelled': 'float',
        'current_orientation': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.current_distance_travelled = kwargs.get('current_distance_travelled', float())
        self.current_orientation = kwargs.get('current_orientation', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.current_distance_travelled != other.current_distance_travelled:
            return False
        if self.current_orientation != other.current_orientation:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def current_distance_travelled(self):
        """Message field 'current_distance_travelled'."""
        return self._current_distance_travelled

    @current_distance_travelled.setter
    def current_distance_travelled(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'current_distance_travelled' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'current_distance_travelled' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._current_distance_travelled = value

    @builtins.property
    def current_orientation(self):
        """Message field 'current_orientation'."""
        return self._current_orientation

    @current_orientation.setter
    def current_orientation(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'current_orientation' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'current_orientation' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._current_orientation = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AvoidingObstacles_SendGoal_Request(type):
    """Metaclass of message 'AvoidingObstacles_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__avoiding_obstacles__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__avoiding_obstacles__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__avoiding_obstacles__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__avoiding_obstacles__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__avoiding_obstacles__send_goal__request

            from com2009_team65_2025.action import AvoidingObstacles
            if AvoidingObstacles.Goal.__class__._TYPE_SUPPORT is None:
                AvoidingObstacles.Goal.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AvoidingObstacles_SendGoal_Request(metaclass=Metaclass_AvoidingObstacles_SendGoal_Request):
    """Message class 'AvoidingObstacles_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'com2009_team65_2025/AvoidingObstacles_Goal',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['com2009_team65_2025', 'action'], 'AvoidingObstacles_Goal'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_Goal
        self.goal = kwargs.get('goal', AvoidingObstacles_Goal())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def goal(self):
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value):
        if __debug__:
            from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_Goal
            assert \
                isinstance(value, AvoidingObstacles_Goal), \
                "The 'goal' field must be a sub message of type 'AvoidingObstacles_Goal'"
        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AvoidingObstacles_SendGoal_Response(type):
    """Metaclass of message 'AvoidingObstacles_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__avoiding_obstacles__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__avoiding_obstacles__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__avoiding_obstacles__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__avoiding_obstacles__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__avoiding_obstacles__send_goal__response

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AvoidingObstacles_SendGoal_Response(metaclass=Metaclass_AvoidingObstacles_SendGoal_Response):
    """Message class 'AvoidingObstacles_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
    ]

    _fields_and_field_types = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.accepted = kwargs.get('accepted', bool())
        from builtin_interfaces.msg import Time
        self.stamp = kwargs.get('stamp', Time())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accepted(self):
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'accepted' field must be of type 'bool'"
        self._accepted = value

    @builtins.property
    def stamp(self):
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value


class Metaclass_AvoidingObstacles_SendGoal(type):
    """Metaclass of service 'AvoidingObstacles_SendGoal'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__avoiding_obstacles__send_goal

            from com2009_team65_2025.action import _avoiding_obstacles
            if _avoiding_obstacles.Metaclass_AvoidingObstacles_SendGoal_Request._TYPE_SUPPORT is None:
                _avoiding_obstacles.Metaclass_AvoidingObstacles_SendGoal_Request.__import_type_support__()
            if _avoiding_obstacles.Metaclass_AvoidingObstacles_SendGoal_Response._TYPE_SUPPORT is None:
                _avoiding_obstacles.Metaclass_AvoidingObstacles_SendGoal_Response.__import_type_support__()


class AvoidingObstacles_SendGoal(metaclass=Metaclass_AvoidingObstacles_SendGoal):
    from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_SendGoal_Request as Request
    from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_SendGoal_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AvoidingObstacles_GetResult_Request(type):
    """Metaclass of message 'AvoidingObstacles_GetResult_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__avoiding_obstacles__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__avoiding_obstacles__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__avoiding_obstacles__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__avoiding_obstacles__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__avoiding_obstacles__get_result__request

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AvoidingObstacles_GetResult_Request(metaclass=Metaclass_AvoidingObstacles_GetResult_Request):
    """Message class 'AvoidingObstacles_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AvoidingObstacles_GetResult_Response(type):
    """Metaclass of message 'AvoidingObstacles_GetResult_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__avoiding_obstacles__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__avoiding_obstacles__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__avoiding_obstacles__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__avoiding_obstacles__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__avoiding_obstacles__get_result__response

            from com2009_team65_2025.action import AvoidingObstacles
            if AvoidingObstacles.Result.__class__._TYPE_SUPPORT is None:
                AvoidingObstacles.Result.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AvoidingObstacles_GetResult_Response(metaclass=Metaclass_AvoidingObstacles_GetResult_Response):
    """Message class 'AvoidingObstacles_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
    ]

    _fields_and_field_types = {
        'status': 'int8',
        'result': 'com2009_team65_2025/AvoidingObstacles_Result',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['com2009_team65_2025', 'action'], 'AvoidingObstacles_Result'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.status = kwargs.get('status', int())
        from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_Result
        self.result = kwargs.get('result', AvoidingObstacles_Result())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'status' field must be an integer in [-128, 127]"
        self._status = value

    @builtins.property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_Result
            assert \
                isinstance(value, AvoidingObstacles_Result), \
                "The 'result' field must be a sub message of type 'AvoidingObstacles_Result'"
        self._result = value


class Metaclass_AvoidingObstacles_GetResult(type):
    """Metaclass of service 'AvoidingObstacles_GetResult'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__avoiding_obstacles__get_result

            from com2009_team65_2025.action import _avoiding_obstacles
            if _avoiding_obstacles.Metaclass_AvoidingObstacles_GetResult_Request._TYPE_SUPPORT is None:
                _avoiding_obstacles.Metaclass_AvoidingObstacles_GetResult_Request.__import_type_support__()
            if _avoiding_obstacles.Metaclass_AvoidingObstacles_GetResult_Response._TYPE_SUPPORT is None:
                _avoiding_obstacles.Metaclass_AvoidingObstacles_GetResult_Response.__import_type_support__()


class AvoidingObstacles_GetResult(metaclass=Metaclass_AvoidingObstacles_GetResult):
    from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_GetResult_Request as Request
    from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_GetResult_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AvoidingObstacles_FeedbackMessage(type):
    """Metaclass of message 'AvoidingObstacles_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__avoiding_obstacles__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__avoiding_obstacles__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__avoiding_obstacles__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__avoiding_obstacles__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__avoiding_obstacles__feedback_message

            from com2009_team65_2025.action import AvoidingObstacles
            if AvoidingObstacles.Feedback.__class__._TYPE_SUPPORT is None:
                AvoidingObstacles.Feedback.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AvoidingObstacles_FeedbackMessage(metaclass=Metaclass_AvoidingObstacles_FeedbackMessage):
    """Message class 'AvoidingObstacles_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'com2009_team65_2025/AvoidingObstacles_Feedback',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['com2009_team65_2025', 'action'], 'AvoidingObstacles_Feedback'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_Feedback
        self.feedback = kwargs.get('feedback', AvoidingObstacles_Feedback())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def feedback(self):
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        if __debug__:
            from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_Feedback
            assert \
                isinstance(value, AvoidingObstacles_Feedback), \
                "The 'feedback' field must be a sub message of type 'AvoidingObstacles_Feedback'"
        self._feedback = value


class Metaclass_AvoidingObstacles(type):
    """Metaclass of action 'AvoidingObstacles'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('com2009_team65_2025')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'com2009_team65_2025.action.AvoidingObstacles')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__avoiding_obstacles

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from com2009_team65_2025.action import _avoiding_obstacles
            if _avoiding_obstacles.Metaclass_AvoidingObstacles_SendGoal._TYPE_SUPPORT is None:
                _avoiding_obstacles.Metaclass_AvoidingObstacles_SendGoal.__import_type_support__()
            if _avoiding_obstacles.Metaclass_AvoidingObstacles_GetResult._TYPE_SUPPORT is None:
                _avoiding_obstacles.Metaclass_AvoidingObstacles_GetResult.__import_type_support__()
            if _avoiding_obstacles.Metaclass_AvoidingObstacles_FeedbackMessage._TYPE_SUPPORT is None:
                _avoiding_obstacles.Metaclass_AvoidingObstacles_FeedbackMessage.__import_type_support__()


class AvoidingObstacles(metaclass=Metaclass_AvoidingObstacles):

    # The goal message defined in the action definition.
    from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_Goal as Goal
    # The result message defined in the action definition.
    from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_Result as Result
    # The feedback message defined in the action definition.
    from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from com2009_team65_2025.action._avoiding_obstacles import AvoidingObstacles_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')
