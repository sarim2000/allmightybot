import arrow
import time
from datetime import datetime, tzinfo, timedelta, timezone
import logging
import json
import Constants as keys
from telegram.ext import *
import requests
print('Bot started')


def start_command(update, context):
    update.message.reply_text("Type")


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def help_command(update, context):
    update.message.reply_text('Hello')


def datetime_from_utc_to_local(utc_datetime):
    utc = datetime.strptime(utc_datetime, "%Y-%m-%dT%H:%M:%S.%fZ")
    return utc


def utc2local(utc):
    print(utc)
    return arrow.get(utc).to(('Asia/Kolkata')).format('YYYY-MM-DD HH:mm:ss ZZ')


def codeforces(update, context):
    response = requests.get('https://kontests.net/api/v1/codeforces.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime.strptime(utc_datetime, "%Y-%m-%dT")
        print(d1.weekday())
        d4 = utc2local(start)
        d2 = utc2local(end)
        new_format = "%Y-%m-%d"
        info += (x["name"]+"\nStart: "+str(d4) +
                 "\nEnd: "+str(d2)+"\nRegister: "+x["url"] + "\n\n")
    update.message.reply_text(info)


def codechef(update, context):
    response = requests.get('https://kontests.net/api/v1/code_chef.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d2 = datetime_from_utc_to_local(end)
        new_format = "%Y-%m-%d"
        info += (x["name"]+"\nStart: "+str(d1) +
                 "\nEnd: "+str(d2)+"\nRegister: "+x["url"] + "\n\n")
    update.message.reply_text(info)


def leetcode(update, context):
    response = requests.get('https://kontests.net/api/v1/leet_code.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d2 = datetime_from_utc_to_local(end)
        new_format = "%Y-%m-%d"
        info += (x["name"]+"\nStart: "+str(d1) +
                 "\nEnd: "+str(d2)+"\nRegister: "+x["url"] + "\n\n")
    update.message.reply_text(info)


def kickstart(update, context):
    response = requests.get('https://kontests.net/api/v1/kick_start.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d2 = datetime_from_utc_to_local(end)
        new_format = "%Y-%m-%d"
        info += (x["name"]+"\nStart: "+str(d1) +
                 "\nEnd: "+str(d2)+"\nRegister: "+x["url"] + "\n\n")
    update.message.reply_text(info)


def atcoder(update, context):
    response = requests.get('https://kontests.net/api/v1/at_coder.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d2 = datetime_from_utc_to_local(end)
        new_format = "%Y-%m-%d"
        info += (x["name"]+"\nStart: "+str(d1) +
                 "\nEnd: "+str(d2)+"\nRegister: "+x["url"] + "\n\n")
    update.message.reply_text(info)


def hackerearth(update, context):
    response = requests.get('https://kontests.net/api/v1/hacker_earth.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d2 = datetime_from_utc_to_local(end)
        new_format = "%Y-%m-%d"
        info += (x["name"]+"\nStart: "+str(d1) +
                 "\nEnd: "+str(d2)+"\nRegister: "+x["url"] + "\n\n")
    update.message.reply_text(info)


def all_contest(update, context):
    contest_name = ["codeforces", "at_coder",
                    "code_chef", "leet_code", "kick_start"]
    for i in contest_name:
        info = ""

        response = requests.get('https://kontests.net/api/v1/'+i+".json")
        data = response.json()
        for x in data:
            if (x["in_24_hours"] == "Yes"):
                start = x["start_time"]
                end = x["end_time"]
                d1 = datetime_from_utc_to_local(start)
                d2 = datetime_from_utc_to_local(end)
                new_format = "%Y-%m-%d"
                info += (x["name"]+"\nStart: "+str(d1) +
                         "\nEnd: "+str(d2)+"\nRegister: "+x["url"] + "\n\n")
        update.message.reply_text(info)


def error_handler(update, context):
    print(context.error)


def main():
    updater = Updater(keys.API_KEY, use_context="true")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("codeforces", codeforces))
    dp.add_handler(CommandHandler("codechef", codechef))
    dp.add_handler(CommandHandler("atcoder", atcoder))
    dp.add_handler(CommandHandler("hackerearth", hackerearth))
    dp.add_handler(CommandHandler("kickstart", kickstart))
    dp.add_handler(CommandHandler("all", all_contest))
    dp.add_handler(CommandHandler("leetcode", leetcode))

    dp.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()


main()
