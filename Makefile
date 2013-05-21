rube_goldberg: tunnel goodbye

tunnel: tunnel.go
	8g tunnel.go
	8l -o tunnel tunnel.8
	@rm -f tunnel.8

goodbye: goodbye.hs
	ghc --make goodbye.hs
	@rm -f goodbye.o goodbye.hi

go: rube_goldberg
	./rube.sh go

clean:
	@rm -f tunnel	goodbye
