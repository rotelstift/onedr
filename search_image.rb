$images = ""
$tweet_urls_with_images = ""

$client.search("#深夜の真剣お絵描き60分一本勝負 -rt", :lang=>"ja", :count=>20).take(100).shuffle.collect do |tweet|
		if tweet.media? then
			media_urls = tweet.media
			tweet_urls = tweet.uri
	
			media_urls.each do |url|
				$images << "\"#{url.media_uri_https}\","
				$tweet_urls_with_images << "\"#{tweet_urls}\","
				#$images << "<div><img src=\"#{url.media_uri_https}\" height=\"80%\"/></div>"
			end
		end
	end


