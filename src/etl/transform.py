import requests
import pathlib
import pandas as pd
import jdatetime
from tqdm import tqdm
from loguru import logger
from src.utils import extract_date_from_file_path

# logger.add("transform.log", level="INFO", format="{time} {level} {message}", rotation="1 day", retention="7 days")

def change_format_to_csv(stage_path, datalake_path):
    
    try:
    
        df = pd.read_excel(stage_path, skiprows=2)
        date = extract_date_from_file_path(str(stage_path))
        df["تاریخ شمسی"] = date
        df["تاریخ میلادی"] = jdatetime.date.togregorian(jdatetime.datetime.strptime(date, format="%Y-%m-%d"))
        df["تاریخ میلادی"] = pd.to_datetime(df["تاریخ میلادی"])  
        
        if df.shape != 0:
            df.to_csv(datalake_path,encoding="utf-8", index=False)
            logger.info(f"format changed successfully!")
        else:
            logger.info(f"{stage_path} empty!")
    except Exception as e:
        logger.error(f" We have a error: {e}")

