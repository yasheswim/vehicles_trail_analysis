from fastapi import FastAPI
from functions import merge_trails_trip_df
from hard_coded_variables import EXCEL_REPORT_PATH
from pydantic import BaseModel
from typing import Optional
import traceback


app = FastAPI()

@app.get("/api/generate_report")
def api_endpoint(start_time:Optional[int] = None, end_time:Optional[int] = None):
    try:
        result = merge_trails_trip_df(start_time=start_time,end_time=end_time)
        if isinstance(result,Exception):
            raise result
        result.to_excel(EXCEL_REPORT_PATH,index=False)
        return {"message": "Report generated successfully", "file_path": EXCEL_REPORT_PATH}
    except Exception as e:
        return {"message": "Error occurred while generating the report", "error": str(e)}


