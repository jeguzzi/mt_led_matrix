cmake_minimum_required(VERSION 2.8.3)
project(mt_led_matrix)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

add_message_files(
  FILES
  Buffer.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(CATKIN_DEPENDS  std_msgs  message_runtime)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
