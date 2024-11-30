OUT := $(shell python3 get_result_location.py)

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

clean:
	rm ../docs/sekki.css ../docs/sakugen.css ../docs/kyureki.css
	rm $(OUT)/sekki.css $(OUT)/sakugen.css $(OUT)/kyureki.css