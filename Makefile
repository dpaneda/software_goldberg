all: tunnel.go
	6g tunnel.go
	6l -o tunnel tunnel.6
	@rm -f tunnel.6

go:
	./rube.sh go

clean:
	@rm -f tunnel	
