pdf:
	pandoc --output=out.pdf *.md
	pdfunite cover.pdf out.pdf tsp.pdf