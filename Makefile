build:
	mdbook build --dest-dir docs

epub:
	rm -rf build && mkdir build
	cp -r src/* build
	python3 mathjax_conv.py build/*.md
	cd build && pandoc --toc --output=../out.epub *.md --metadata title="The Super Programmer"