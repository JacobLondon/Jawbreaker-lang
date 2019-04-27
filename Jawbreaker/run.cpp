#include <stdlib.h>
#include <string>

int main(int argc, char* argv[]) {

    std::string args = "\"python jawbreaker.py";
    for(int i = 0; i < argc; i++) {
        args.append(" ");
        args.append(argv[i]);
    }
    args.append("\"");

    system(args.c_str());

    return 0;
}