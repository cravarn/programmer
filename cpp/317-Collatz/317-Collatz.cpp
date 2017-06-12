#include<iostream>
#include<string>
using namespace std;

void generate_collatz(String input) {
  String arules = "bc", brules = "a", crules = "aaa", append;

  while (input.compare("a") != 0) {
    if (input[0] == 'a')
      append = arules;
    else if (input[0] == 'b')
      append = brules;
    else
      append = crules;

  input = input.substr(1, string::npos)
  cout<<input;
  }
}


int main()
{
  String input;

  cout<<"Enter the input string";
  cin>>input;

  generate_collatz(input);

  return 0;
}
