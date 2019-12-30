CC = g++

exe = GCI_Name.o
object = GCI_Name.cpp

main: $(exe)S
	@$(CC)  $< -o $@
	@./main
exe: $(object)
	$(CC)  $< -o $@
	
.PHONY: clean main exe
clean:
	@Secho "Clean..."
	-rm *.o main
