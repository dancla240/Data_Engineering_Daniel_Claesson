FROM python:3.12.3-bullseye

WORKDIR /Exercise1

COPY ./src/ex1_0_setup.py ./src/ex1_0_setup.py
COPY ./src/ex1_1_setup.py ./src/ex1_1_setup.py
COPY ./src/python_version.py ./src/python_version.py
COPY ./run.sh ./run.sh

RUN pip install matplotlib plotly_express pandas numpy dash scikit-learn

RUN chmod +x run.sh

#CMD ["python","src/ex1_0_setup.py"]
CMD ["./run.sh"]
# asajad la in en bash här, sedan en bash i filsystemet, i bashfilen finns sedan flera saker