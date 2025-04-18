// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DeadManSwitch {
    address public owner;
    uint256 public lastActivationTime;
    uint256 public activationTimeout = 1 weeks;  // Timeout after 1 week of inactivity
    bool public isActive;

    event Activated(address indexed user);
    event TimeoutTriggered(address indexed user);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    constructor() {
        owner = msg.sender;
        lastActivationTime = block.timestamp;
        isActive = true;
    }

    function activateSwitch() public {
        require(isActive, "Dead Man's Switch is not active.");
        lastActivationTime = block.timestamp;
        emit Activated(msg.sender);
    }

    function checkStatus() public view returns (bool) {
        if (block.timestamp > lastActivationTime + activationTimeout) {
            return false;  // Timeout occurred, switch is triggered
        }
        return true;  // Active, owner is alive
    }

    function triggerActionIfInactive() public {
        require(!checkStatus(), "Owner is still active.");
        require(isActive, "Dead Man's Switch is inactive.");
        
        // Perform some action, like sending funds, calling an emergency function, etc.
        emit TimeoutTriggered(owner);

        // Deactivate the switch
        isActive = false;
    }

    function resetSwitch() public onlyOwner {
        isActive = true;
        lastActivationTime = block.timestamp;
    }
}
