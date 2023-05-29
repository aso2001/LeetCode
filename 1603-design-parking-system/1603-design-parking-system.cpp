class ParkingSystem {
public:
    int arr[3];
    ParkingSystem(int big, int medium, int small) {
        this->arr[0] = big;
        this->arr[1] = medium;
        this->arr[2] = small;
    }
    
    bool addCar(int carType) {
        if (!this->arr[carType - 1]) return false;
        this->arr[carType - 1]--;
        return true;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */