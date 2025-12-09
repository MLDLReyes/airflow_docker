FROM apache/airflow:2.5.1
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt

# FROM apache/airflow:2.5.1

# USER airflow
# COPY requirements.txt .

# RUN pip install --user --upgrade pip \
#     && pip install --user --no-cache-dir -r requirements.txt