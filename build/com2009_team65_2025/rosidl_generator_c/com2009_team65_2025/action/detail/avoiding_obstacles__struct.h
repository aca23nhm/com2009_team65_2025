// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from com2009_team65_2025:action/AvoidingObstacles.idl
// generated code does not contain a copyright notice

#ifndef COM2009_TEAM65_2025__ACTION__DETAIL__AVOIDING_OBSTACLES__STRUCT_H_
#define COM2009_TEAM65_2025__ACTION__DETAIL__AVOIDING_OBSTACLES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/AvoidingObstacles in the package com2009_team65_2025.
typedef struct com2009_team65_2025__action__AvoidingObstacles_Goal
{
  float fwd_velocity;
  float ang_velocity;
  float stopping_distance;
} com2009_team65_2025__action__AvoidingObstacles_Goal;

// Struct for a sequence of com2009_team65_2025__action__AvoidingObstacles_Goal.
typedef struct com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence
{
  com2009_team65_2025__action__AvoidingObstacles_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/AvoidingObstacles in the package com2009_team65_2025.
typedef struct com2009_team65_2025__action__AvoidingObstacles_Result
{
  float total_distance_travelled;
  float closest_obstacle;
} com2009_team65_2025__action__AvoidingObstacles_Result;

// Struct for a sequence of com2009_team65_2025__action__AvoidingObstacles_Result.
typedef struct com2009_team65_2025__action__AvoidingObstacles_Result__Sequence
{
  com2009_team65_2025__action__AvoidingObstacles_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} com2009_team65_2025__action__AvoidingObstacles_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/AvoidingObstacles in the package com2009_team65_2025.
typedef struct com2009_team65_2025__action__AvoidingObstacles_Feedback
{
  float current_distance_travelled;
  float current_orientation;
} com2009_team65_2025__action__AvoidingObstacles_Feedback;

// Struct for a sequence of com2009_team65_2025__action__AvoidingObstacles_Feedback.
typedef struct com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence
{
  com2009_team65_2025__action__AvoidingObstacles_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "com2009_team65_2025/action/detail/avoiding_obstacles__struct.h"

/// Struct defined in action/AvoidingObstacles in the package com2009_team65_2025.
typedef struct com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  com2009_team65_2025__action__AvoidingObstacles_Goal goal;
} com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request;

// Struct for a sequence of com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request.
typedef struct com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence
{
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/AvoidingObstacles in the package com2009_team65_2025.
typedef struct com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response;

// Struct for a sequence of com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response.
typedef struct com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence
{
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/AvoidingObstacles in the package com2009_team65_2025.
typedef struct com2009_team65_2025__action__AvoidingObstacles_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} com2009_team65_2025__action__AvoidingObstacles_GetResult_Request;

// Struct for a sequence of com2009_team65_2025__action__AvoidingObstacles_GetResult_Request.
typedef struct com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence
{
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "com2009_team65_2025/action/detail/avoiding_obstacles__struct.h"

/// Struct defined in action/AvoidingObstacles in the package com2009_team65_2025.
typedef struct com2009_team65_2025__action__AvoidingObstacles_GetResult_Response
{
  int8_t status;
  com2009_team65_2025__action__AvoidingObstacles_Result result;
} com2009_team65_2025__action__AvoidingObstacles_GetResult_Response;

// Struct for a sequence of com2009_team65_2025__action__AvoidingObstacles_GetResult_Response.
typedef struct com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence
{
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "com2009_team65_2025/action/detail/avoiding_obstacles__struct.h"

/// Struct defined in action/AvoidingObstacles in the package com2009_team65_2025.
typedef struct com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  com2009_team65_2025__action__AvoidingObstacles_Feedback feedback;
} com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage;

// Struct for a sequence of com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage.
typedef struct com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence
{
  com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // COM2009_TEAM65_2025__ACTION__DETAIL__AVOIDING_OBSTACLES__STRUCT_H_
