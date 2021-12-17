#include <iostream>
#include <string>
using namespace std;
int win_positions[8][3] {{1,2,3}, {4,5,6}, {7,8,9}, {1,4,7}, {2,5,8}, {3,6,9}, {1,5,9}, {3,5,7}};
string board_with_numbers[3][3] = {{"1","2","3"}, {"4","5","6"}, {"7","8","9"}};
string board[3][3] = {{".",".","."}, {".",".","."}, {".",".","."}};
string players[2] = {"X", "O"};
string winner = "";
int in_move, _move;

void print_2d(string __array[][3]) {
    for(int i=0; i<3; i++) {
        cout<<"|";
        for(int j=0; j<3; j++) {
            cout<<__array[i][j]<<"|";
        }
        cout<<endl;
    }
}

string check_winner(string __board[3][3]) {
    for(int i=0; i<8; i++) {
        int count = 0;
        string temp="";
        for (int j=0; j<3; j++) {
            if (temp != "") {
                if (__board[(win_positions[i][j]-1)/3][(win_positions[i][j]-1)%3] != temp && 
                    __board[(win_positions[i][j]-1)/3][(win_positions[i][j]-1)%3] != ".") {
                    count = 0;
                    break;
                }
                else if (__board[(win_positions[i][j]-1)/3][(win_positions[i][j]-1)%3] != ".") {
                    count++;
                }
            }
            else {
                temp = __board[(win_positions[i][j]-1)/3][(win_positions[i][j]-1)%3];
                count++;
            }
        }
        if(count == 3) {
            return temp;
        }
    }
    return "";
}

void make_move(string __board[3][3], int _to, string _who) {
    if(__board[(_to-1)/3][(_to-1)%3] != "X" && __board[(_to-1)/3][(_to-1)%3] != "O" && _to<=9) {__board[(_to-1)/3][(_to-1)%3] = _who; _move++;}
    else cout<<"This cell is occupied"<<endl;
}

int main(int argc, char const *argv[])
{
    cout<<"Tic tac toe"<<endl;
    cout<<"To make a move enter number of the cell"<<endl;
    print_2d(board_with_numbers);
    while(_move<9) {
        winner = check_winner(board);
        if(winner != "") break;
        cin>>in_move;
        make_move(board, in_move, players[_move%2]);
        print_2d(board);
        winner = check_winner(board);
    }
    if(winner != "") cout<<winner<<" Won!";
    else cout<<"It's a tie!";
    return 0;
}
