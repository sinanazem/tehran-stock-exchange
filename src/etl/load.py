import pathlib
from loguru import logger
from src.etl.transform import change_format_to_csv


def change_format_store(stage_path, delete_excel=False):
    
    excel_file_path_list = pathlib.Path(stage_path).resolve()
    
    datalake_dir = excel_file_path_list.parent / 'datalake'
    datalake_dir.mkdir(parents=True, exist_ok=True)
    try:
        for excel_file_path in excel_file_path_list.glob('*'):
            print(excel_file_path)
            csv_file_path = datalake_dir /  (excel_file_path.stem + '.csv')

            change_format_to_csv(excel_file_path, csv_file_path)

            if delete_excel:

                # Check if the file exists before attempting to delete
                if excel_file_path.exists():
                    try:
                        # Delete the file
                        excel_file_path.unlink()
                        print(f"{excel_file_path} has been deleted successfully.")
                    except Exception as e:
                        print(f"Error deleting {excel_file_path}: {e}")
                else:
                    print(f"The file {excel_file_path} does not exist.")
    except Exception as e:
        logger.error(f" We have a error: {e}")


if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--stagedir',help='Stage Directory file Path')
    parser.add_argument('-d','--delete',help='Delete Excel Files')
    args = parser.parse_args()
    
    change_format_store(args.stagedir, bool(args.delete))
