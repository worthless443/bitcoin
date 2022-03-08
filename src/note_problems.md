### Main Issue for compiling

* conflicting `C++` extern with `C` extern
* leveldb namespace not being included nor linked 

*possible culprits -*

`namespace leveldb {...}` defined in the `*.cc` files, for now, can't find a way to include them while compiling.

