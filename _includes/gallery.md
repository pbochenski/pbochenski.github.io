<ul id="media" class="clearfix justified-gallery">

  {% for image in site.gallery reversed %}
      <div
        class="albumList"
        data-sub-html=""
        data-download-url="{{image.large}}"
        data-src="{{image.large}}"
        data-exthumbimage="{{image.thumb}}"
        data-filename="{{image.name}}"
      >
        <a href="{{image.large}}">
          <img src="{{image.small}}" height="300" />
        </a>
      </div>
  {% endfor %}
</ul>
