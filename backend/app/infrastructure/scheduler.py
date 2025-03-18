from apscheduler.schedulers.background import BackgroundScheduler
import asyncio
from app.services.tasks import scheduled_stock_analysis

scheduler = BackgroundScheduler()

# Wrap the async function inside a sync function
def run_analysis():
    print("scheduler running")
    asyncio.run(scheduled_stock_analysis())

# Schedule the job to run every hour
#hours=1
#minutes=5
scheduler.add_job(run_analysis, "interval", seconds=5)
scheduler.start()
