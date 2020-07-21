def success(rec):
  print('> message delivered to %s with partition %d and offset %d' % (rec.topic, rec.partition, rec.offset))

def error(exception):
  # handle exception
  print('> message unsent with exception:', exception)