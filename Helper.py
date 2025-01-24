from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink, Callback, EMPTY_KEYBOARD, BaseStateGroup
from vkbottle import GroupTypes, GroupEventType , PhotoMessageUploader
from vkbottle.bot import Bot, Message
from vkbottle.user import User
import asyncio
import re
import time
from io import BytesIO
import requests
from flask import Flask
import threading
import os
import ssl
import aiohttp
import logging
from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart

l
