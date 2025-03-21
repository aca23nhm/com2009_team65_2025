// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from com2009_team65_2025:action/ExploreForward.idl
// generated code does not contain a copyright notice
#include "com2009_team65_2025/action/detail/explore_forward__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
com2009_team65_2025__action__ExploreForward_Goal__init(com2009_team65_2025__action__ExploreForward_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // exploration_time
  return true;
}

void
com2009_team65_2025__action__ExploreForward_Goal__fini(com2009_team65_2025__action__ExploreForward_Goal * msg)
{
  if (!msg) {
    return;
  }
  // exploration_time
}

bool
com2009_team65_2025__action__ExploreForward_Goal__are_equal(const com2009_team65_2025__action__ExploreForward_Goal * lhs, const com2009_team65_2025__action__ExploreForward_Goal * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // exploration_time
  if (lhs->exploration_time != rhs->exploration_time) {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_Goal__copy(
  const com2009_team65_2025__action__ExploreForward_Goal * input,
  com2009_team65_2025__action__ExploreForward_Goal * output)
{
  if (!input || !output) {
    return false;
  }
  // exploration_time
  output->exploration_time = input->exploration_time;
  return true;
}

com2009_team65_2025__action__ExploreForward_Goal *
com2009_team65_2025__action__ExploreForward_Goal__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_Goal * msg = (com2009_team65_2025__action__ExploreForward_Goal *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_Goal), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__ExploreForward_Goal));
  bool success = com2009_team65_2025__action__ExploreForward_Goal__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__ExploreForward_Goal__destroy(com2009_team65_2025__action__ExploreForward_Goal * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__ExploreForward_Goal__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__ExploreForward_Goal__Sequence__init(com2009_team65_2025__action__ExploreForward_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_Goal * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__ExploreForward_Goal *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__ExploreForward_Goal), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__ExploreForward_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__ExploreForward_Goal__fini(&data[i - 1]);
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
com2009_team65_2025__action__ExploreForward_Goal__Sequence__fini(com2009_team65_2025__action__ExploreForward_Goal__Sequence * array)
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
      com2009_team65_2025__action__ExploreForward_Goal__fini(&array->data[i]);
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

com2009_team65_2025__action__ExploreForward_Goal__Sequence *
com2009_team65_2025__action__ExploreForward_Goal__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_Goal__Sequence * array = (com2009_team65_2025__action__ExploreForward_Goal__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_Goal__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__ExploreForward_Goal__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__ExploreForward_Goal__Sequence__destroy(com2009_team65_2025__action__ExploreForward_Goal__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__ExploreForward_Goal__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__ExploreForward_Goal__Sequence__are_equal(const com2009_team65_2025__action__ExploreForward_Goal__Sequence * lhs, const com2009_team65_2025__action__ExploreForward_Goal__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_Goal__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_Goal__Sequence__copy(
  const com2009_team65_2025__action__ExploreForward_Goal__Sequence * input,
  com2009_team65_2025__action__ExploreForward_Goal__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__ExploreForward_Goal);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__ExploreForward_Goal * data =
      (com2009_team65_2025__action__ExploreForward_Goal *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__ExploreForward_Goal__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__ExploreForward_Goal__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_Goal__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
com2009_team65_2025__action__ExploreForward_Result__init(com2009_team65_2025__action__ExploreForward_Result * msg)
{
  if (!msg) {
    return false;
  }
  // total_time
  // zones_visited
  return true;
}

void
com2009_team65_2025__action__ExploreForward_Result__fini(com2009_team65_2025__action__ExploreForward_Result * msg)
{
  if (!msg) {
    return;
  }
  // total_time
  // zones_visited
}

bool
com2009_team65_2025__action__ExploreForward_Result__are_equal(const com2009_team65_2025__action__ExploreForward_Result * lhs, const com2009_team65_2025__action__ExploreForward_Result * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // total_time
  if (lhs->total_time != rhs->total_time) {
    return false;
  }
  // zones_visited
  if (lhs->zones_visited != rhs->zones_visited) {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_Result__copy(
  const com2009_team65_2025__action__ExploreForward_Result * input,
  com2009_team65_2025__action__ExploreForward_Result * output)
{
  if (!input || !output) {
    return false;
  }
  // total_time
  output->total_time = input->total_time;
  // zones_visited
  output->zones_visited = input->zones_visited;
  return true;
}

com2009_team65_2025__action__ExploreForward_Result *
com2009_team65_2025__action__ExploreForward_Result__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_Result * msg = (com2009_team65_2025__action__ExploreForward_Result *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_Result), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__ExploreForward_Result));
  bool success = com2009_team65_2025__action__ExploreForward_Result__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__ExploreForward_Result__destroy(com2009_team65_2025__action__ExploreForward_Result * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__ExploreForward_Result__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__ExploreForward_Result__Sequence__init(com2009_team65_2025__action__ExploreForward_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_Result * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__ExploreForward_Result *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__ExploreForward_Result), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__ExploreForward_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__ExploreForward_Result__fini(&data[i - 1]);
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
com2009_team65_2025__action__ExploreForward_Result__Sequence__fini(com2009_team65_2025__action__ExploreForward_Result__Sequence * array)
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
      com2009_team65_2025__action__ExploreForward_Result__fini(&array->data[i]);
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

com2009_team65_2025__action__ExploreForward_Result__Sequence *
com2009_team65_2025__action__ExploreForward_Result__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_Result__Sequence * array = (com2009_team65_2025__action__ExploreForward_Result__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_Result__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__ExploreForward_Result__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__ExploreForward_Result__Sequence__destroy(com2009_team65_2025__action__ExploreForward_Result__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__ExploreForward_Result__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__ExploreForward_Result__Sequence__are_equal(const com2009_team65_2025__action__ExploreForward_Result__Sequence * lhs, const com2009_team65_2025__action__ExploreForward_Result__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_Result__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_Result__Sequence__copy(
  const com2009_team65_2025__action__ExploreForward_Result__Sequence * input,
  com2009_team65_2025__action__ExploreForward_Result__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__ExploreForward_Result);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__ExploreForward_Result * data =
      (com2009_team65_2025__action__ExploreForward_Result *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__ExploreForward_Result__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__ExploreForward_Result__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_Result__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `current_state`
#include "rosidl_runtime_c/string_functions.h"

bool
com2009_team65_2025__action__ExploreForward_Feedback__init(com2009_team65_2025__action__ExploreForward_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // time_elapsed
  // current_zones
  // current_state
  if (!rosidl_runtime_c__String__init(&msg->current_state)) {
    com2009_team65_2025__action__ExploreForward_Feedback__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__ExploreForward_Feedback__fini(com2009_team65_2025__action__ExploreForward_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // time_elapsed
  // current_zones
  // current_state
  rosidl_runtime_c__String__fini(&msg->current_state);
}

bool
com2009_team65_2025__action__ExploreForward_Feedback__are_equal(const com2009_team65_2025__action__ExploreForward_Feedback * lhs, const com2009_team65_2025__action__ExploreForward_Feedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // time_elapsed
  if (lhs->time_elapsed != rhs->time_elapsed) {
    return false;
  }
  // current_zones
  if (lhs->current_zones != rhs->current_zones) {
    return false;
  }
  // current_state
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->current_state), &(rhs->current_state)))
  {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_Feedback__copy(
  const com2009_team65_2025__action__ExploreForward_Feedback * input,
  com2009_team65_2025__action__ExploreForward_Feedback * output)
{
  if (!input || !output) {
    return false;
  }
  // time_elapsed
  output->time_elapsed = input->time_elapsed;
  // current_zones
  output->current_zones = input->current_zones;
  // current_state
  if (!rosidl_runtime_c__String__copy(
      &(input->current_state), &(output->current_state)))
  {
    return false;
  }
  return true;
}

com2009_team65_2025__action__ExploreForward_Feedback *
com2009_team65_2025__action__ExploreForward_Feedback__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_Feedback * msg = (com2009_team65_2025__action__ExploreForward_Feedback *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_Feedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__ExploreForward_Feedback));
  bool success = com2009_team65_2025__action__ExploreForward_Feedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__ExploreForward_Feedback__destroy(com2009_team65_2025__action__ExploreForward_Feedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__ExploreForward_Feedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__ExploreForward_Feedback__Sequence__init(com2009_team65_2025__action__ExploreForward_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_Feedback * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__ExploreForward_Feedback *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__ExploreForward_Feedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__ExploreForward_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__ExploreForward_Feedback__fini(&data[i - 1]);
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
com2009_team65_2025__action__ExploreForward_Feedback__Sequence__fini(com2009_team65_2025__action__ExploreForward_Feedback__Sequence * array)
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
      com2009_team65_2025__action__ExploreForward_Feedback__fini(&array->data[i]);
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

com2009_team65_2025__action__ExploreForward_Feedback__Sequence *
com2009_team65_2025__action__ExploreForward_Feedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_Feedback__Sequence * array = (com2009_team65_2025__action__ExploreForward_Feedback__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_Feedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__ExploreForward_Feedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__ExploreForward_Feedback__Sequence__destroy(com2009_team65_2025__action__ExploreForward_Feedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__ExploreForward_Feedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__ExploreForward_Feedback__Sequence__are_equal(const com2009_team65_2025__action__ExploreForward_Feedback__Sequence * lhs, const com2009_team65_2025__action__ExploreForward_Feedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_Feedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_Feedback__Sequence__copy(
  const com2009_team65_2025__action__ExploreForward_Feedback__Sequence * input,
  com2009_team65_2025__action__ExploreForward_Feedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__ExploreForward_Feedback);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__ExploreForward_Feedback * data =
      (com2009_team65_2025__action__ExploreForward_Feedback *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__ExploreForward_Feedback__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__ExploreForward_Feedback__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_Feedback__copy(
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
// #include "com2009_team65_2025/action/detail/explore_forward__functions.h"

bool
com2009_team65_2025__action__ExploreForward_SendGoal_Request__init(com2009_team65_2025__action__ExploreForward_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    com2009_team65_2025__action__ExploreForward_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!com2009_team65_2025__action__ExploreForward_Goal__init(&msg->goal)) {
    com2009_team65_2025__action__ExploreForward_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__ExploreForward_SendGoal_Request__fini(com2009_team65_2025__action__ExploreForward_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  com2009_team65_2025__action__ExploreForward_Goal__fini(&msg->goal);
}

bool
com2009_team65_2025__action__ExploreForward_SendGoal_Request__are_equal(const com2009_team65_2025__action__ExploreForward_SendGoal_Request * lhs, const com2009_team65_2025__action__ExploreForward_SendGoal_Request * rhs)
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
  if (!com2009_team65_2025__action__ExploreForward_Goal__are_equal(
      &(lhs->goal), &(rhs->goal)))
  {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_SendGoal_Request__copy(
  const com2009_team65_2025__action__ExploreForward_SendGoal_Request * input,
  com2009_team65_2025__action__ExploreForward_SendGoal_Request * output)
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
  if (!com2009_team65_2025__action__ExploreForward_Goal__copy(
      &(input->goal), &(output->goal)))
  {
    return false;
  }
  return true;
}

com2009_team65_2025__action__ExploreForward_SendGoal_Request *
com2009_team65_2025__action__ExploreForward_SendGoal_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_SendGoal_Request * msg = (com2009_team65_2025__action__ExploreForward_SendGoal_Request *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Request));
  bool success = com2009_team65_2025__action__ExploreForward_SendGoal_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__ExploreForward_SendGoal_Request__destroy(com2009_team65_2025__action__ExploreForward_SendGoal_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__ExploreForward_SendGoal_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence__init(com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_SendGoal_Request * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__ExploreForward_SendGoal_Request *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__ExploreForward_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__ExploreForward_SendGoal_Request__fini(&data[i - 1]);
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
com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence__fini(com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence * array)
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
      com2009_team65_2025__action__ExploreForward_SendGoal_Request__fini(&array->data[i]);
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

com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence *
com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence * array = (com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence__destroy(com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence__are_equal(const com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence * lhs, const com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_SendGoal_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence__copy(
  const com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence * input,
  com2009_team65_2025__action__ExploreForward_SendGoal_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__ExploreForward_SendGoal_Request * data =
      (com2009_team65_2025__action__ExploreForward_SendGoal_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__ExploreForward_SendGoal_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__ExploreForward_SendGoal_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_SendGoal_Request__copy(
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
com2009_team65_2025__action__ExploreForward_SendGoal_Response__init(com2009_team65_2025__action__ExploreForward_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    com2009_team65_2025__action__ExploreForward_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__ExploreForward_SendGoal_Response__fini(com2009_team65_2025__action__ExploreForward_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

bool
com2009_team65_2025__action__ExploreForward_SendGoal_Response__are_equal(const com2009_team65_2025__action__ExploreForward_SendGoal_Response * lhs, const com2009_team65_2025__action__ExploreForward_SendGoal_Response * rhs)
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
com2009_team65_2025__action__ExploreForward_SendGoal_Response__copy(
  const com2009_team65_2025__action__ExploreForward_SendGoal_Response * input,
  com2009_team65_2025__action__ExploreForward_SendGoal_Response * output)
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

com2009_team65_2025__action__ExploreForward_SendGoal_Response *
com2009_team65_2025__action__ExploreForward_SendGoal_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_SendGoal_Response * msg = (com2009_team65_2025__action__ExploreForward_SendGoal_Response *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Response));
  bool success = com2009_team65_2025__action__ExploreForward_SendGoal_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__ExploreForward_SendGoal_Response__destroy(com2009_team65_2025__action__ExploreForward_SendGoal_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__ExploreForward_SendGoal_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence__init(com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_SendGoal_Response * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__ExploreForward_SendGoal_Response *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__ExploreForward_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__ExploreForward_SendGoal_Response__fini(&data[i - 1]);
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
com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence__fini(com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence * array)
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
      com2009_team65_2025__action__ExploreForward_SendGoal_Response__fini(&array->data[i]);
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

com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence *
com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence * array = (com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence__destroy(com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence__are_equal(const com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence * lhs, const com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_SendGoal_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence__copy(
  const com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence * input,
  com2009_team65_2025__action__ExploreForward_SendGoal_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__ExploreForward_SendGoal_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__ExploreForward_SendGoal_Response * data =
      (com2009_team65_2025__action__ExploreForward_SendGoal_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__ExploreForward_SendGoal_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__ExploreForward_SendGoal_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_SendGoal_Response__copy(
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
com2009_team65_2025__action__ExploreForward_GetResult_Request__init(com2009_team65_2025__action__ExploreForward_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    com2009_team65_2025__action__ExploreForward_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__ExploreForward_GetResult_Request__fini(com2009_team65_2025__action__ExploreForward_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

bool
com2009_team65_2025__action__ExploreForward_GetResult_Request__are_equal(const com2009_team65_2025__action__ExploreForward_GetResult_Request * lhs, const com2009_team65_2025__action__ExploreForward_GetResult_Request * rhs)
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
com2009_team65_2025__action__ExploreForward_GetResult_Request__copy(
  const com2009_team65_2025__action__ExploreForward_GetResult_Request * input,
  com2009_team65_2025__action__ExploreForward_GetResult_Request * output)
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

com2009_team65_2025__action__ExploreForward_GetResult_Request *
com2009_team65_2025__action__ExploreForward_GetResult_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_GetResult_Request * msg = (com2009_team65_2025__action__ExploreForward_GetResult_Request *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Request));
  bool success = com2009_team65_2025__action__ExploreForward_GetResult_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__ExploreForward_GetResult_Request__destroy(com2009_team65_2025__action__ExploreForward_GetResult_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__ExploreForward_GetResult_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence__init(com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_GetResult_Request * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__ExploreForward_GetResult_Request *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__ExploreForward_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__ExploreForward_GetResult_Request__fini(&data[i - 1]);
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
com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence__fini(com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence * array)
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
      com2009_team65_2025__action__ExploreForward_GetResult_Request__fini(&array->data[i]);
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

com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence *
com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence * array = (com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence__destroy(com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence__are_equal(const com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence * lhs, const com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_GetResult_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence__copy(
  const com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence * input,
  com2009_team65_2025__action__ExploreForward_GetResult_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__ExploreForward_GetResult_Request * data =
      (com2009_team65_2025__action__ExploreForward_GetResult_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__ExploreForward_GetResult_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__ExploreForward_GetResult_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_GetResult_Request__copy(
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
// #include "com2009_team65_2025/action/detail/explore_forward__functions.h"

bool
com2009_team65_2025__action__ExploreForward_GetResult_Response__init(com2009_team65_2025__action__ExploreForward_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!com2009_team65_2025__action__ExploreForward_Result__init(&msg->result)) {
    com2009_team65_2025__action__ExploreForward_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__ExploreForward_GetResult_Response__fini(com2009_team65_2025__action__ExploreForward_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  com2009_team65_2025__action__ExploreForward_Result__fini(&msg->result);
}

bool
com2009_team65_2025__action__ExploreForward_GetResult_Response__are_equal(const com2009_team65_2025__action__ExploreForward_GetResult_Response * lhs, const com2009_team65_2025__action__ExploreForward_GetResult_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // result
  if (!com2009_team65_2025__action__ExploreForward_Result__are_equal(
      &(lhs->result), &(rhs->result)))
  {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_GetResult_Response__copy(
  const com2009_team65_2025__action__ExploreForward_GetResult_Response * input,
  com2009_team65_2025__action__ExploreForward_GetResult_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  output->status = input->status;
  // result
  if (!com2009_team65_2025__action__ExploreForward_Result__copy(
      &(input->result), &(output->result)))
  {
    return false;
  }
  return true;
}

com2009_team65_2025__action__ExploreForward_GetResult_Response *
com2009_team65_2025__action__ExploreForward_GetResult_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_GetResult_Response * msg = (com2009_team65_2025__action__ExploreForward_GetResult_Response *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Response));
  bool success = com2009_team65_2025__action__ExploreForward_GetResult_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__ExploreForward_GetResult_Response__destroy(com2009_team65_2025__action__ExploreForward_GetResult_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__ExploreForward_GetResult_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence__init(com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_GetResult_Response * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__ExploreForward_GetResult_Response *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__ExploreForward_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__ExploreForward_GetResult_Response__fini(&data[i - 1]);
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
com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence__fini(com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence * array)
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
      com2009_team65_2025__action__ExploreForward_GetResult_Response__fini(&array->data[i]);
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

com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence *
com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence * array = (com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence__destroy(com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence__are_equal(const com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence * lhs, const com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_GetResult_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence__copy(
  const com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence * input,
  com2009_team65_2025__action__ExploreForward_GetResult_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__ExploreForward_GetResult_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__ExploreForward_GetResult_Response * data =
      (com2009_team65_2025__action__ExploreForward_GetResult_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__ExploreForward_GetResult_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__ExploreForward_GetResult_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_GetResult_Response__copy(
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
// #include "com2009_team65_2025/action/detail/explore_forward__functions.h"

bool
com2009_team65_2025__action__ExploreForward_FeedbackMessage__init(com2009_team65_2025__action__ExploreForward_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    com2009_team65_2025__action__ExploreForward_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!com2009_team65_2025__action__ExploreForward_Feedback__init(&msg->feedback)) {
    com2009_team65_2025__action__ExploreForward_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
com2009_team65_2025__action__ExploreForward_FeedbackMessage__fini(com2009_team65_2025__action__ExploreForward_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  com2009_team65_2025__action__ExploreForward_Feedback__fini(&msg->feedback);
}

bool
com2009_team65_2025__action__ExploreForward_FeedbackMessage__are_equal(const com2009_team65_2025__action__ExploreForward_FeedbackMessage * lhs, const com2009_team65_2025__action__ExploreForward_FeedbackMessage * rhs)
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
  if (!com2009_team65_2025__action__ExploreForward_Feedback__are_equal(
      &(lhs->feedback), &(rhs->feedback)))
  {
    return false;
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_FeedbackMessage__copy(
  const com2009_team65_2025__action__ExploreForward_FeedbackMessage * input,
  com2009_team65_2025__action__ExploreForward_FeedbackMessage * output)
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
  if (!com2009_team65_2025__action__ExploreForward_Feedback__copy(
      &(input->feedback), &(output->feedback)))
  {
    return false;
  }
  return true;
}

com2009_team65_2025__action__ExploreForward_FeedbackMessage *
com2009_team65_2025__action__ExploreForward_FeedbackMessage__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_FeedbackMessage * msg = (com2009_team65_2025__action__ExploreForward_FeedbackMessage *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_FeedbackMessage), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(com2009_team65_2025__action__ExploreForward_FeedbackMessage));
  bool success = com2009_team65_2025__action__ExploreForward_FeedbackMessage__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
com2009_team65_2025__action__ExploreForward_FeedbackMessage__destroy(com2009_team65_2025__action__ExploreForward_FeedbackMessage * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    com2009_team65_2025__action__ExploreForward_FeedbackMessage__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence__init(com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_FeedbackMessage * data = NULL;

  if (size) {
    data = (com2009_team65_2025__action__ExploreForward_FeedbackMessage *)allocator.zero_allocate(size, sizeof(com2009_team65_2025__action__ExploreForward_FeedbackMessage), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = com2009_team65_2025__action__ExploreForward_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        com2009_team65_2025__action__ExploreForward_FeedbackMessage__fini(&data[i - 1]);
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
com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence__fini(com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence * array)
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
      com2009_team65_2025__action__ExploreForward_FeedbackMessage__fini(&array->data[i]);
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

com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence *
com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence * array = (com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence *)allocator.allocate(sizeof(com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence__destroy(com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence__are_equal(const com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence * lhs, const com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_FeedbackMessage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence__copy(
  const com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence * input,
  com2009_team65_2025__action__ExploreForward_FeedbackMessage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(com2009_team65_2025__action__ExploreForward_FeedbackMessage);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    com2009_team65_2025__action__ExploreForward_FeedbackMessage * data =
      (com2009_team65_2025__action__ExploreForward_FeedbackMessage *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!com2009_team65_2025__action__ExploreForward_FeedbackMessage__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          com2009_team65_2025__action__ExploreForward_FeedbackMessage__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!com2009_team65_2025__action__ExploreForward_FeedbackMessage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
