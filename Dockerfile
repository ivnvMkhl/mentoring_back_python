# 
FROM python:3.12.3

# 
RUN mkdir /mentor_hub_app
# 

WORKDIR /mentor_hub_app

# 
COPY requirements.txt .

# 
RUN pip install -r requirements.txt

# 
COPY . .

# 
RUN chmod a+x bin/*.sh