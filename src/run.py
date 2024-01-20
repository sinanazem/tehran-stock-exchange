from src.etl import extract, transform, load 
from src.analysis import stock_analysis

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-s','--startdate',help='Start Date Tehran Exchange Market')
parser.add_argument('-e','--enddate',help='End Date Tehran Exchange Market')
parser.add_argument('-d','--delete',help='Delete Excel Files')
args = parser.parse_args()


extract.download_tehran_stock_exchange_files(args.startdate, args.enddate)
load.change_format_store("src/stage/", bool(args.delete))

