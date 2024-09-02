# 
FROM python:3.12.3

# 
RUN mkdir /Menti_app
# 

WORKDIR /Menti_app

# 
COPY requirements.txt .

# 
RUN pip install -r requirements.txt

# 
COPY . .

# 
RUN chmod a+x docker/*.sh

#CMD gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000