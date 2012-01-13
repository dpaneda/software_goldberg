rube_goldberg: tunnel goodbye

tunnel: tunnel.go
	6g tunnel.go
	6l -o tunnel tunnel.6
	@rm -f tunnel.6

goodbye: goodbye.hs
	ghc --make goodbye.hs
	@rm -f goodbye.o goodbye.hi

go:
	./rube.sh go

clean:
	@rm -f tunnel	goodbye
