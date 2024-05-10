// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

void solveR(vector<bool>& room, int numSteps) {
    int position = room.size() / 2; // Start in the middle of the room

    for (int step = 0; step < numSteps; ++step) {
        // Clean the current position if it's dirty
        if (room[position]) {
            room[position] = false;
            cout << "Cleaned position " << position << endl;
        }

        // Check if there are adjacent dirty positions
        if (position > 0 && room[position - 1]) {
            // Move left if the position to the left is dirty
            position--;
        } else if (position < room.size() - 1 && room[position + 1]) {
            // Move right if the position to the right is dirty
            position++;
        } else {
            // If no adjacent dirty positions, move randomly
            position += rand() % 2 == 0 ? -1 : 1;
        }
    }
}


int main() {
    // Write C++ code here
    int roomSize=10;
    int numSteps=5;
    
    //room with random dirty squares
    vector<bool> room(roomSize,false);
    for(int i=0;i<roomSize;i++){
        room[i]=rand()%2==0; //50% chance of being dirty
    }
    
    //iniital room state
    cout<<"Initial room state: "<<endl;
    for(int i=0;i<roomSize;i++){
        cout<<(room[i] ? " D ":" C "); //if room exists in room array then Dirty else clean
    }
    cout<<endl;
    
    //clean room
    solveR(room,numSteps);
    
    //final room state
    cout<<"Final room state: "<<endl;
    for(int i=0;i<roomSize;i++){
        cout<<(room[i] ? " D ":" C ");
    }
    cout<<endl;
    
    
    return 0;
}
