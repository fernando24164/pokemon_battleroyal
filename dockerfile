FROM python:3.7-slim

COPY app app

CMD python -c 'python signal; signal.pause()'