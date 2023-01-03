
<div style="text-align: center">2023</div>

<ul id="y2023" class="clearfix justified-gallery">

  {% for image in site.gallery reversed %}
    {% assign year = image.date | date: "%Y" %}
    {% if year == "2023" %}
      <div
        class="albumList"
        data-sub-html=""
        data-download-url="{{image.large}}"
        data-src="{{image.large}}"
        data-exthumbimage="{{image.thumb}}"
        data-filename="{{image.name}}"
      >
        <a href="{{image.large}}">
          <img alt="{{image.name}}" src="{{image.small}}" height="300" />
        </a>
      </div>
    {% endif %}
  {% endfor %}
</ul>

<div style="text-align: center">2022</div>
<ul id="y2022" class="clearfix justified-gallery">

  {% for image in site.gallery reversed %}
    {% assign year = image.date | date: "%Y" %}
    {% if year == "2022" %}
      <div
        class="albumList"
        data-sub-html=""
        data-download-url="{{image.large}}"
        data-src="{{image.large}}"
        data-exthumbimage="{{image.thumb}}"
        data-filename="{{image.name}}"
      >
        <a href="{{image.large}}">
          <img alt="{{image.name}}" src="{{image.small}}" height="300" />
        </a>
      </div>
    {% endif %}
  {% endfor %}
</ul>

<div style="text-align: center">2021</div>
<ul id="y2021" class="clearfix justified-gallery">
  {% for image in site.gallery reversed %}
    {% assign year = image.date | date: "%Y" %}
    {% if year == "2021" %}
      <div
        class="albumList"
        data-sub-html=""
        data-download-url="{{image.large}}"
        data-src="{{image.large}}"
        data-exthumbimage="{{image.thumb}}"
        data-filename="{{image.name}}"
      >
        <a href="{{image.large}}">
          <img alt="{{image.name}}" src="{{image.small}}" height="300" />
        </a>
      </div>
    {% endif %}
  {% endfor %}
</ul>

<div style="text-align: center">2020</div>
<ul id="y2020" class="clearfix justified-gallery">
  {% for image in site.gallery reversed %}
    {% assign year = image.date | date: "%Y" %}
    {% if year == "2020" %}
      <div
        class="albumList"
        data-sub-html=""
        data-download-url="{{image.large}}"
        data-src="{{image.large}}"
        data-exthumbimage="{{image.thumb}}"
        data-filename="{{image.name}}"
      >
        <a href="{{image.large}}">
          <img alt="{{image.name}}" src="{{image.small}}" height="300" />
        </a>
      </div>
    {% endif %}
  {% endfor %}
</ul>

<div style="text-align: center">2019</div>
<ul id="y2019" class="clearfix justified-gallery">
  {% for image in site.gallery reversed %}
    {% assign year = image.date | date: "%Y" %}
    {% if year == "2019" %}
      <div
        class="albumList"
        data-sub-html=""
        data-download-url="{{image.large}}"
        data-src="{{image.large}}"
        data-exthumbimage="{{image.thumb}}"
        data-filename="{{image.name}}"
      >
        <a href="{{image.large}}">
          <img alt="{{image.name}}" src="{{image.small}}" height="300" />
        </a>
      </div>
    {% endif %}
  {% endfor %}
</ul>
