magick convert $1 -resize 120x120  media/thumbs/$1
magick convert $1 -resize "300^>"  media/small/$1
magick convert $1 -resize "1000^>" media/large/$1