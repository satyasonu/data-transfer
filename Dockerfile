FROM tiangolo/uvicorn-gunicorn:python3.9-alpine3.14
LABEL maintainer="Satyabrata Sahoo <sbssunu1@gmail.com>"

COPY ./app /app
COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir -r /api/requirements.txt

ENV PYTHONPATH=/app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["uvicorn"]

# CMD ["api.main:app", "--host", "0.0.0.0", "--port", "3000"]

CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "./app/log.ini"]