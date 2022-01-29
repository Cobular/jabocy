FROM gorialis/discord.py:3.10-alpine-minimal

COPY ./test.py ./test.py

CMD [ "python", "./test.py" ]