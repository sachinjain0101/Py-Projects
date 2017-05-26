from openpyxl import Workbook
from colexp import Vars
from colexp import getAppLogger
import openpyxl
import threading
import os
import pyodbc
import sys
import time

logger = getAppLogger(__name__)

def seperator():
    logger.info("*" * 60)
    
# simple log test
seperator()
logger.info("starting... " + __name__ + " " + Vars.APP_VERSION)
seperator()
