CC=g++
EXE=GCI_Name.o
object=GCI_Name.cpp

main: $(EXE)S
	@$(CC)  $< -o $@
	@./main
EXE: $(object)
	$(CC)  $< -o $@
	
.PHONY: clean main EXE
clean:
	@Secho "clean....."
	-rm *.o main
