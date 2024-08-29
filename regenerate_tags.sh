rm -fr ./tag
rm -fr ./_site
bundle exec jekyll build
cp -r ./_site/tag ./tag