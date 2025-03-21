// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from com2009_team65_2025:action/AvoidingObstacles.idl
// generated code does not contain a copyright notice
#include "com2009_team65_2025/action/detail/avoiding_obstacles__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
com2009_team65_2025__action__AvoidingObstacles_Goal__init(com2009_team65_2025__action__AvoidingObstacles_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // fwd_velocity
  // ang_velocity
  // stopping_distance
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_Goal__fini(com2009_team65_2025__action__AvoidingObstacles_Goal * msg)
{
  if (!msg) {
    return;
  }
  // fwd_velocity
  // ang_velocity
  // stopping_distance
}

bool
com2009_team65_2025__action__AvoidingObstacles_Goal__are_equal(const com2009_team65_2025__action__AvoidingObstacles_Goal * lhs, const com2009_team65_2025__action__AvoidingObstacles_Goal * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // fwd_velocity
  if (lhs->fwd_velocity != rhs->fwd_velocity) {
    return false;
  }
  // ang_velocity
  if (lhs->ang_velocity != rhs->ang_velocity) {
    return false;
  }
  // stopping_distance
  if (lhs->stopping_distance != rhs->stopping_distance) {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_Goal__copy(
  const com2009_team65_2025__action__AvoidingObstacles_Goal * input,
  com2009_team65_2025__action__AvoidingObstacles_Goal * output)
{
  if (!input || !output) {
    return false;
  }
  // fwd_velocity
  output->fwd_velocity = input->fwd_velocity;
  // ang_velocity
  output->ang_velocity = input->ang_velocity;
  // stopping_distance
  output->stopping_distance = input->stopping_distance;
  return true;
}

com2009_team65_2025__action__AvoidingObstacles_Goal *
com2009_team65_2025__action__AvoidingObstacles_Goal__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_Goal * msg = (com2009_team65_2025__action__AvoidingObstacles_Goal *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_Goal), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__AvoidingObstacles_Goal));
  bool success = com2009_team65_2025__action__AvoidingObstacles_Goal__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__AvoidingObstacles_Goal__destroy(com2009_team65_2025__action__AvoidingObstacles_Goal * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__AvoidingObstacles_Goal__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence__init(com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_Goal * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__AvoidingObstacles_Goal *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__AvoidingObstacles_Goal), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__AvoidingObstacles_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__AvoidingObstacles_Goal__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence__fini(com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      com2009_team65_2025__action__AvoidingObstacles_Goal__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence *
com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence * array = (com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence__destroy(com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence__are_equal(const com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence * lhs, const com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_Goal__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence__copy(
  const com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence * input,
  com2009_team65_2025__action__AvoidingObstacles_Goal__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__AvoidingObstacles_Goal);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__AvoidingObstacles_Goal * data =
      (com2009_team65_2025__action__AvoidingObstacles_Goal *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__AvoidingObstacles_Goal__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__AvoidingObstacles_Goal__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_Goal__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
com2009_team65_2025__action__AvoidingObstacles_Result__init(com2009_team65_2025__action__AvoidingObstacles_Result * msg)
{
  if (!msg) {
    return false;
  }
  // total_distance_travelled
  // closest_obstacle
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_Result__fini(com2009_team65_2025__action__AvoidingObstacles_Result * msg)
{
  if (!msg) {
    return;
  }
  // total_distance_travelled
  // closest_obstacle
}

bool
com2009_team65_2025__action__AvoidingObstacles_Result__are_equal(const com2009_team65_2025__action__AvoidingObstacles_Result * lhs, const com2009_team65_2025__action__AvoidingObstacles_Result * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // total_distance_travelled
  if (lhs->total_distance_travelled != rhs->total_distance_travelled) {
    return false;
  }
  // closest_obstacle
  if (lhs->closest_obstacle != rhs->closest_obstacle) {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_Result__copy(
  const com2009_team65_2025__action__AvoidingObstacles_Result * input,
  com2009_team65_2025__action__AvoidingObstacles_Result * output)
{
  if (!input || !output) {
    return false;
  }
  // total_distance_travelled
  output->total_distance_travelled = input->total_distance_travelled;
  // closest_obstacle
  output->closest_obstacle = input->closest_obstacle;
  return true;
}

com2009_team65_2025__action__AvoidingObstacles_Result *
com2009_team65_2025__action__AvoidingObstacles_Result__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_Result * msg = (com2009_team65_2025__action__AvoidingObstacles_Result *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_Result), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__AvoidingObstacles_Result));
  bool success = com2009_team65_2025__action__AvoidingObstacles_Result__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__AvoidingObstacles_Result__destroy(com2009_team65_2025__action__AvoidingObstacles_Result * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__AvoidingObstacles_Result__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__AvoidingObstacles_Result__Sequence__init(com2009_team65_2025__action__AvoidingObstacles_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_Result * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__AvoidingObstacles_Result *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__AvoidingObstacles_Result), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__AvoidingObstacles_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__AvoidingObstacles_Result__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_Result__Sequence__fini(com2009_team65_2025__action__AvoidingObstacles_Result__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      com2009_team65_2025__action__AvoidingObstacles_Result__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

com2009_team65_2025__action__AvoidingObstacles_Result__Sequence *
com2009_team65_2025__action__AvoidingObstacles_Result__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_Result__Sequence * array = (com2009_team65_2025__action__AvoidingObstacles_Result__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_Result__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__AvoidingObstacles_Result__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__AvoidingObstacles_Result__Sequence__destroy(com2009_team65_2025__action__AvoidingObstacles_Result__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__AvoidingObstacles_Result__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__AvoidingObstacles_Result__Sequence__are_equal(const com2009_team65_2025__action__AvoidingObstacles_Result__Sequence * lhs, const com2009_team65_2025__action__AvoidingObstacles_Result__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_Result__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_Result__Sequence__copy(
  const com2009_team65_2025__action__AvoidingObstacles_Result__Sequence * input,
  com2009_team65_2025__action__AvoidingObstacles_Result__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__AvoidingObstacles_Result);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__AvoidingObstacles_Result * data =
      (com2009_team65_2025__action__AvoidingObstacles_Result *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__AvoidingObstacles_Result__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__AvoidingObstacles_Result__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_Result__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
com2009_team65_2025__action__AvoidingObstacles_Feedback__init(com2009_team65_2025__action__AvoidingObstacles_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // current_distance_travelled
  // current_orientation
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_Feedback__fini(com2009_team65_2025__action__AvoidingObstacles_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // current_distance_travelled
  // current_orientation
}

bool
com2009_team65_2025__action__AvoidingObstacles_Feedback__are_equal(const com2009_team65_2025__action__AvoidingObstacles_Feedback * lhs, const com2009_team65_2025__action__AvoidingObstacles_Feedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // current_distance_travelled
  if (lhs->current_distance_travelled != rhs->current_distance_travelled) {
    return false;
  }
  // current_orientation
  if (lhs->current_orientation != rhs->current_orientation) {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_Feedback__copy(
  const com2009_team65_2025__action__AvoidingObstacles_Feedback * input,
  com2009_team65_2025__action__AvoidingObstacles_Feedback * output)
{
  if (!input || !output) {
    return false;
  }
  // current_distance_travelled
  output->current_distance_travelled = input->current_distance_travelled;
  // current_orientation
  output->current_orientation = input->current_orientation;
  return true;
}

com2009_team65_2025__action__AvoidingObstacles_Feedback *
com2009_team65_2025__action__AvoidingObstacles_Feedback__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_Feedback * msg = (com2009_team65_2025__action__AvoidingObstacles_Feedback *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_Feedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__AvoidingObstacles_Feedback));
  bool success = com2009_team65_2025__action__AvoidingObstacles_Feedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__AvoidingObstacles_Feedback__destroy(com2009_team65_2025__action__AvoidingObstacles_Feedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__AvoidingObstacles_Feedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence__init(com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_Feedback * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__AvoidingObstacles_Feedback *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__AvoidingObstacles_Feedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__AvoidingObstacles_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__AvoidingObstacles_Feedback__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence__fini(com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      com2009_team65_2025__action__AvoidingObstacles_Feedback__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence *
com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence * array = (com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence__destroy(com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence__are_equal(const com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence * lhs, const com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_Feedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence__copy(
  const com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence * input,
  com2009_team65_2025__action__AvoidingObstacles_Feedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__AvoidingObstacles_Feedback);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__AvoidingObstacles_Feedback * data =
      (com2009_team65_2025__action__AvoidingObstacles_Feedback *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__AvoidingObstacles_Feedback__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__AvoidingObstacles_Feedback__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_Feedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `goal`
// already included above
// #include "com2009_team65_2025/action/detail/avoiding_obstacles__functions.h"

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__init(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!com2009_team65_2025__action__AvoidingObstacles_Goal__init(&msg->goal)) {
    com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__fini(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  com2009_team65_2025__action__AvoidingObstacles_Goal__fini(&msg->goal);
}

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__are_equal(const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * lhs, const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // goal
  if (!com2009_team65_2025__action__AvoidingObstacles_Goal__are_equal(
      &(lhs->goal), &(rhs->goal)))
  {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__copy(
  const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * input,
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // goal
  if (!com2009_team65_2025__action__AvoidingObstacles_Goal__copy(
      &(input->goal), &(output->goal)))
  {
    return false;
  }
  return true;
}

com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request *
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * msg = (com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request));
  bool success = com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__destroy(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence__init(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence__fini(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence *
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence * array = (com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence__destroy(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence__are_equal(const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence * lhs, const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence__copy(
  const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence * input,
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request * data =
      (com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_SendGoal_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__init(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__fini(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__are_equal(const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * lhs, const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // accepted
  if (lhs->accepted != rhs->accepted) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__copy(
  const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * input,
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // accepted
  output->accepted = input->accepted;
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  return true;
}

com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response *
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * msg = (com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response));
  bool success = com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__destroy(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence__init(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence__fini(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence *
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence * array = (com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence__destroy(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence__are_equal(const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence * lhs, const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence__copy(
  const com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence * input,
  com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response * data =
      (com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_SendGoal_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__init(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__fini(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__are_equal(const com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * lhs, const com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__copy(
  const com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * input,
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  return true;
}

com2009_team65_2025__action__AvoidingObstacles_GetResult_Request *
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * msg = (com2009_team65_2025__action__AvoidingObstacles_GetResult_Request *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request));
  bool success = com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__destroy(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence__init(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__AvoidingObstacles_GetResult_Request *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence__fini(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence *
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence * array = (com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence__destroy(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence__are_equal(const com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence * lhs, const com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence__copy(
  const com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence * input,
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__AvoidingObstacles_GetResult_Request * data =
      (com2009_team65_2025__action__AvoidingObstacles_GetResult_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_GetResult_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `result`
// already included above
// #include "com2009_team65_2025/action/detail/avoiding_obstacles__functions.h"

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__init(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!com2009_team65_2025__action__AvoidingObstacles_Result__init(&msg->result)) {
    com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__fini(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  com2009_team65_2025__action__AvoidingObstacles_Result__fini(&msg->result);
}

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__are_equal(const com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * lhs, const com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // result
  if (!com2009_team65_2025__action__AvoidingObstacles_Result__are_equal(
      &(lhs->result), &(rhs->result)))
  {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__copy(
  const com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * input,
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  output->status = input->status;
  // result
  if (!com2009_team65_2025__action__AvoidingObstacles_Result__copy(
      &(input->result), &(output->result)))
  {
    return false;
  }
  return true;
}

com2009_team65_2025__action__AvoidingObstacles_GetResult_Response *
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * msg = (com2009_team65_2025__action__AvoidingObstacles_GetResult_Response *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response));
  bool success = com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__destroy(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence__init(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__AvoidingObstacles_GetResult_Response *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence__fini(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence *
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence * array = (com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence__destroy(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence__are_equal(const com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence * lhs, const com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence__copy(
  const com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence * input,
  com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__AvoidingObstacles_GetResult_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__AvoidingObstacles_GetResult_Response * data =
      (com2009_team65_2025__action__AvoidingObstacles_GetResult_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_GetResult_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `feedback`
// already included above
// #include "com2009_team65_2025/action/detail/avoiding_obstacles__functions.h"

bool
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__init(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!com2009_team65_2025__action__AvoidingObstacles_Feedback__init(&msg->feedback)) {
    com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__fini(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  com2009_team65_2025__action__AvoidingObstacles_Feedback__fini(&msg->feedback);
}

bool
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__are_equal(const com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * lhs, const com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // feedback
  if (!com2009_team65_2025__action__AvoidingObstacles_Feedback__are_equal(
      &(lhs->feedback), &(rhs->feedback)))
  {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__copy(
  const com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * input,
  com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // feedback
  if (!com2009_team65_2025__action__AvoidingObstacles_Feedback__copy(
      &(input->feedback), &(output->feedback)))
  {
    return false;
  }
  return true;
}

com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage *
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * msg = (com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage));
  bool success = com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__destroy(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence__init(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence__fini(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence *
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence * array = (com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence__destroy(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence__are_equal(const com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence * lhs, const com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence__copy(
  const com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence * input,
  com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage * data =
      (com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__AvoidingObstacles_FeedbackMessage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
