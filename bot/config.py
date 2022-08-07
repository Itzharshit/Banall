import os

class Config:
    TELEGRAM_TOKEN=os.environ['TELEGRAM_TOKEN']
#fuck off
    TELEGRAM_TOKEN1=os.environ['TELEGRAM_TOKEN1']
    TELEGRAM_TOKEN2=os.environ['TELEGRAM_TOKEN2']
    TELEGRAM_TOKEN3=os.environ['TELEGRAM_TOKEN3']
    TELEGRAM_TOKEN4=os.environ['TELEGRAM_TOKEN4']
    TELEGRAM_TOKEN5=os.environ['TELEGRAM_TOKEN5']
#its dick😂
    SUDOS=os.environ['SUDOS']
    TELEGRAM_APP_HASH=os.environ['TELEGRAM_APP_HASH']
    TELEGRAM_APP_ID=int(os.environ['TELEGRAM_APP_ID'])
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
#it sucks
    if not TELEGRAM_TOKEN1:
        raise ValueError('TELEGRAM BOT TOKEN 1 not set')
    if not TELEGRAM_TOKEN2:
        raise ValueError('TELEGRAM BOT TOKEN 2 not set')
    if not TELEGRAM_TOKEN3:
        raise ValueError('TELEGRAM BOT TOKEN  3 not set')
    if not TELEGRAM_TOKEN4:
        raise ValueError('TELEGRAM BOT TOKEN 4 not set')
    if not TELEGRAM_TOKEN5:
        raise ValueError('TELEGRAM BOT TOKEN 5 not set')
