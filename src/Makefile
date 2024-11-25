OUT := $(shell python3 get_result_location.py)

hello:
	python3 gen.py > $(OUT)/hello.txt
	mkdir ../docs/result
	cp $(OUT)/hello.txt ../docs/result

$(OUT)/sekki.css: gen_css.py sekki.py
	python3 gen_css.py sekki > $@

$(OUT)/sakugen.css: gen_css.py sakugen.py
	python3 gen_css.py sakugen > $@

$(OUT)/kyureki.css: gen_css.py kyureki.py
	python3 gen_css.py kyureki > $@

all: $(OUT)/sekki.css $(OUT)/sakugen.css $(OUT)/kyureki.css

copy: all
	cp $(OUT)/sekki.css $(OUT)/sakugen.css $(OUT)/kyureki.css ../docs

freeze:
	pip3 freeze > requirements.txt
