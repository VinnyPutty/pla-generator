from main import compare_pla_layouts, generate_pla_layout
import timeit


def wrapper(func, *args, **kwargs):
    def wrapped_func():
        return func(*args, **kwargs)
    return wrapped_func


def benchmark_pla_layout_comparison(filename_1, filename_2):
    print(compare_pla_layouts(filename_1, filename_2))
    time_wrap = wrapper(compare_pla_layouts, filename_1, filename_2)
    print("Time elapsed: {}s".format(timeit.timeit(time_wrap, number=10000)))


# benchmark_pla_layout_comparison("../../pla_layout/4x4x16_pla_layout_output_25.lay",
#                                 "../../pla_layout/4x4x16_pla_layout_output_26.lay")
#
# benchmark_pla_layout_comparison("../../pla_layout/32x32x32_pla_layout_output_5.lay",
#                                 "../../pla_layout/32x32x32_pla_layout_output_5.lay")
#
# benchmark_pla_layout_comparison("../../pla_layout/1024x1024x1024_pla_layout_output_2.lay",
#                                 "../../pla_layout/1024x1024x1024_pla_layout_output_3.lay")
#
# benchmark_pla_layout_comparison("../../pla_layout/4096x4096x4096_pla_layout_output_0.lay",
#                                 "../../pla_layout/1024x1024x1024_pla_layout_output_3.lay")


# load_definitions()
# load_pla_codes(False)

# generate_pla_layout(True, "../../pla_codes/simple_pla_codes.pla")
# generate_pla_layout(True, "../../pla_codes/4x4x16_pla_codes.pla")
# generate_pla_layout(True, "../../pla_codes/5x32x256_with_duplicate_codes_pla_codes.pla")
generate_pla_layout(True, "../../pla_codes/31x31x31_pla_codes.pla")
# generate_pla_layout(True, "../../pla_codes/32x32x32_pla_codes.pla")
# generate_pla_layout(True, "../../pla_codes/32x32x256_pla_codes.pla")
# generate_pla_layout(True, "../../pla_codes/1024x1024x1024_pla_codes.pla")  # this takes some time on redstone
# generate_pla_layout(True, "../../pla_codes/1024x1024x4096_pla_codes.pla")  # this takes a long time on redstone
# generate_pla_layout(True, "../../pla_codes/4096x4096x4096_pla_codes.pla")  # this takes forever on redstone; it
# also requires about 6 GB of available memory

# wrapped = wrapper(generate_pla_layout, True, "../../pla_codes/1024x1024x1024_pla_codes.pla")  # for benchmarking
# print(timeit.timeit(wrapped, number=1) / 1)  # for benchmarking
# timeit_(generate_pla_layout) # doesn't work

# generate_pla_wires_layout_code_key() # NotImplementedException or NotImplementedWarning