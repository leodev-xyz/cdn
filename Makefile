
build: build-docs

build-docs:
	node docs/yuescript-build.js `find . -name "*.yue"`
	pip3 install lupa
	python3 docs/build.py
	cp _headers out/_headers
