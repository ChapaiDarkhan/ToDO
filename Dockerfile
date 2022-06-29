FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /app
ADD . /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
