FROM python:3.9
WORKDIR /app
COPY task_8.py /app/task_8
ENTRYPOINT [ "python", "task_8" ]