#!/usr/local/bin/ruby

require 'twitter'
require 'cgi/html'

require './keys.rb'

images = ""
$client.search("#深夜の真剣お絵描き60分一本勝負 -rt", :lang=>"ja", :count=>10).take(10).collect do |tweet|
	images << "<p>"
	images << "#{tweet.user.screen_name}: #{tweet.text}"
	images << "</p>"
	
	if tweet.media? then
		media_urls = tweet.media
	
	media_urls.each do |url|
		image = CGI.new("html4")
		
		images << image.img("#{url.media_uri_https}", "ワンドロ")
	end
	end
end

################### HTML ########################
print "Content-Type: text/html\n\n"

puts <<HTML
<html>
<head>
<title>test</title></head>
<body>

<h1>HELLO</h1>


#{images}


</body>
</html>
HTML