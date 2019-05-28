from main import compare_pla_layouts
import timeit


def wrapper(func, *args, **kwargs):
    def wrapped_func():
        return func(*args, **kwargs)
    return wrapped_func


def benchmark_pla_layout_comparison(filename_1, filename_2):
    print(compare_pla_layouts(filename_1, filename_2))
    time_wrap = wrapper(compare_pla_layouts, filename_1, filename_2)
    print("Time elapsed: {}s".format(timeit.timeit(time_wrap, number=10000)))


benchmark_pla_layout_comparison("../../pla_layout/4x4x16_pla_layout_output_25.lay",
                                "../../pla_layout/4x4x16_pla_layout_output_26.lay")

benchmark_pla_layout_comparison("../../pla_layout/32x32x32_pla_layout_output_5.lay",
                                "../../pla_layout/32x32x32_pla_layout_output_5.lay")

benchmark_pla_layout_comparison("../../pla_layout/1024x1024x1024_pla_layout_output_2.lay",
                                "../../pla_layout/1024x1024x1024_pla_layout_output_3.lay")

benchmark_pla_layout_comparison("../../pla_layout/4096x4096x4096_pla_layout_output_0.lay",
                                "../../pla_layout/1024x1024x1024_pla_layout_output_3.lay")
