FROM python
MAINTAINER vickychen@gillygaming888.com
LABEL version = '1.0'

ARG PRODUCT_NAME='app'
RUN mkdir -p /${PRODUCT_NAME}
WORKDIR /${PRODUCT_NAME}


#COPY src /app
COPY src .
WORKDIR /app
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt