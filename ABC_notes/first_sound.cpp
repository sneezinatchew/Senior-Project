#include <iostream>
#include <windows.h>
using namespace std;

int main() {
	bool played = PlaySound(LPCWSTR("test.wav"), NULL, SND_ASYNC);
	cout << played << endl;
	return 0;
}
