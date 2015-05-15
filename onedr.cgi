#!/usr/local/bin/ruby

require 'twitter'
require 'cgi/html'

require './keys.rb'

images = ""
$client.search("#深夜の真剣お絵描き60分一本勝負 -rt", :lang=>"ja", :count=>20).take(20).collect do |tweet|
	#images << "<p>"
	#images << "#{tweet.user.screen_name}: #{tweet.text}"
	#images << "</p>"
	
	if tweet.media? then
		media_urls = tweet.media
	
		media_urls.each do |url|
		
#			images << image.img("#{url.media_uri_https}", "ワンドロ")
			images << "<div><img src=\"#{url.media_uri_https}\" height=\"80%\"/></div>"
		end
	end
end

################### HTML ########################
print "Content-Type: text/html\n\n"

puts <<HTML
<html>
<head>
<title>test</title>

<link rel="stylesheet" type="text/css" href="slick/slick.css"/>
<link rel="stylesheet" type="text/css" href="slick/slick-theme.css"/>
<style type="text/css">
	<!--
	.content {
	   margin : 50px;
	   background-color : #1D6CAB;
	   border: solid 1px #000000;
	}
	.slider {
	   margin : 50px;
	}
	img {
		padding: 10px 150px;
	}
	--> 
	</style>
</head>
<body>


<h1 style="text-align:center;">#深夜の真剣お絵描き60分一本勝負</h1>
<div class="content">
    <div class="slider autoplay center single-item">
		#{images}
    </div>
</div>



<script type="text/javascript" src="jquery-1.11.2.min.js"></script>
  <script type="text/javascript" src="slick/slick.min.js"></script>
<script type="text/javascript">
$(function() {
    $('.autoplay').slick({
  centerMode: true,
  variableWidth: true,
  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
});
});
</script>
</body>
</html>
HTML