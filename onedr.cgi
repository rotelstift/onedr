#!/usr/local/bin/ruby

require 'twitter'
require 'cgi/html'

require './keys.rb'



################### HTML ########################
print "Content-Type: text/html\n\n"

puts "<html>"
puts "<head><title>test</title></head>"
puts "<body>"

puts "<h1>HELLO</h1>"


$client.search("#深夜の真剣お絵描き60分一本勝負 -rt", :lang=>"ja", :count=>10).take(10).collect do |tweet|
	puts "<p>"
	puts "#{tweet.user.screen_name}: #{tweet.text}"
	puts "</p>"
	
	if tweet.media? then
		media_urls = tweet.media
	
	media_urls.each do |url|
		image = CGI.new("html4")
		
		puts image.img("#{url.media_uri_https}", "ワンドロ")
	end
	end
end


puts "</body>"
puts "</html>"