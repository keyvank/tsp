build:
	mdbook build --dest-dir docs

pdf:
	rm -rf build && mkdir build
	cp -r src/* build
	python3 mathjax_conv.py build/*.md
	cd build && pandoc --toc --output=../tsp.pdf *.md --metadata title="The Super Programmer"