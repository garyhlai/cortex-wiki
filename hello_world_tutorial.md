# Cortex AI Smart Contract Guide

Cortex is the first and currently the only public blockchain capable of executing on-chain AI. This tutorial will lead you through the process of deploying a simple “Hello World” AI Dapp. If you prefer to learn by reading the formal documentation, click here (https://github.com/CortexFoundation/tech-doc).

By the end of this tutorial, you will have learned how to write a simple handwritten digit recognition AI DApp that takes an input image from the user and tells which digit (0-9) is in the image by calling an on-chain AI model on Cortex.

Here's the overall code we're going to write. We will go over it step-by-step below.

### Overall code

```javascript
pragma solidity ^0.4.18;

contract Infer {
    // 1 * 3 * 32 * 32 matrix
    // 1 uint256 = 32 bytes
    // Now we need 1 * 3 * 32 * 32 bytes

    // initiate the variables
    uint256[] public input_data;
    // address of the on-chain model
    address modelAddr = 0x420bD8d2FE73514E9b77fdBc78c0306Fd8a12866;
    uint256 public currentInferResult;

    constructor() public {
        // Math.ceil (how many bytes we need)
        // b/c CVM
        input_data = new uint256[]((1 * 3 * 32 * 32 + 31) >> 5);
    }

    function GenerateRandomInput() public {
        input_data[0] = uint(sha256(now));
        for(uint i = 1; i < input_data.length; ++i) {
          input_data[i] = uint(sha256(input_data[i - 1]));
        }
    }
    // use randomly generated input
    function DigitRecognitionInfer() public {
        uint256[] memory output = new uint256[](uint256((1 * 10 + 31) >> 5));
        inferArray(modelAddr, input_data, output);
        currentInferResult = (output[0] >> (256 - 32)) & ((1 << 32) - 1);
        currentInferResult = currentInferResult % 10;
    }

    // take user input
    function NewDigitRecognitionInfer(uint256[] imgData) public {
        uint256[] memory output = new uint256[](uint256((1 * 10 + 31) >> 5));
        input_data = imgData;
        inferArray(modelAddr, input_data, output);
        currentInferResult = (output[0] >> (256 - 32)) & ((1 << 32) - 1);
        currentInferResult = currentInferResult % 10;
    }
}


```

Example of inferring digit recognition model on Cortex blockchain (model address: **0x420bD8d2FE73514E9b77fdBc78c0306Fd8a12866**).

### Create a contract

```javascript
pragma solidity ^0.4.18;

contract Infer {

}
```

### Add basic variables

```javascript
    uint256[] public input_data;
    address modelAddr = 0x420bD8d2FE73514E9b77fdBc78c0306Fd8a12866;
    uint256 public currentInferResult;
```

### The built-in Infer function

```javascript
// feed data in input_data to model and store the output in infer_output
inferArray(model, input_data, infer_output);
```

### Create our function which calls the Infer function

```javascript
    function DigitRecognitionInfer() public {
        uint256[] memory output = new uint256[](uint256((1 * 10 + 31) >> 5));
        inferArray(modelAddr, input_data, output);
        // big endian little endian
        currentInferResult = (output[0] >> (256 - 32)) & ((1 << 32) - 1);
        currentInferResult = currentInferResult % 10;
        // output will be from 0-9
    }
```

- User need to call the function from remix. Need help deploying this contract and then calling it from testnet. Then need tutorial on how to deploy them to mainnet.
- Example input? 1 _ 3 _ 32 \* 32

red blue green
[[][] []]

32 32
red [ [ row1 ][ row2 ] [ row3 ][ row4 ] ... [ row32 ] ]
blue

- What does output in inferArray mean? Placeholder.
- Is this deployment to testnet or mainnet?
- Why % 10?

Need two things now: 1. how to deploy this contract to testnet and then call it from remix. 2. How to move it to MainNet
