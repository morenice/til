#include <iostream>
#include <string_view>

// function that accepts a string, use an std::string_view as parameter type. 
//  - string_view is that it will never copy a string.
//  - string_view is a read-only view of a string 
//    it doesn't offer replace method.
void printStringView(std::string_view strView)
{
    std::cout << strView;    
    if (strView.size() >=4)
    {
        std::cout << " (Substring: " << strView.substr(1,3) << ")";
    }
    std::cout << std::endl;
}

int main()
{
    // std::string_view
    // 
    // Basically, a string_view just contains a pointer to a string, and its length. 
    // No need to use an std::string_view reference.
    // A string_view is very cheap to copy, so it’s perfectly fine to pass by value. 
    
    std::string sampleStr1 = "std::string cheap string copy";
    const char* sampleStr2 = "const char*";

    printStringView(sampleStr1);
    printStringView(sampleStr2);
    return 0;
}