<ul id="media" class="clearfix justified-gallery">

  {% for number in (1..75) reversed %}
    {% assign padded = number | prepend: '000' | slice: -3, 3 %}
      <div
        class="albumList"
        data-sub-html=""
        data-download-url="media/large/{{padded}}.jpg"
        data-src="media/large/{{padded}}.jpg"
        data-exthumbimage="media/thumbs/{{padded}}.jpg"
        data-filename="{{padded}}.jpg"
      >
        <a href="media/large/{{padded}}.jpg">
          <img src="media/small/{{padded}}.jpg" height="300" />
        </a>
      </div>
  {% endfor %}
</ul>
