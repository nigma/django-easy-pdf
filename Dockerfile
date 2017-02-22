FROM python:3.6

LABEL github="https://github.com/nigma/django-easy-pdf"

ENV PYTHONUNBUFFERED 1
ENV LANG=en_US.UTF-8
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on

RUN mkdir -p /app /static
WORKDIR /app

RUN set -eux \
    && DEPS=' \
        bash \
        gettext \
        libcairo2 \
        libffi-dev \
        libpango1.0-0 \
        libgdk-pixbuf2.0-0 \
        libxml2-dev \
        libxslt1-dev \
        shared-mime-info \
    ' \
    && apt-get update \
    && apt-get install -y --no-install-recommends $DEPS \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN set -eux \
    && pip3 install --no-cache-dir -U pip setuptools \
    && pip3 install --no-cache-dir --timeout 1000 -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "demo.py"]
