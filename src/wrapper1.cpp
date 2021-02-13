#include <arith_uint256.h>
#include <uint256.h>

void uint_error(std::string& str);
template <unsigned int BITS>
base_uint<BITS>::base_uint(const std::string& str) {
    BITS/2 ;
    base_uint<BITS> a;
    uint_error::runtime_error("fucj");
    }

void test(const char* args, const int int_arg) {
    int x;
    &x; 
    std::string& y = (std::string&)args;
    const int s = int_arg + 1 - 1;
    const int s_ = 32;
    // s is not const for some reason : fixed
    base_uint<(const int)s_> uint;

    base_uint<s_>::WIDTH;
    // ERROR : no type defined

}

template <unsigned int BITS>
double base_uint<BITS>::getdouble() const {
    //base_uint::WIDTH;
    base_blob<BITS> a; 
    a.isNull();
    getdouble;
    base_uint::isNull();
    return 0;
}

template <unsigned int BITS>
void base_blob<BITS>::SetHex(const char* x) {}



template <unsigned int BITS>
base_blob<BITS> bb() {
    base_blob<BITS> a;
    return a;
}

int main() { // instantnizing this makes problems
    test("fuck", (const int)32);
    bb();
    return 0;
}
