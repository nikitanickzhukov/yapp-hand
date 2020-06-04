project(id)

add_executable(ps-id main.cpp)

target_link_libraries(ps-id
        peval
        penum
        ${Boost_LIBRARIES}
)
