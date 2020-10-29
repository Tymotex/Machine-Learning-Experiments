#!/bin/sh
# For automated conversion of notebooks into html

for eachNB in *.ipynb; do
    jupyter nbconvert --to html $eachNB
done

echo "<h1>Quick Links</h1>" > index.html
for eachHTMLFile in *.html; do
    if test $eachHTMLFile != index.html; then
        echo "<a href=\"$eachHTMLFile\">$eachHTMLFile</a>" >> index.html
    fi
done
