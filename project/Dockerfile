FROM python:3.10

RUN mkdir /src
COPY src src
WORKDIR /src

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /src/
RUN poetry install -n --no-root

EXPOSE 5000
ENTRYPOINT ["python3", "/src/mainApi.py"]