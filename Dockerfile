FROM python:3.6-alpine3.6

RUN apk --no-cache add curl

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

HEALTHCHECK --interval=6s --timeout=2s CMD curl --fail http://localhost:5000/health || exit 1

ENTRYPOINT ["python"]

EXPOSE 5000

CMD ["app.py"]
