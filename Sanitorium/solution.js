function solution(A) {
    // Log the input array for debugging purposes
    console.log("Input array:", A);
    
    // Sort the array in descending order to prioritize larger groups
    A.sort((a, b) => b - a);
    // Log the sorted array to verify the sorting step
    console.log("Sorted array:", A);
    
    // Initialize the minimum number of rooms needed to 0
    let minRooms = 0;
    // Initialize the current room size counter to 0
    let currentRoomSize = 0;
    
    // Iterate through each element in the sorted array
    for (let i = 0; i < A.length; i++) {
        // Check if the current room can accommodate the current group
        if (currentRoomSize >= A[i]) {
            // Increment the room count since the current room is full
            minRooms++;
            // Reset the current room size for the next group
            currentRoomSize = 0;
        }
        // Increment the current room size counter
        currentRoomSize++;
    }
    
    // If there are any groups left that have not been assigned to a room
    if (currentRoomSize > 0) {
        // Increment the room count for the remaining groups
        minRooms++;
    }
    
    // Log the minimum number of rooms required for debugging
    console.log("Minimum number of rooms:", minRooms);
    // Return the calculated minimum number of rooms needed
    return minRooms;
}

console.log(solution([1, 1, 1, 1, 1])); 
console.log(solution([2, 1, 4])); 
console.log(solution([2, 7, 2, 9, 8])); 
console.log(solution([7, 3, 1, 1, 4, 5, 4, 9])); 