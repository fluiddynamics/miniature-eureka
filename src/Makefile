OUT := $(shell python3 get_result_location.py)

hello:
	python3 gen.py > $(OUT)/hello.txt
	mkdir ../docs/result
	cp $(OUT)/hello.txt ../docs/result
