from telegram import ParseMode
import arrow
import time
from datetime import datetime, tzinfo, timedelta, timezone
import logging
import json
import Constants as keys
from telegram.ext import *
import requests
print('Bot started')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

###########################################HELPER FUNCTIONS#####################################


def datetime_from_utc_to_local(utc_datetime):
    utc = datetime.strptime(utc_datetime, "%Y-%m-%dT%H:%M:%S.%fZ")
    return utc


def utc2local(utc):
    print(utc)
    return arrow.get(utc).to(('Asia/Kolkata')).format('HH:mm:ss ZZ')

###########################################BOT FUNCTIONS########################################


def start_command(update, context):
    update.message.reply_text(
        "I am the all mighty watcher 💪. ‍My work is to simply remind you of coding competetion(basically all) schedules in IST.\n Do /help for my commands.")


def help_command(update, context):
    update.message.reply_text(
        'How to use me?\n1. /codeforces\n2. /atcoder\n3. /codechef\n4. /kickstart\n5. /leetcode\n6. /all')


def codeforces(update, context):
    response = requests.get('https://kontests.net/api/v1/codeforces.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d4 = utc2local(start)
        d2 = utc2local(end)
        new_format = "%Y-%m-%d"
        info += ("<a href=\""+x["url"]+"\">"+x["name"]+"</a>"+"\nStart: "+(d1.strftime("%A %d. %B %Y")) + "  " + str(d4) +
                 "\nEnd: "+str(d2)+"hr\n\n")
    update.message.reply_text(
        info, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def codechef(update, context):
    response = requests.get('https://kontests.net/api/v1/code_chef.json')
    data = response.json()
    info = ""
    contains = ["Rated", "SnackDown", "Lunchtime", "Cook-Off"]
    for x in data:
        if any(word in contains for word in x["name"]):
            start = x["start_time"]
            end = x["end_time"]
            d1 = datetime_from_utc_to_local(start)
            d4 = utc2local(start)
            d2 = utc2local(end)
            new_format = "%Y-%m-%d"
            info += ("<a href=\""+x["url"]+"\">"+x["name"]+"</a>"+"\nStart: "+(d1.strftime("%A %d. %B %Y")) + "  " + str(d4) +
                     "\nEnd: "+str(d2)+"hr\n\n")
    update.message.reply_text(
        info, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def leetcode(update, context):
    response = requests.get('https://kontests.net/api/v1/leet_code.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d4 = utc2local(start)
        d2 = utc2local(end)
        new_format = "%Y-%m-%d"
        info += ("<a href=\""+x["url"]+"\">"+x["name"]+"</a>"+"\nStart: "+(d1.strftime("%A %d. %B %Y")) + "  " + str(d4) +
                 "\nEnd: "+str(d2)+"hr\n\n")
    update.message.reply_text(
        info, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def kickstart(update, context):
    response = requests.get('https://kontests.net/api/v1/kick_start.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d4 = utc2local(start)
        d2 = utc2local(end)
        new_format = "%Y-%m-%d"
        info += ("<a href=\""+x["url"]+"\">"+x["name"]+"</a>"+"\nStart: "+(d1.strftime("%A %d. %B %Y")) + "  " + str(d4) +
                 "\nEnd: "+str(d2)+"hr\n\n")
    update.message.reply_text(
        info, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def atcoder(update, context):
    response = requests.get('https://kontests.net/api/v1/at_coder.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d4 = utc2local(start)
        d2 = utc2local(end)
        new_format = "%Y-%m-%d"
        info += ("<a href=\""+x["url"]+"\">"+x["name"]+"</a>"+"\nStart: "+(d1.strftime("%A %d. %B %Y")) + "  " + str(d4) +
                 "\nEnd: "+str(d2)+"hr\n\n")
    update.message.reply_text(
        info, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def hackerearth(update, context):
    response = requests.get('https://kontests.net/api/v1/hacker_earth.json')
    data = response.json()
    info = ""
    for x in data:
        start = x["start_time"]
        end = x["end_time"]
        d1 = datetime_from_utc_to_local(start)
        d4 = utc2local(start)
        d2 = utc2local(end)
        new_format = "%Y-%m-%d"
        info += ("<a href=\""+x["url"]+"\">"+x["name"]+"</a>"+"\nStart: "+(d1.strftime("%A %d. %B %Y")) + "  " + str(d4) +
                 "\nEnd: "+str(d2)+"hr\n\n")
    update.message.reply_text(
        info, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def all_contest(update, context):
    info = ""
    contest_name = ["codeforces", "at_coder",
                    "code_chef", "leet_code", "kick_start"]
    for i in contest_name:
        print(i)
        response = requests.get('https://kontests.net/api/v1/'+i+".json")
        data = response.json()
        for x in data:
            print(x["in_24_hours"])
            if (x["in_24_hours"] == "Yes"):
                start = x["start_time"]
                end = x["end_time"]
                d1 = datetime_from_utc_to_local(start)
                d4 = utc2local(start)
                d2 = utc2local(end)
                new_format = "%Y-%m-%d"
                info += ("<a href=\""+x["url"]+"\">"+x["name"]+"</a>"+"\nStart: "+(d1.strftime("%A %d. %B %Y")) + "  " + str(d4) +
                         "\nEnd: "+str(d2)+"hr\n\n")
    update.message.reply_text(
        info, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def error_handler(update, context):
    print(context.error)


###########################################BOT FUNCTIONS########################################


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
