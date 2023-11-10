pdf:
	pandoc --toc --output=out.pdf *.md
	pdfunite cover.pdf out.pdf tsp.pdf
	pdftotext tsp.pdf - | wc -w
	firefox tsp.pdf