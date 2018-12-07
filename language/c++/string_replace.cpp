#include <iostream>
#include <boost/algorithm/string/replace.hpp>


void boostReplaceSample() 
{
    // 1. replace all    
    std::string str1 = "Template $some$";

    std::cout << "= boost replace_all =" << str1 << std::endl;

    std::cout << "before: " << str1 << std::endl;
    boost::replace_all(str1, "$some$", "engine");
    std::cout << "after: " << str1 << std::endl;
    std::cout << std::endl;

    // 2. replace all copy
    const std::string str2 = "Template $some$";

    std::cout << "= boost replace_all_copy =" << str1 << std::endl;

    std::cout << "before: " << str2 << std::endl;
    std::string copiedStr2 = boost::replace_all_copy(str2, "$some$", "engine");
    std::cout << "after: " << str2 << std::endl;
    std::cout << "after(copied): " << copiedStr2 << std::endl;
}

int main() 
{
    boostReplaceSample();
}