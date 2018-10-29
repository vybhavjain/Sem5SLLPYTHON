<html>
<body>
<table id="cars table">
<tr ><th>Cars</th></tr>
<tr onmouseover="when_hover(this.id);" id="0" ><th >Ford Fiesta</th></tr>
<tr onmouseover="when_hover(this.id);" id="1"><th >BMW Bake</th></tr>
<tr onmouseover="when_hover(this.id);" id="2"><th >Honda City</th></tr>
</table>
<p id="c_name"></p>
<p id="c_price"></p>
<p id="c_brand"></p>
<img id="c_img" src="">

<script>
function when_hover(id)
{
var j=[{"name":"Ford Fiesta", "price": "100" , "brand":"ford","url":"https://media.zigcdn.com/media/model/2017/Nov/ecosport-right_320x160.jpg"},
		{"name":"BMW Bake", "price": "150" , "brand":"BMW","url":"https://www.drivespark.com/car-image/640x480x100/car/300x225x22841640-bmw_x1.jpg.pagespeed.ic.1xSZoZDjj-.jpg"},
		{"name":"Honda City", "price": "200" , "brand":"Honda","url":"https://stimg.cardekho.com/images/carexteriorimages/360x240/Honda/Honda-Brio/047.jpg"}];

var name=document.getElementById("c_name");
var price=document.getElementById("c_price");
var brand=document.getElementById("c_brand");
var image=document.getElementById("c_img");

name.innerHTML="Car Name : "+j[id]["name"];
price.innerHTML="Car Price : "+j[id]["price"];
brand.innerHTML="Car Brand : "+j[id]["brand"];
image.src=innerHTML=j[id]["url"];
}
</script>
</body>
</html>
