FROM alpine:3.23

ENV TZ=Asia/Shanghai

RUN apk add --no-cache tzdata nginx curl fcgiwrap && \
    rm -rf /var/cache/apk/* /tmp/*

COPY --chmod=755 ./rootfs /

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]