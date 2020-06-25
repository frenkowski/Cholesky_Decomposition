CC = g++
CXXFLAGS = -DNDEBUG -O3


ifeq ($(UNAME),Windows)
LIBS = -lpsapi
endif

Progetto_1.exe: Progetto_1.o
	g++ $(CXXFLAGS) $< -o $@

Progetto_1.o: Progetto_1.cpp
	g++ $(CXXFLAGS) -c $< -o $@ $(LIBS)

.PHONY: clean

clean:
	rm *.exe *.o
	