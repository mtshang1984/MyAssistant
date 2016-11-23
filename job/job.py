import json

from local_windows.local_windows import LocalWindows


class Job:
    today =''
    job_index=0
    job_name=''
    filename=''

    def __init__(self,filename):
        self.filename=filename
        json_content=json.load(open(filename,'r',encoding="utf-8"))
        # print(json_content)
        self.today=json_content['today']
        self.job_index=json_content['job_index']
        work_plan=json_content['work_plan']

        for index_in_work_plan in range(0,len(work_plan)):
            #找到当天的任务清单
            if(self.today==work_plan[index_in_work_plan]['date']):
                job_list=work_plan[index_in_work_plan]['job_list']
                for index_in_job_list in(0,len(job_list)):
                    if(self.job_index==job_list[index_in_job_list]['job_index']):
                        self.job_name=job_list[index_in_job_list]['job_name']
                        break


    def run_today_job(self):
        if(self.today=="2016.11.23"):
            if(self.job_name=="看一些新闻"):
                local_windows=LocalWindows()
                local_windows.browse_webpage('news.baidu.com')