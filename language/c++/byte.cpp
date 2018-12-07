#include <iostream>
#include <cstddef>
 
using namespace std;

int main(int argc, char* argv[])
{
    byte myByte{ 2 };
    cout << to_integer<int>(myByte) << endl; // 2

    // A 2-bit left shift
    myByte <<= 2;
    cout << to_integer<int>(myByte) << endl; // 8
 
    // Initialize two new bytes using binary literals.
    byte byte1{ 0b0011 };
    byte byte2{ 0b1010 };
    cout << to_integer<int>(byte1) << endl; // 3
    cout << to_integer<int>(byte2) << endl; // 10
    
    // Bit-wise OR and AND operations
    byte byteOr = byte1 | byte2;
    byte byteAnd = byte1 & byte2;
    cout << to_integer<int>(byteOr) << endl;
    cout << to_integer<int>(byteAnd) << endl; 

    // Compile error
    //
    // byte byte3{ 0b111111001110111 };

// root@99ea4eb101c3:/usr/local/src# g++ -std=c++17 byte.cpp -o byte
// byte.cpp: In function 'int main(int, char**)':
// byte.cpp:27:35: error: narrowing conversion of '32375' from 'int' to 'unsigned char' inside { } [-Wnarrowing]
//      byte byte3{ 0b111111001110111 };

    cout << "byte size: " << sizeof(byte1) << endl;
    return 0;
}