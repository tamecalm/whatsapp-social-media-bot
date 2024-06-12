from flask_apscheduler import APScheduler
from app.social_media import post_to_social_media

scheduler = APScheduler()

def schedule_post(time, content):
    job_id = f"post_{time}"
    scheduler.add_job(id=job_id, func=post_to_social_media, trigger='date', run_date=time, args=[content])
