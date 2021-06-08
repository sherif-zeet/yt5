from flask import Flask, request, send_file
from pytube import YouTube
import logging
import sys

"""
Flask YouTube Video Downloader - Python Marketer
https://pythonmarketer.com/2020/10/07/making-a-youtube-video-downloader-with-pythons-flask-and-pytube3-libraries/
"""
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)

@app.route("/")
def youtube_downloader():
    """Render HTML form to accept YouTube URL."""
    html_page = f"""<html>
                    <head>
                    <Title>Youtube Downloader - Online Youtube Video Downloader | YT5</Title>
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"/>
                    <link href="view-source:http://codenow.epizy.com/CSS/socialmedia/style.css" rel="stylesheet"/>
                    <link rel="stylesheet" type="text/css" href="https://yt1s.com/statics/css/style.css?v=1.99">
                    <link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-128x128.png" sizes="128x128">
                    <link rel="alternate" href="https://yt1s.com/en6" hreflang="x-default" /><link rel="alternate" href="https://yt1s.com/en6" hreflang="en" /><link rel="alternate" href="https://yt1s.com/de5" hreflang="de" /><link rel="alternate" href="https://yt1s.com/es6" hreflang="es" /><link rel="alternate" href="https://yt1s.com/fr" hreflang="fr" /><link rel="alternate" href="https://yt1s.com/hi" hreflang="hi" /><link rel="alternate" href="https://yt1s.com/id" hreflang="id" /><link rel="alternate" href="https://yt1s.com/it1" hreflang="it" /><link rel="alternate" href="https://yt1s.com/ja1" hreflang="ja" /><link rel="alternate" href="https://yt1s.com/ko1" hreflang="ko" /><link rel="alternate" href="https://yt1s.com/my1" hreflang="my" /><link rel="alternate" href="https://yt1s.com/ms" hreflang="ms" /><link rel="alternate" href="https://yt1s.com/ph" hreflang="en-PH" /><link rel="alternate" href="https://yt1s.com/pt2" hreflang="pt" /><link rel="alternate" href="https://yt1s.com/ru1" hreflang="ru" /><link rel="alternate" href="https://yt1s.com/th" hreflang="th" /><link rel="alternate" href="https://yt1s.com/tr1" hreflang="tr" /><link rel="alternate" href="https://yt1s.com/vi1" hreflang="vi" /><link rel="alternate" href="https://yt1s.com/zh-cn" hreflang="zh-CN" /><link rel="alternate" href="https://yt1s.com/zh-tw" hreflang="zh-TW" /><link rel="alternate" href="https://yt1s.com/sa1" hreflang="sa" /><link rel="alternate" href="https://yt1s.com/bn" hreflang="bn" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon.png" />
<link rel="apple-touch-icon-precomposed" sizes="57x57" href="https://yt1s.com/statics/image/apple-touch-icon-57x57.png" />
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://yt1s.com/statics/image/apple-touch-icon-114x114.png" />
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://yt1s.com/statics/image/apple-touch-icon-72x72.png" />
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://yt1s.com/statics/image/apple-touch-icon-144x144.png" />
<link rel="apple-touch-icon-precomposed" sizes="60x60" href="https://yt1s.com/statics/image/apple-touch-icon-60x60.png" />
<link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://yt1s.com/statics/image/apple-touch-icon-120x120.png" />
<link rel="apple-touch-icon-precomposed" sizes="76x76" href="https://yt1s.com/statics/image/apple-touch-icon-76x76.png" />
<link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://yt1s.com/statics/image/apple-touch-icon-152x152.png" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-196x196.png" sizes="196x196" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-96x96.png" sizes="96x96" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-32x32.png" sizes="32x32" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-16x16.png" sizes="16x16" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-128x128.png" sizes="128x128" />
                    </head>
                    <body style="font-family: Arial, Helvetica, sans-serif;">
<header>
<div class="main_nav">
<a class="logo" href="https://sherifzeet-yt5-4075.zeet.app/">
<svg xmlns="http://www.w3.org/2000/svg" width="37" height="28" viewBox="0 0 37 28" fill="none" alt="YT1S">
<g clip-path="url(#clip0)">
<path d="M0.413567 5.80249C0.646742 2.9375 2.94402 0.705376 5.81232 0.517162C9.497 0.275378 14.5363 0 18.375 0C22.2137 0 27.253 0.275378 30.9377 0.517162C33.806 0.705375 36.1033 2.9375 36.3364 5.80249C36.5469 8.38873 36.75 11.5252 36.75 14C36.75 16.4748 36.5469 19.6113 36.3364 22.1975C36.1033 25.0625 33.806 27.2946 30.9377 27.4828C27.253 27.7246 22.2137 28 18.375 28C14.5363 28 9.497 27.7246 5.81232 27.4828C2.94402 27.2946 0.646742 25.0625 0.413567 22.1975C0.203079 19.6113 0 16.4748 0 14C0 11.5252 0.203079 8.38873 0.413567 5.80249Z" fill="#FF0000"></path>
<path d="M11.1223 8.18535L8 11.1334L18 21L28 11.1334L24.8777 8.18535L20.1879 12.8132V0H15.8121V12.8132L11.1223 8.18535Z" fill="white"></path>
</g>
<defs>
<clipPath id="clip0">
<rect width="36.75" height="28" fill="white"></rect>
</clipPath>
</defs>
</svg> <span> YT5</span> </a>

</div>
<div id="navbar" class="navbar-collapse">

</div>
</header>
<br><br><br>
                  <center><h1 style="color:#4A474C">Youtube Downloader</h1>
                    <p style="color:#4A474C">Convert and download Youtube videos in MP4 for free</p> </center>
                    <div class="form">
                    <form action="/download_video" method="post">
                    <br><center>
                    <input class="pl-3" type="url" name="URL" aria-label="Search" placeholder="Search or paste Youtube link here" style="width: 500px; height: 50px; border-radius: 50px; outline: red; border:1px solid #4A474C ;" required ></input>
                    <input type="submit" value="Download" style="width: 125px; height: 50px; border-radius: 50px; outline: red; border:1px solid #4A474C ; background: #4A474C; color: white;">
                    </form></div><br><br><br><br>

                    <center><h2 class="title">Youtube Video Downloader</h2></center>
                    <div class="mw70">Download Youtube videos with YT5 YouTube Downloader. By using our downloader you can easily convert YouTube videos to MP4 file... and download them for free - this service works for computers, tablets and mobile devices. The videos are always converted in the highest available quality.</div>
                    <div class="ftco-section center">
<h2 class="title">How to download Youtube video? </h2>
<ul class="listicon liststep">
<li>
<span class="number">1</span>
 <span>Paste YouTube url or enter keywords into the search box.</span>
</li>
<li>
<span class="number">2</span>
<span>Choose output MP4 format you want to convert and click "Download" button.</span>
</li>
<li>
<span class="number">3</span>
<span>Wait until the conversion is completed and download the file. Very easy and fast.</span>
</li>
</ul>
</div>




<center><a class="btn-red mag0" type="button" href="#">Convert now</a></center>






<cneter>
<div class="ftco-section section-left">
<section itemscope="" itemtype="https://schema.org/FAQPage">
<div class="sf_container">
<div class="wrapper">
<div class="sf_faq">
<h3 class="title center">Questions and Answers</h3>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">What is the fastest way to download Youtube videos?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
<ol>
<li>Access the Youtube URL you need to download.</li>
<li>Add "<b>pp</b>" after the word "youtube" then click "Enter". For example: youtube.com/watch?v=1PJIqpLInrw =&gt; youtubePP.com/watch?v=1PJIqpLInrw</li>
<li>Select the file format you wish then click to "Download" button.</li>
</ol> </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">Is there any limit on the amount of downloaded files applied for users?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
No. Our website allows users to convert and download unlimited amount of file and for free. </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">What are the supported video/audio formats?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
We offer a ton of conversion options and allow you to download MP4 format. You can watch video right after that on your device without installing any other software. </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">What are the compatible devices for the conversion?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
We offer the service that is compatible with all PC devices, smart phones and tablets. </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">How to download Youtube video to Android mobile phone?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
<ol>
<li>Access Youtube from your browser or open Youtube app on your Android device; after that, coppy the video URL you wish to download. </li>
<li>Paste the URL into the search box. You also can enter keyword to look for the video you wish. </li>
<li>Select the format you wish to download then tap "Download". After a few seconds, you can download the file.</li>
</ol> </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">Where do the downloaded files get saved?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
Files you've downloaded are automatically saved in the Downloads folder or the "download history" section on your device. </div>
</div>
</div>
</div>
</div>
</div>
</section>
</div>
</center>



<center>
<a href="https://www.facebook.com/profile.php?id=100068549361726" title="facebook" class="fa fa-facebook"></a>
<a href="#" title="twitter" class="fa fa-twitter"></a>
<a href="#" title="linkedin" class="fa fa-linkedin"></a>
<br><br> <hr>
</center>




<footer>
<div class="copyright">

<cneter>yt5.com © Sherif Abdullah Mahmoud 2021</center>
</div>
</footer>


<script>
console.log("Created by : Sherif Abdullah Mahmoud")
</script>

                    </body></html>"""
    return html_page

