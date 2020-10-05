from celery import Celery

app = Celery('proj',
        broker='amqp://admin:admin@localhost:5672',
        backend='amqp://admin:admin@localhost:5672',
             )

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)


if __name__ == '__main__':
    app.start()

