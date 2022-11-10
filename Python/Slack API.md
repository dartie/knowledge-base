# Slack API

## pyslack

```python
def send_slack_message(text, receiver, INCOMING_WEB_HOOK, title=None, title_link=None, style=None):
  if title is None:
      title = text

  CHANNEL = receiver

  # Create a new instance.
  logging = slackpy.SlackLogger(INCOMING_WEB_HOOK, CHANNEL, USER_NAME, ICON_URL)

  # You can set a log level. The default level is INFO.
  logging.set_log_level(slackpy.LogLv.DEBUG) # Or logging.set_log_level(10)

  # Minimum Parameter
  # logging = slackpy.SlackLogger(INCOMING_WEB_HOOK)

  # Simple Usage
  logging.info('INFO Message')
  
  # LogLevel's only required parameter is "message", all others are optional.
  
  # LogLevel: DEBUG
  logging.debug(message='DEBUG Message', title='DEBUG Title', fields='')
  
  # LogLevel: INFO
  logging.info(message='INFO Message', title='INFO Title', fields='')
  
  # LogLevel: WARN
  logging.warn(message='WARN Message', title='WARN Title', fields='')
  
  # LogLevel: ERROR
  logging.error(message='ERROR Message', title='ERROR Title', fields='')
  
  # LogLevel: CUSTOM
  logging.message(message='CUSTOM Message', title='CUSTOM Title', color='good',
                  fields=[{"title": "CUSTOM", "value": "test", "short": True}],
                  log_level=40)

  # Title Link (New v2.1.0)
  if style == 'error':
      logging.error(message=text, title=title, title_link=title_link)
  elif style == 'message':
      logging.message(message=text, title=title, title_link=title_link)
  elif style == 'warn':
      logging.warn(message=text, title=title, title_link=title_link)
  elif style == 'info':
      logging.info(message=text, title=title, title_link=title_link)
  else:  # debug
      logging.debug(message=text, title=title, title_link=title_link)

```