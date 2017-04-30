import logging
from threading import Thread
import requests
import os
import io
from time import sleep
from slackclient import SlackClient
import CmdQueue
import elMsg
from Drivers.ServoEnums import *
from MsgServo import *
from MsgPic import *
import os
PIC_COMMANDS = ["take"]
SERVO_COMMANDS= ["open", "close", "reset"]

PIC_PATH = "sammypic.png"

class SlackComms(object):
    """interface to work with slack"""

    log = logging.getLogger('SlackComms')
    READ_WEBSOCKET_DELAY = 1

    def PushPic(self, filepath):
        SlackComms.log.debug("cwd {}".format(os.getcwd()))
        self.upload_file(filepath, filepath, self.BOT_TOKEN, self.MyChannel, "uploaded pic" )

    def upload_file(self, filename, path, token, channels, title):
        '''
        upload a long text as a file
        '''
        ff = open(path, 'rb').read()
        SlackComms.log.debug("Length is ", len(ff))
        ret = self.slack_client.api_call("files.upload", 
                                         filename=filename, 
                                         channels=channels,
                                         title=title,
                                         filetype="image/png",
                                         file=ff)

        if not 'ok' in ret or not ret['ok']:
            # error
            SlackComms.log.error('fileUpload failed %s', ret['error'])

    def add_attachment(self, filename, path, token, channels, title):
        image_url = "https://files.slack.com/files-pri/T3URT3HBL-F52JD9H5E/untitled.png"
        attachments = attachments = [{"title": "Cat", "image_url": image_url}]
            
        slack_client.api_call("chat.postMessage", 
                                channel=channel, 
                                text='postMessage test',
                                as_user=True,
                                attachments=attachments)

    def handle_command(self, command, channel):
        """
            Receives commands directed at the bot and determines if they
            are valid commands. If so, then acts on the commands. If not,
            returns back what it needs for clarification.
        """
        self.MyChannel = channel
        if(any(word in command for word in SERVO_COMMANDS)):
            if(command.lower().startswith("open")):
                cmsg = MsgElServo(command, ServoAction.Open, "E1")
            elif(command.lower().startswith("close")):
                cmsg = MsgElServo(command, ServoAction.Close, "E1")            
            elif(command.lower().startswith("reset")):
                cmsg = MsgElServo(command, ServoAction.ServoReset, "*")            

            self.CommandQueue.addCommand(cmsg)
            self.slack_client.api_call("chat.postMessage", channel=channel,
                        text="Command Running", as_user=True)
        elif(any(word in command for word in PIC_COMMANDS)):
            cmsg = MsgPic("custom name", command, PIC_PATH)
            self.CommandQueue.addCommand(cmsg)
            self.slack_client.api_call("chat.postMessage", channel=channel,
                        text="Command Running", as_user=True)

        else:
            response = "Unknown command >" + command + "<"
            self.slack_client.api_call("chat.postMessage", channel=channel,
                        text=response, as_user=True)


    def parse_slack_output(self, slack_rtm_output):
        """
            The Slack Real Time Messaging API is an events firehose.
            this parsing function returns None unless a message is
            directed at the Bot, based on its ID.
        """
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and self.AT_BOT in output['text']:
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(self.AT_BOT)[1].strip().lower(), \
                           output['channel']
        return None, None

    def __init__(self, cmdqueue):
        SlackComms.log.info("SlackComms init")
        self.CommandQueue = cmdqueue
        self.MyChannel = ""
        #this can be set in windows Environment variables (make sure to logout to apply)
        #or can be set in linux: 
        if(("SLACK_BOT_TOKEN" in os.environ) and ("SLACK_BOT_UID" in os.environ)):
            self.BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
            self.BOT_UID = os.environ.get("SLACK_BOT_UID")
            self.AT_BOT = "<@" + self.BOT_UID + ">"
            self.slack_client = SlackClient(self.BOT_TOKEN)
        else:
            log.critical('NO private SLACK_BOT_TOKEN found')
            log.critical('can be setup by: windows - create Environment variable')
            log.critical('               : linux - export SLACK_BOT_TOKEN=...')


    def start(self):
    
        SlackComms.log.info('SlackComms Starting')
    
        self.thread = Thread(target = self.slackProcessor, args = (10, ))
    
        self.thread.start()
    
        SlackComms.log.info('SlackComms Starting... complete')
    
    def stop(self):
        self.Running = False
        self.myq.put("e")

    def slackProcessor(self, args):
        SlackComms.log.info("slackProcessor entered")

        self.Running = True
        
        self.BOT_NAME = 'semmy'
    
        if(self.BOT_TOKEN != None and self.BOT_UID != None):
        
            api_call = self.slack_client.api_call("users.list")
            if api_call.get('ok'):
                # retrieve all users so we can find our bot
                users = api_call.get('members')
                for user in users:
                    if 'name' in user and user.get('name') == self.BOT_NAME:
                        print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
            else:
                SlackComms.log.warn("could not find bot user with the name " + self.BOT_NAME)

            READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
            if self.slack_client.rtm_connect():
                SlackComms.log.info("StarterBot connected and running!")
                while self.Running:
                    command, channel = self.parse_slack_output(self.slack_client.rtm_read())
                    
                    if command and channel:
                        self.handle_command(command, channel)
                        sleep(self.READ_WEBSOCKET_DELAY)
            else:
                SlackComms.log.error("Connection failed. Invalid Slack token or bot ID?")
