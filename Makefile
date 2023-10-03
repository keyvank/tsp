pdf:
	pandoc --toc --output=out.pdf *.md
	pdfunite cover.pdf out.pdf tsp.pdf
	firefox tsp.pdf