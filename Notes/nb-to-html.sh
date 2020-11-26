#!/bin/sh
# For automated conversion of notebooks into html

for eachNB in *.ipynb; do
    jupyter nbconvert --to html $eachNB
done

echo "---" > index.md
echo "title: Neural Networks" >> index.md
echo "description: A collection of deep learning resources, neural networks and data science demos" >> index.md
echo "show_downloads: true" >> index.md
echo "---" >> index.md
echo "# Neural Networks and Deep Learning Notes" >> index.md
echo "" >> index.md
for eachHTMLFile in *.html; do
    if test $eachHTMLFile != index.html; then
        filename=$(echo $eachHTMLFile | sed 's/\.html//g' | sed 's/[0-9]-[A-Z]-//g')
        echo "[$filename]($eachHTMLFile)" >> index.md
        echo "" >> index.md
    fi
done
