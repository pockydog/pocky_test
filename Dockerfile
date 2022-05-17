#FROM mysql
#MAINTAINER vickychen@gillygaming888.com
#LABEL version = '1.0'
#
#ARG PRODUCT_NAME='app'
#
#COPY requirments.txt .
#
#RUN pip3 --no-cache-dir install -r requirements.txt
#
#CDM ['python', 'run']