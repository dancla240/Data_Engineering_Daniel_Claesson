# Specifying Docker Hub image to start from
FROM python:3.12.3-bullseye

# Specify the working directory inside the container
WORKDIR /Exercise1

# Copy application files into the container, Python and Bash
COPY ./src/ex1_0_setup.py ./src/ex1_0_setup.py
COPY ./src/ex1_1_setup.py ./src/ex1_1_setup.py
COPY ./src/python_version.py ./src/python_version.py
COPY ./src/cron.py ./src/cron.py
COPY ./run.sh ./run.sh
COPY crontab /etc/cron.d/mycron

# Install dependencies, Python and Bash
RUN pip install matplotlib plotly_express pandas numpy dash scikit-learn
RUN apt-get update && apt-get install -y tree cron nano

# Ensure cron.py is readable by the cron daemon
RUN chmod 644 /Exercise1/src/cron.py

# Make run.sh executable
RUN chmod +x ./run.sh

# Give execution rights to the cron job (0644 handlar om permissions)
RUN chmod 0644 /etc/cron.d/mycron

# Add the Cron job
# RUN crontab -l | { cat; echo "*/1 * * * * python /Exercise1/src/cron.py >> /Exercise1/src/output.log"; } | crontab -
#RUN crontab crontab
RUN crontab /etc/cron.d/mycron

# Create the log file to be able to run the tail
RUN touch /Exercise1/src/output.log


# Set the default command to run the run.sh script
CMD ["./run.sh"]
#CMD ["python","src/ex1_0_setup.py"]