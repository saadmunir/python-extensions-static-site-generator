from ssg import hooks

import time

start_time = None
total_written = 0

@hooks.event("start_build")
def start_build():
    global start_time
    start_time = time()

@hooks.event("written")
def written():
    global total_written
    total_written = total_written + 1

@hooks.event("stats")
def stats():
    final_time = time - start_time
    average = final_time/ total_written
    if average <0:
        return "Error"
    report = r"Converted: {}, Time: {:.2f} sec , Avg: {:.4f} sec/file"
    print(report.format(total_written, final_time, average))