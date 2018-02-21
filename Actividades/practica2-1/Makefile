default:
	@make clean
	@make install
	@make run

clean:
	@find . -name \*.pyc -delete
	@clear

install:
	@sudo pip3 install numpy
	@sudo pip3 install pandas

run:
	@python3 app.py