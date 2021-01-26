FROM python:3.6.7 as base
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .


###############
# Debugger
###############
FROM base as debugger
RUN pip install debugpy
ENTRYPOINT [ "python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m" ]

###############
# primary
###############
FROM base as primary

CMD [ "python", "app.py" ]