#!/usr/local/bin/ruby

require 'twitter'
require 'cgi/html'

require './keys.rb'
require './search_image.rb'


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
	body {
		background-color : #000000;
	}
	.content {
	   margin : 50px;
	   background-color : #1D6CAB;
	   border: solid 1px #000000;
	   height : 80%;
	}
	.slider {
	   margin : 50px;
	}
	.slick-list {
		height: 80%;
	}
	img {
		padding: 0px 150px;
		//height: 600px;
	}
	--> 
	</style>
</head>
<body>


<h1 style="text-align:center; color: #fff">#深夜の真剣お絵描き60分一本勝負</h1>
<div class="content">
    <div class="slider autoplay center single-item add-remove">
		
    </div>
</div>



<script type="text/javascript" src="jquery-1.11.2.min.js"></script>
  <script type="text/javascript" src="slick/slick.min.js"></script>
<script type="text/javascript">
$(function() {
  var array = [
  	#{$images}
  ];
  var l = array.length;
  for (i = 0; i<l; i++) {
	    //var r = Math.floor(Math.random()*l);
    	var imgurl = array[i];
    	$('.autoplay').append('<img src="'+imgurl+'" />');
    	//$("img.randomimg"+i).attr({"src":imgurl});
  }
    	
 $('.autoplay').slick({
    centerMode: true,
    variableWidth: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    lazyLoad: 'ondemand',
  });
    	/*
  setInterval( function (){
  	for (i = 1; i<=5; i++) {
	    var r = Math.floor(Math.random()*l);
    	var imgurl = array[r];
    	$("img.randomimg"+i).attr({"src":imgurl});
    }
    },10000);*/
    
    
  
});
</script>
</body>
</html>
HTML