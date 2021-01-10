# VSinder Bot

<img src="./readme-assets/logo.png" align="right" alt="Logo by 3n3a" width="120" height="178">

VSinder Bot is a bot written for the VSinder Dating Platform. It's built up from reverse engineering the API Calls the VSinder App makes in iOS.

* Supports swiping on people
* Displaying Users Info
* Messaging your Matches

<p align="center">
  <img src="./readme-assets/screen1.png" alt="The Bot in Action" width="738">
</p>

## Why should you use VSinder Bot

The answer is very simple, because it makes using VSinder so much easier :). Imagine you have work but you don't want your programmer dating life to stop, so what do you do? Well you reverse engineer VSinder, or at least part of it and make a bot that runs until there's nothing more to swipe.

## How It Works

1. VSinder Bot has multiple functions for various endpoints of the VSinder Api. With the `access-token`, `refresh_token` and the `cookie` taken from a network request to the Api, this bot can swipe right on all the people, or as in the example `bot.py` swipe right or left at random.

2. After getting a match, which happens pretty fast, VSinder Bot sends all the users that haven't sent a message a _Hey There :)_.

3. You found love ... great!

## Author

<a align="center" href="https://3n3a.ch">
  <img src="https://avatars1.githubusercontent.com/u/46775561?s=200" alt="The Author" width="200">
</a>