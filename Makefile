all: tunnel.go
	6g tunnel.go
	6l -o tunnel tunnel.6
	@rm -f tunnel.6

start:
	./read_tweet.py &
	./tunnel &

stop:
	pkill -f read_tweet
	pkill -f tunnel

clean:
	@rm -f tunnel	
