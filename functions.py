import sys
import logging
import pymysql
import os

def open_rds_connection():
    # rds settings
    user_name = os.environ['USER_NAME']
    password = os.environ['PASSWORD']
    rds_host = os.environ['RDS_HOST']
    db_name = os.environ['DB_NAME']
    # user_name = 'root'
    # password = 'Smiley9201a21fs'
    # rds_host = 'localhost'
    # db_name = 'terp'

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # create the database connection outside of the handler to allow connections to be
    # re-used by subsequent function invocations.
    try:
        conn = pymysql.connect(host=rds_host, user=user_name, passwd=password, db=db_name, connect_timeout=5)
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit()

    logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
    return conn