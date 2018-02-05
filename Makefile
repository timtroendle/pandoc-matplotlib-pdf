test.png:
	python create_plots.py

test.pdf:
	python create_plots.py

test.docx: test.png test.pdf
	pandoc test.md -t docx -o test.docx
