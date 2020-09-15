all: build push

build:
	docker build -t nickick/stellaris-ethos-origin-bot .
push: 
	docker push nickick/stellaris-ethos-origin-bot