@app.route("/download_video", methods=["GET","POST"])
def download_video():
    """
    First pytube downloads the file locally in pythonanywhere:
    /home/your_username/video_name.mp4
    Then use Flask's send_file() to download the video
    to the user's Downloads folder.
    """
    try:
        youtube_url = request.form["URL"]
        local_download_path = YouTube(youtube_url).streams[0].download()
        fname = local_download_path.split("//")[-1]
        return send_file(fname, as_attachment=True)
    except:
        logging.exception("Failed download")
        return """<html>
                    <head>
                    <Title>Youtube Downloader - Online Youtube Video Downloader | YT5</Title>
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"/>
                    <link href="view-source:http://codenow.epizy.com/CSS/socialmedia/style.css" rel="stylesheet"/>
                    <link rel="stylesheet" type="text/css" href="https://yt1s.com/statics/css/style.css?v=1.99">
                    <link rel="alternate" href="https://yt1s.com/en6" hreflang="x-default" /><link rel="alternate" href="https://yt1s.com/en6" hreflang="en" /><link rel="alternate" href="https://yt1s.com/de5" hreflang="de" /><link rel="alternate" href="https://yt1s.com/es6" hreflang="es" /><link rel="alternate" href="https://yt1s.com/fr" hreflang="fr" /><link rel="alternate" href="https://yt1s.com/hi" hreflang="hi" /><link rel="alternate" href="https://yt1s.com/id" hreflang="id" /><link rel="alternate" href="https://yt1s.com/it1" hreflang="it" /><link rel="alternate" href="https://yt1s.com/ja1" hreflang="ja" /><link rel="alternate" href="https://yt1s.com/ko1" hreflang="ko" /><link rel="alternate" href="https://yt1s.com/my1" hreflang="my" /><link rel="alternate" href="https://yt1s.com/ms" hreflang="ms" /><link rel="alternate" href="https://yt1s.com/ph" hreflang="en-PH" /><link rel="alternate" href="https://yt1s.com/pt2" hreflang="pt" /><link rel="alternate" href="https://yt1s.com/ru1" hreflang="ru" /><link rel="alternate" href="https://yt1s.com/th" hreflang="th" /><link rel="alternate" href="https://yt1s.com/tr1" hreflang="tr" /><link rel="alternate" href="https://yt1s.com/vi1" hreflang="vi" /><link rel="alternate" href="https://yt1s.com/zh-cn" hreflang="zh-CN" /><link rel="alternate" href="https://yt1s.com/zh-tw" hreflang="zh-TW" /><link rel="alternate" href="https://yt1s.com/sa1" hreflang="sa" /><link rel="alternate" href="https://yt1s.com/bn" hreflang="bn" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon.png" />
<link rel="apple-touch-icon-precomposed" sizes="57x57" href="https://yt1s.com/statics/image/apple-touch-icon-57x57.png" />
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://yt1s.com/statics/image/apple-touch-icon-114x114.png" />
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://yt1s.com/statics/image/apple-touch-icon-72x72.png" />
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://yt1s.com/statics/image/apple-touch-icon-144x144.png" />
<link rel="apple-touch-icon-precomposed" sizes="60x60" href="https://yt1s.com/statics/image/apple-touch-icon-60x60.png" />
<link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://yt1s.com/statics/image/apple-touch-icon-120x120.png" />
<link rel="apple-touch-icon-precomposed" sizes="76x76" href="https://yt1s.com/statics/image/apple-touch-icon-76x76.png" />
<link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://yt1s.com/statics/image/apple-touch-icon-152x152.png" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-196x196.png" sizes="196x196" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-96x96.png" sizes="96x96" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-32x32.png" sizes="32x32" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-16x16.png" sizes="16x16" />
<link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-128x128.png" sizes="128x128" />
             
                    <link rel="icon" type="image/png" href="https://yt1s.com/statics/image/favicon-128x128.png" sizes="128x128">
                    </head>
                    <body style="font-family: Arial, Helvetica, sans-serif;">
<header>
<div class="main_nav">
<a class="logo" href="https://sherifzeet-yt5-4075.zeet.app/">
<svg xmlns="http://www.w3.org/2000/svg" width="37" height="28" viewBox="0 0 37 28" fill="none" alt="YT1S">
<g clip-path="url(#clip0)">
<path d="M0.413567 5.80249C0.646742 2.9375 2.94402 0.705376 5.81232 0.517162C9.497 0.275378 14.5363 0 18.375 0C22.2137 0 27.253 0.275378 30.9377 0.517162C33.806 0.705375 36.1033 2.9375 36.3364 5.80249C36.5469 8.38873 36.75 11.5252 36.75 14C36.75 16.4748 36.5469 19.6113 36.3364 22.1975C36.1033 25.0625 33.806 27.2946 30.9377 27.4828C27.253 27.7246 22.2137 28 18.375 28C14.5363 28 9.497 27.7246 5.81232 27.4828C2.94402 27.2946 0.646742 25.0625 0.413567 22.1975C0.203079 19.6113 0 16.4748 0 14C0 11.5252 0.203079 8.38873 0.413567 5.80249Z" fill="#FF0000"></path>
<path d="M11.1223 8.18535L8 11.1334L18 21L28 11.1334L24.8777 8.18535L20.1879 12.8132V0H15.8121V12.8132L11.1223 8.18535Z" fill="white"></path>
</g>
<defs>
<clipPath id="clip0">
<rect width="36.75" height="28" fill="white"></rect>
</clipPath>
</defs>
</svg> <span> YT5</span> </a>

</div>
<div id="navbar" class="navbar-collapse">

</div>
</header>
<br><br><br>
                  <center><h1 style="color:#4A474C">Youtube Downloader</h1>
                    <p style="color:#4A474C">Convert and download Youtube videos in MP4 for free</p> </center>
                    <div class="form">
                    <form action="/download_video" method="post">
                    <br><center>
                    <input class="pl-3" type="url" name="URL" aria-label="Search" placeholder="Search or paste Youtube link here" style="width: 500px; height: 50px; border-radius: 50px; outline: red; border:1px solid #4A474C ;"  required ></input>
                    <input type="submit" value="Download" style="width: 125px; height: 50px; border-radius: 50px; outline: red; border:1px solid #4A474C ; background: #4A474C; color: white;">
                    </form></div><br><br><br><br>

                    <center><h2 class="title">Youtube Video Downloader</h2></center>
                    <div class="mw70">Download Youtube videos with YT1s YouTube Downloader. By using our downloader you can easily convert YouTube videos to MP3 file... and download them for free - this service works for computers, tablets and mobile devices. The videos are always converted in the highest available quality.</div>
                    <div class="ftco-section center">
<h2 class="title">How to download Youtube video? </h2>
<ul class="listicon liststep">
<li>
<span class="number">1</span>
 <span>Paste YouTube url or enter keywords into the search box.</span>
</li>
<li>
<span class="number">2</span>
<span>Choose output MP4 format you want to convert and click "Download" button.</span>
</li>
<li>
<span class="number">3</span>
<span>Wait until the conversion is completed and download the file. Very easy and fast.</span>
</li>
</ul>
</div>




<center><a class="btn-red mag0" type="button" href="#">Convert now</a></center>






<cneter>
<div class="ftco-section section-left">
<section itemscope="" itemtype="https://schema.org/FAQPage">
<div class="sf_container">
<div class="wrapper">
<div class="sf_faq">
<h3 class="title center">Questions and Answers</h3>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">What is the fastest way to download Youtube videos?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
<ol>
<li>Access the Youtube URL you need to download.</li>
<li>Add "<b>pp</b>" after the word "youtube" then click "Enter". For example: youtube.com/watch?v=1PJIqpLInrw =&gt; youtubePP.com/watch?v=1PJIqpLInrw</li>
<li>Select the file format you wish then click to "Download" button.</li>
</ol> </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">Is there any limit on the amount of downloaded files applied for users?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
No. Our website allows users to convert and download unlimited amount of file and for free. </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">What are the supported video/audio formats?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
We offer a ton of conversion options and allow you to download MP4 format. You can watch video right after that on your device without installing any other software. </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">What are the compatible devices for the conversion?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
We offer the service that is compatible with all PC devices, smart phones and tablets. </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">How to download Youtube video to Android mobile phone?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
<ol>
<li>Access Youtube from your browser or open Youtube app on your Android device; after that, coppy the video URL you wish to download. </li>
<li>Paste the URL into the search box. You also can enter keyword to look for the video you wish. </li>
<li>Select the format you wish to download then tap "Download". After a few seconds, you can download the file.</li>
</ol> </div>
</div>
</div>
<div class="faq_item" itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
<div class="faq_item_title">
<h4 itemprop="name">Where do the downloaded files get saved?</h4>
</div>
<div class="faq_item_content" id="divId" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
<div itemprop="text">
Files you've downloaded are automatically saved in the Downloads folder or the "download history" section on your device. </div>
</div>
</div>
</div>
</div>
</div>
</section>
</div>
</center>



<center>
<a href="https://www.facebook.com/profile.php?id=100068549361726" title="facebook" class="fa fa-facebook"></a>
<a href="#" title="twitter" class="fa fa-twitter"></a>
<a href="#" title="linkedin" class="fa fa-linkedin"></a>
<br><br> <hr>
</center>




<footer>
<div class="copyright">

<cneter>yt5.com © Sherif Abdullah Mahmoud 2021</center>
</div>
</footer>
<script>
console.log("Created by : Sherif Abdullah Mahmoud")
</script>

                    </body></html>"""
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=81)
