$images = ""

$client.search("#深夜の真剣お絵描き60分一本勝負 -rt", :lang=>"ja", :count=>20).take(100).collect do |tweet|
		if tweet.media? then
			media_urls = tweet.media
	
			media_urls.each do |url|
				$images << "\"#{url.media_uri_https}\","
				#$images << "<div><img src=\"#{url.media_uri_https}\" height=\"80%\"/></div>"
			end
		end
	end


