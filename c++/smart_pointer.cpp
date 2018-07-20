#include <iostream>
#include <memory>
#include <vector>

class Point
{
    public: 
        Point(int in_x, int in_y) { x = in_x; y = in_y; }
        void print();
    
    private:
        int x, y;
};

void Point::print()
{
    std::cout << "x:" << x << " y:" << y << std::endl;
}

void sample()
{
    // $valgrind --leak-check=full ./smart_pointer
    //
    // ==459== HEAP SUMMARY:
    // ==459==     in use at exit: 8 bytes in 1 blocks
    // ==459==   total heap usage: 11 allocs, 10 frees, 73,896 bytes allocated
    // ==459==
    // ==459== 8 bytes in 1 blocks are definitely lost in loss record 1 of 1
    // ==459==    at 0x4C3017F: operator new(unsigned long) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    // ==459==    by 0x1092CA: sample() (smart_pointer.cpp:24)
    // ==459==    by 0x1093EF: main (smart_pointer.cpp:35)
    // ==459==
    auto a = new Point(1,2);    

    // smart pointer for prevention memory leak
    // std::shared_ptr is therefore a reference counting smart pointer.
    //     
    auto a2 = std::make_shared<Point>(5,5);
    std::shared_ptr<Point> a3(new Point(6,6));

    a->print();
    a2->print();
    a3->print();
}

int main(int argc, char* argv[])
{
    sample();
 
    auto b = std::make_shared<Point>(-1,2);
    std::shared_ptr<Point> b2(new Point(4,3));

    std::vector<std::shared_ptr<Point>> pointList;
    pointList.push_back(b);
    pointList.push_back(b2);

    return 0;
}