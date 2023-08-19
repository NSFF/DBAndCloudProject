# getting python base image
FROM python:3.8

# directory from where the local files will be copied to the image
# uncomment only for local use
#WORKDIR /home/nsff/School/DBAndCloud/DBAndCloudProject

ENV DB_READ_USER_PASS=${{secrets.DB_READ_USER_PASS}}

# copy local files to image
COPY requirements.txt src/* ./

# install extra libraries
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# execute scripts
CMD [ "python", "./main.py"]