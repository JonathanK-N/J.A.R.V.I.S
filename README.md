<h1 align="center">J.A.R.V.I.S </h1> 

<div align="center">
  
[![Welcome to my profile](https://img.shields.io/badge/Hello,Devs!-Welcome-blue.svg?style=flat&logo=github)](https://github.com/gauravsingh9356/J.A.R.V.I.S)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/gauravsingh9356/J.A.R.V.I.S)
 [![GitHub issues](https://img.shields.io/github/issues/GauravSingh9356/J.A.R.V.I.S)](https://github.com/GauravSingh9356/J.A.R.V.I.S/issues)
![Stars](https://img.shields.io/github/stars/gauravsingh9356/J.A.R.V.I.S?style=flat&logo=github)
![Forks](https://img.shields.io/github/forks/gauravsingh9356/J.A.R.V.I.S?style=flat&logo=github)
[![GitHub license](https://img.shields.io/github/license/GauravSingh9356/J.A.R.V.I.S)](https://github.com/GauravSingh9356/J.A.R.V.I.S/blob/master/LICENSE)
  
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

  </div>



<img src="jarvis1.jpg"/>

### Requirements:

<li>datetime</li>
<li>os</li>
<li> pyttsx3</li>
<li> wikipedia</li>
<li> speech_recognition </li>
<li> webbrowser</li>
<li> sys</li>
<li> smtplib</li>
<li>requests</li>
<li>json</li>
<li>difflib</li>
<li>geocoder</li>
<li>pyjokes</li>
<li>psutil</li>
<li> pyautogui</li>
<li> opencv</li>

<h2>Required Packages</h2>

```
pip install -r requirements.txt
```

> _On **Windows**, download a matching wheel for [`PyAudio`](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually before the rest of the requirements._
```bash
pip install PyAudio-0.2.14-cp<version>-cp<version>m-win_amd<architecture>.whl
```

### On Ubuntu based Linux distribution you need to install the following packages so that the code works:

```
sudo apt-get update && sudo apt-get install espeak portaudio19-dev python3-pyaudio

```

The dependency list was verified on **Ubuntu 22.04** and **Windows 10** with Python 3.8.
### Environment Variables

Set the following variables in your shell or `.env` file before running J.A.R.V.I.S:

- `EMAIL_USER` – email address used for sending mails
- `EMAIL_PASS` – password or app token for `EMAIL_USER`
- `NEWS_API_KEY` – API key for the news service
- `CHROME_PATH` – optional path to the Chrome executable
- `TESSERACT_CMD` – optional path to the Tesseract OCR executable
- `MUSIC_FILE` – optional path of the mp3 file used when the "play music" command is triggered
- `SCREENSHOT_PATH` – optional file destination for screenshots (defaults to `screenshot.png`)


### What it does...

  <ul>
   <li>Dynamic Authentication using Optical Face Recognition</li>
<li>Send emails</li>
  <li>Dynamic News Reporting at any time with api integration</li>
  <li>Todo list generator, Yes it remembers all!</li> 
<li>Open any website with just a voice command</li>
<li>Plays Music</li>
<li>Tells time</li>
<li>Wikipedia powered AI</li>
<li>Dictionary with Intelligent Sensing i.e. auto checking if spell mistake</li>
<li>Weather Report such as temp, wind speed, humidity, weather description</li>
<li>Latitude and longitude</li>
 <li>YouTube searching</li> 
 <li>Google Map searching</a>
 <li>YouTube Downloader, download any youtube video by just putting url of video</li>
 <li>Now Master can switch b/w J.A.R.V.I.S and F.R.I.D.A.Y, switch to female voice assistant</li>
</ul>

<table>
  <tr>
    <td><img src="images/Screenshot%20(138).png"/></td>
      <td><img src="https://github.com/GauravSingh9356/J.A.R.V.I.S/blob/master/images/face-600x900.png"/></td>
    

</tr>
<tr>
<td><img src="images/email.jpg"/></td>
<td><img src="https://github.com/GauravSingh9356/J.A.R.V.I.S/blob/master/images/maxresdefault.jpg"/></td>
</tr>
<td><img src="https://github.com/GauravSingh9356/J.A.R.V.I.S/blob/master/images/4-Best-Weather-Forecast-APIs-for-Development-of-Weather-Apps-624x304.jpeg"/></td>
  <td><img src="https://github.com/GauravSingh9356/J.A.R.V.I.S/blob/master/images/maxresdefault%20(1).jpg"/></td>
</tr>
<tr>
  <td><img src="canny.jpg"/>
          </td>
  <td><img src="ImgContor.jpg"/>
          </td>
</tr>
</table>

## Some Sneak peeks:

<ul>
  <li><h2> Jarvis, Are you there?</h2></li>
  <li><h2> At your service, Sir</h2></li>
  
  <li><h2> Jarvis, What are today's news headlines? can you tell?</h2></li>
  <li><h2>Ofcourse, Sir -> Then news headlines   Would you like to visit the news url?</h2></li>
  
  <li><h2> Search Youtube</h2></li>
  <li><h2>What you want to search, Sir</h2></li>
  <li><h2>Coding for kids</h2></li>
  <li><h2> Opens youtube in browser with desired search query results </h2></li>
  
   <li><h2> Jarvis, Can you send email to Gaurav?</h2></li>
  <li><h2>What I say sir, Sir</h2></li>
   <li><h2>Gaurav is a good boy</h2></li>
  <li><h2> Email is sent successfully, Sir</h2></li>
  
  # And so on....
  
<a href="https://techtalkswithgaurav.blogspot.com/2020/06/your-personal-assistant-jarvis.html" target="_blank">Read complete blog article</a>

## Contribution:
Thank you for your interest in contributing to our Repo! Pull requests are welcome. For fixing typos, please make a PR with your fixes. We are happy for every contribution.
A lot can be done with this project. Core AI chatbot like functionality can be added. More python scripts can be associated. Pull requests for any such changes are accepted. Feel free to fork this project and make your own changes too.

## Docker

Build the image:
```bash
docker build -t jarvis .
```

Run the container:
```bash
docker run --rm -it jarvis
```
