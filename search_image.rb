$images = ""
$tweet_urls_with_images = ""

$client.search("\##{$text}"+" -rt", :lang=>"ja", :count=>20,  :filter=>"images").take(100).shuffle.collect do |tweet|
		if tweet.media? then
			media_urls = tweet.media
			tweet_urls = tweet.uri
	
			media_urls.each do |url|
				$images << "\"#{url.media_uri_https}\","
				$tweet_urls_with_images << "\"#{tweet_urls}\","
			end
		end
	end


