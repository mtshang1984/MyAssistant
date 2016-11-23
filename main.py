import os

from job.job import Job
from local_windows.local_windows import LocalWindows

if __name__=='__main__':
    job=Job('input.json')
    job.run_today_job()