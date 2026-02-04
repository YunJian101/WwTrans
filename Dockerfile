FROM docker.1ms.run/alpine:3.23

ENV TZ=Asia/Shanghai

RUN apk add --no-cache tzdata nginx curl fcgiwrap dos2unix && \
    rm -rf /var/cache/apk/* /tmp/*

COPY ./rootfs /

RUN chmod +x /entrypoint.sh && \
    chmod +x /app/web/getip.cgi && \
    dos2unix /entrypoint.sh && \
    dos2unix /app/web/getip.cgi

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]