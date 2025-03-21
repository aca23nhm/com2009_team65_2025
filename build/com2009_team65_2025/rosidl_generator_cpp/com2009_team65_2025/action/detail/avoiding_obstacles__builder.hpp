// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from com2009_team65_2025:action/AvoidingObstacles.idl
// generated code does not contain a copyright notice

#ifndef COM2009_TEAM65_2025__ACTION__DETAIL__AVOIDING_OBSTACLES__BUILDER_HPP_
#define COM2009_TEAM65_2025__ACTION__DETAIL__AVOIDING_OBSTACLES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "com2009_team65_2025/action/detail/avoiding_obstacles__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace com2009_team65_2025
{

namespace action
{

namespace builder
{

class Init_AvoidingObstacles_Goal_stopping_distance
{
public:
  explicit Init_AvoidingObstacles_Goal_stopping_distance(::com2009_team65_2025::action::AvoidingObstacles_Goal & msg)
  : msg_(msg)
  {}
  ::com2009_team65_2025::action::AvoidingObstacles_Goal stopping_distance(::com2009_team65_2025::action::AvoidingObstacles_Goal::_stopping_distance_type arg)
  {
    msg_.stopping_distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_Goal msg_;
};

class Init_AvoidingObstacles_Goal_ang_velocity
{
public:
  explicit Init_AvoidingObstacles_Goal_ang_velocity(::com2009_team65_2025::action::AvoidingObstacles_Goal & msg)
  : msg_(msg)
  {}
  Init_AvoidingObstacles_Goal_stopping_distance ang_velocity(::com2009_team65_2025::action::AvoidingObstacles_Goal::_ang_velocity_type arg)
  {
    msg_.ang_velocity = std::move(arg);
    return Init_AvoidingObstacles_Goal_stopping_distance(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_Goal msg_;
};

class Init_AvoidingObstacles_Goal_fwd_velocity
{
public:
  Init_AvoidingObstacles_Goal_fwd_velocity()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AvoidingObstacles_Goal_ang_velocity fwd_velocity(::com2009_team65_2025::action::AvoidingObstacles_Goal::_fwd_velocity_type arg)
  {
    msg_.fwd_velocity = std::move(arg);
    return Init_AvoidingObstacles_Goal_ang_velocity(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::com2009_team65_2025::action::AvoidingObstacles_Goal>()
{
  return com2009_team65_2025::action::builder::Init_AvoidingObstacles_Goal_fwd_velocity();
}

}  // namespace com2009_team65_2025


namespace com2009_team65_2025
{

namespace action
{

namespace builder
{

class Init_AvoidingObstacles_Result_closest_obstacle
{
public:
  explicit Init_AvoidingObstacles_Result_closest_obstacle(::com2009_team65_2025::action::AvoidingObstacles_Result & msg)
  : msg_(msg)
  {}
  ::com2009_team65_2025::action::AvoidingObstacles_Result closest_obstacle(::com2009_team65_2025::action::AvoidingObstacles_Result::_closest_obstacle_type arg)
  {
    msg_.closest_obstacle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_Result msg_;
};

class Init_AvoidingObstacles_Result_total_distance_travelled
{
public:
  Init_AvoidingObstacles_Result_total_distance_travelled()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AvoidingObstacles_Result_closest_obstacle total_distance_travelled(::com2009_team65_2025::action::AvoidingObstacles_Result::_total_distance_travelled_type arg)
  {
    msg_.total_distance_travelled = std::move(arg);
    return Init_AvoidingObstacles_Result_closest_obstacle(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::com2009_team65_2025::action::AvoidingObstacles_Result>()
{
  return com2009_team65_2025::action::builder::Init_AvoidingObstacles_Result_total_distance_travelled();
}

}  // namespace com2009_team65_2025


namespace com2009_team65_2025
{

namespace action
{

namespace builder
{

class Init_AvoidingObstacles_Feedback_current_orientation
{
public:
  explicit Init_AvoidingObstacles_Feedback_current_orientation(::com2009_team65_2025::action::AvoidingObstacles_Feedback & msg)
  : msg_(msg)
  {}
  ::com2009_team65_2025::action::AvoidingObstacles_Feedback current_orientation(::com2009_team65_2025::action::AvoidingObstacles_Feedback::_current_orientation_type arg)
  {
    msg_.current_orientation = std::move(arg);
    return std::move(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_Feedback msg_;
};

class Init_AvoidingObstacles_Feedback_current_distance_travelled
{
public:
  Init_AvoidingObstacles_Feedback_current_distance_travelled()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AvoidingObstacles_Feedback_current_orientation current_distance_travelled(::com2009_team65_2025::action::AvoidingObstacles_Feedback::_current_distance_travelled_type arg)
  {
    msg_.current_distance_travelled = std::move(arg);
    return Init_AvoidingObstacles_Feedback_current_orientation(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::com2009_team65_2025::action::AvoidingObstacles_Feedback>()
{
  return com2009_team65_2025::action::builder::Init_AvoidingObstacles_Feedback_current_distance_travelled();
}

}  // namespace com2009_team65_2025


namespace com2009_team65_2025
{

namespace action
{

namespace builder
{

class Init_AvoidingObstacles_SendGoal_Request_goal
{
public:
  explicit Init_AvoidingObstacles_SendGoal_Request_goal(::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Request goal(::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Request msg_;
};

class Init_AvoidingObstacles_SendGoal_Request_goal_id
{
public:
  Init_AvoidingObstacles_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AvoidingObstacles_SendGoal_Request_goal goal_id(::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_AvoidingObstacles_SendGoal_Request_goal(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Request>()
{
  return com2009_team65_2025::action::builder::Init_AvoidingObstacles_SendGoal_Request_goal_id();
}

}  // namespace com2009_team65_2025


namespace com2009_team65_2025
{

namespace action
{

namespace builder
{

class Init_AvoidingObstacles_SendGoal_Response_stamp
{
public:
  explicit Init_AvoidingObstacles_SendGoal_Response_stamp(::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Response stamp(::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Response msg_;
};

class Init_AvoidingObstacles_SendGoal_Response_accepted
{
public:
  Init_AvoidingObstacles_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AvoidingObstacles_SendGoal_Response_stamp accepted(::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_AvoidingObstacles_SendGoal_Response_stamp(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::com2009_team65_2025::action::AvoidingObstacles_SendGoal_Response>()
{
  return com2009_team65_2025::action::builder::Init_AvoidingObstacles_SendGoal_Response_accepted();
}

}  // namespace com2009_team65_2025


namespace com2009_team65_2025
{

namespace action
{

namespace builder
{

class Init_AvoidingObstacles_GetResult_Request_goal_id
{
public:
  Init_AvoidingObstacles_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::com2009_team65_2025::action::AvoidingObstacles_GetResult_Request goal_id(::com2009_team65_2025::action::AvoidingObstacles_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::com2009_team65_2025::action::AvoidingObstacles_GetResult_Request>()
{
  return com2009_team65_2025::action::builder::Init_AvoidingObstacles_GetResult_Request_goal_id();
}

}  // namespace com2009_team65_2025


namespace com2009_team65_2025
{

namespace action
{

namespace builder
{

class Init_AvoidingObstacles_GetResult_Response_result
{
public:
  explicit Init_AvoidingObstacles_GetResult_Response_result(::com2009_team65_2025::action::AvoidingObstacles_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::com2009_team65_2025::action::AvoidingObstacles_GetResult_Response result(::com2009_team65_2025::action::AvoidingObstacles_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_GetResult_Response msg_;
};

class Init_AvoidingObstacles_GetResult_Response_status
{
public:
  Init_AvoidingObstacles_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AvoidingObstacles_GetResult_Response_result status(::com2009_team65_2025::action::AvoidingObstacles_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_AvoidingObstacles_GetResult_Response_result(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::com2009_team65_2025::action::AvoidingObstacles_GetResult_Response>()
{
  return com2009_team65_2025::action::builder::Init_AvoidingObstacles_GetResult_Response_status();
}

}  // namespace com2009_team65_2025


namespace com2009_team65_2025
{

namespace action
{

namespace builder
{

class Init_AvoidingObstacles_FeedbackMessage_feedback
{
public:
  explicit Init_AvoidingObstacles_FeedbackMessage_feedback(::com2009_team65_2025::action::AvoidingObstacles_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::com2009_team65_2025::action::AvoidingObstacles_FeedbackMessage feedback(::com2009_team65_2025::action::AvoidingObstacles_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_FeedbackMessage msg_;
};

class Init_AvoidingObstacles_FeedbackMessage_goal_id
{
public:
  Init_AvoidingObstacles_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AvoidingObstacles_FeedbackMessage_feedback goal_id(::com2009_team65_2025::action::AvoidingObstacles_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_AvoidingObstacles_FeedbackMessage_feedback(msg_);
  }

private:
  ::com2009_team65_2025::action::AvoidingObstacles_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::com2009_team65_2025::action::AvoidingObstacles_FeedbackMessage>()
{
  return com2009_team65_2025::action::builder::Init_AvoidingObstacles_FeedbackMessage_goal_id();
}

}  // namespace com2009_team65_2025

#endif  // COM2009_TEAM65_2025__ACTION__DETAIL__AVOIDING_OBSTACLES__BUILDER_HPP_
