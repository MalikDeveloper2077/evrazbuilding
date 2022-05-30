FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

COPY . /code/
RUN pip install -r /code/requirements.txt
WORKDIR /code

# RUN chmod +x /code/entrypoint.sh
RUN ["chmod", "+x", "/code/entrypoint.sh"]
# ENTRYPOINT [ "/code/entrypoint.sh" ]
