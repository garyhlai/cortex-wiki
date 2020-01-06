IDE link: cerebro.cortexlabs.ai/remix/

# Cortex AI Smart Contract Guide

Cortex is the first and currently the only public blockchain capable of executing on-chain AI. This tutorial will lead you through the process of deploying a simple “Hello World” AI Dapp. If you prefer to learn by reading the formal documentation, click here (https://github.com/CortexFoundation/tech-doc).

By the end of this tutorial, you will have learned how to write a simple handwritten digit recognition AI DApp that takes an input image from the user and tells which digit (0-9) is in the image by calling an on-chain AI model on Cortex.

Here's the overall code we're going to write - always refer back to it if you get lost. We will go over it step-by-step next.

### Overall code

```javascript
pragma solidity ^0.4.18;

contract Infer {

    // initiate the variables
    uint256[] public input_data;
    // address of the on-chain model
    address modelAddr = 0x420bD8d2FE73514E9b77fdBc78c0306Fd8a12866;
    // the output will be stored in this variable
    uint256 public currentInferResult;

    constructor() public {
        // Here we define the dimension of the input_data. To feed an image input of dimension 1 * 3 * 32 * 32 into the model, we need 1 * 3 * 32 * 32 bytes. Now, each uint256 in Solidity is 32 bytes. That's why we need divide 1 * 3 * 32 * 32 by 32 and round up. To express this division in Solidity, we write (1 * 3 * 32 * 32 + 31) >> 5, where >> 5 means divide by 2^5 and adding the 31 allows us to effectively round up.
        input_data = new uint256[]((1 * 3 * 32 * 32 + 31) >> 5);
    }

    // you can choose to randomly generate input as opposed to taking the input image from the user
    function GenerateRandomInput() public {
        input_data[0] = uint(sha256(now));
        for(uint i = 1; i < input_data.length; ++i) {
          input_data[i] = uint(sha256(input_data[i - 1]));
        }
    }
    // recognize digit using randomly generated input image
   function DigitRecognitionInfer() public {
        uint256[] memory output = new uint256[](1);
        inferArray(modelAddr, input_data, output);
        currentInferResult = (output[0] >> (256 - 32)) & ((1 << 32) - 1);
        currentInferResult = currentInferResult % 10;
    }

    // recognize digit using user input image
   function NewDigitRecognitionInfer(uint256[] imgData) public {
        uint256[] memory output = new uint256[](1);
        inferArray(modelAddr, imgData, output);
        currentInferResult = (output[0] >> (256 - 32)) & ((1 << 32) - 1);
        currentInferResult = currentInferResult % 10;
    }

    function NewDigitRecognitionInferView(uint256[] imgData) uint256 public view {
        uint256[] memory output = new uint256[](1);
        inferArray(modelAddr, imgData, output);
        ret = (output[0] >> (256 - 32)) & ((1 << 32) - 1);
        ret = ret % 10;
        return ret;
    }

}


```

Let's begin to walk through the code step-by-step. Pay close attention to the comments.

### Create a contract

```javascript
pragma solidity ^0.4.18;

contract Infer {

}
```

### Initiate basic variables

```javascript
    // The image input is in the form of a matrix (a uint256 array) of pixels, which has dimension 1 * 3 * 32 * 32. If you're confused why this is the dimension of the input image, see footnotes.
    uint256[] public input_data;
    // The address of an exisitng on-chain AI model you will call to recognize the digit in the image. If you prefer to use your own digit recognition model, you can upload it to Cortex storage layer first and then substitute this address.
    address modelAddr = 0x420bD8d2FE73514E9b77fdBc78c0306Fd8a12866;
    // This variable will store the output of the AI inference.
    uint256 public currentInferResult;
```

### Write the main function to call the AI model

Pay attention. This is the most important function in this contract. It takes an input image array of dimension 1 x 3 x 32 x 32 and return a number from 0-9 as the output, telling you which digit is in the image.

```javascript
    // recognize digit using user input image
   function NewDigitRecognitionInfer(uint256[] imgData) public {
        uint256[] memory output = new uint256[](1);
        // inferArray is a built-in function in CVM, it takes the input "imgData", feed it to this model at "modelAddr" and store the inference result in "output", which you pass in as a placeholder at first
        inferArray(modelAddr, imgData, output);

        // These two lines below will convert the output into a digit between 0-9 and store it in "currentInferResult". (The conversion has to do with big endian vs. little endian under the hood)
        currentInferResult = (output[0] >> (256 - 32)) & ((1 << 32) - 1);
        currentInferResult = currentInferResult % 10;
    }
```

And we're done! You can deploy this contract to the TestNet and then use it to recognize a handwritten digit now!

Notice we did not go over the _GenerateRandomInput()_ and _DigitRecognitionInfer()_ funcitons, because they are not essential. All you need to know is that _GenerateRandomInput()_ will randomly generate an input image and store it in the variable _input_data_ and _DigitRecognitionInfer()_ will call the AI model to recognize which digit is in that randomly generated input image. Not too useful but you can use them to test whether your contract is working properly.

### Fotenotes: image dimension

**Question:** Why is the image 1 x 3 x 32 x 32 ?

**Answer:**

1: 1 image

3: 3 colors in RBG - red, blue, green (each can take on a value from 0 to 255). Varying combinations of RBG can get you different colors. In total, there's 256 x 256 x 256 color combinations.

32: 32 rows of pixels

32: 32 columns of pixels

Visualize one such array as

[

red [ [ row1 ],[ row2 ],[ row3 ],[ row4 ]... [ row32 ] ]

blue [ [ row1 ],[ row2 ],[ row3 ],[ row4 ]... [ row32 ] ]

green [ [ row1 ],[ row2 ],[ row3 ],[ row4 ]... [ row32 ] ]

]

where [ row1 ] looks like [ [col1],[col2],[col3],[col4]...[col32]] and within each of [col1] lives a value from 0-255, indicating how much red/green/blue it has in that pixel.

---

### Questions

- Big endian vs. Little endian handling in currentInferResult. How to adapt it for other input size?

- Can the model handle other image dimensions? How/Where exactly can we get the pixel matrix of an image?

- NewDigitRecognitionInferView vs. NewDigitRecognitionInfer?

This is what allows your users to call your model and recognize the digit in their input image. There are two types of calls in blockchain: transaction or call. The former changes the state of the blockchain is verified by network consensus (all computers in the network verifies the change to the state). The latter doesn't change the state of the blockchain; instead, it simply returns you the result of the program as executed by a nearby computer in the network. NewDigitRecognitionInferView is the latter whereas NewDigitRecognitionInfer is the former. If you want your call to the program to be recorded on the blockchain, you should use NewDigitRecognitionInfer; otherwise, you should just use NewDigitRecognitionInferView.

- User need to call the function from remix.

To deploy this contract

Open remix, activate the two modules on the side.

To call this contract, click on the buttons on the left

Three things left now:

\*1. How can users (someone other than the owner of the contract) call this function from remix?

2. Can we take user input image? (Fix the compiler) Where can we get such input image? Can we use input image of other dimensions?
3. How to move it to MainNet?
