#!/bin/bash
python ./src/ex1_0_setup.py
python ./src/ex1_1_setup.py
python ./src/python_version.py
echo "List of installed packages:"
pip list
# start the cron service
cron -f

# follow the logfile to keep the container running
tail -f /Exercise1/src/output.log