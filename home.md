<!-- TITLE: Official Cortex Wiki -->
<!-- SUBTITLE: Your Guide to the AI on Blockchain Ecosystem -->

# Table of Contents
## Cortex Overview
### What is Cortex?
Cortex is the first ever blockchain technology that allows the execution of AI algorithms on the blockchain. Cortex provides an AI platform for developers to upload their models on the blockchain and be incorporated into smart contracts. The MainNet was launched at the end of June, 2019. The whitepaper can be found <a href="https://www.cortexlabs.ai/Cortex_AI_on_Blockchain_EN.pdf">here</a>.

To put it in context, blockchain started with bitcoin, a decentralized digital currency. Then entered Ethereum, which allows programming on top of the blockchain, namely the smart contract. Now Cortex builds on top of Ethereum to enable AI-powered smart contract. 
<img src="/uploads/hiearchy.png" style="width:450px; margin-top: 1%; margin-bottom: 1%; "/>
(The relationship between Cortex, Ethereum, and Bitcoin)

### How does Cortex compare to conventional blockchains like Ethereum?
Right now, conventional blockchains like Ethereum have virtual machines that run on the CPU, which cannot **realistically execute non-trivial AI models.** To incorporate any sort of AI into an Ethereum Dapp, for example, would require running the AI models off-chain, which defeats the purpose of a smart contract. The <a href="https://www.cortexlabs.ai">Cortex team </a> addresses this problem by building a virtual machine that runs on the GPU. This allows AI models to execute directly on the blockchain, enabling **true AI smart contract.** In addition, the CVM is backward-compatible with the EVM, so Ethereum developers can easily migrate their applications onto to the Cortex blockchain and on top of that, incorporate AI models into them.  

### How does Cortex compare to other AI on Blockchain projects?
Cortex is the only project that allows you to run AI programs on the blockchain realistically. 

### How does Cortex enable on-chain AI?
The amount of computation of the AI model exceeds the capabilities of Ethereum's "world computer", so accelerators such as GPUs need to be introduced to speed up the process. 

In today's model inference, there are floating-point numbers and parallel computation parts, which bring uncertainty to the computation results, which is unacceptable when verifying blockchain transactions. The popular quantization method is also not specifically designed to be deterministic. It is therefore necessary to develop an inference engine and a training engine specifically designed for blockchain consensus.

This goal is indeed quite challenging. The main technical difficulties also correspond to the frontier research direction in the Bay Area, including the quantized acceleration method of the deep neural network (DNN) model and the virtualization method adapted to the AI ​​accelerator. The AI industry’s main concern in quantized acceleration research focuses more on speeding up centralized inference and model compression; however, on the blockchain, we need to ensure the deterministic nature of computations. Here, we do not simply use existing frameworks such as Tensorflow, MXNet, or PyTorch, but rather aim to design frameworks optimized for the needs of on-chain inference.

Making engines deterministic has its technical difficulties, considering the cumulative overflow and compatibility with different hardware platforms; we are solving a lot of engineering problems. Only deterministic engines can bring about algorithmic consensus and realize the transparency and immutability of blockchain’s self-verifying mechanism. For example, let’s say an autonomous vehicle got into an accident, the inference for the move that caused the accident must be based on open blockchain consensus to reduce disputes and settle liabilities.

### Why do we want to run AI model on the blockchain?
Running AI model on the blockchain ensures the integrity of the model. 

For example, let’s say a smart contract is programmed to give Amy 100 dollars if the facial recognition model recognizes the person as Amy. If the facial recognition model has to run off-chain, its security would be severely compromised: a hacker can change the model to recognize his own face and thereby steal the 100 dollars from the smart contract. On the other hand, if the execution of the facial recognition model happens on the blockchain, it would be very hard to hack the model.  

With the CVM coupled with the quantization method developed by the Cortex team, running AI on the blockchain has become cost-effective and realistic. The transaction fee is extremely low if the network is not super busy. 

### What does “Decentralized AI Autonomous Ecosystem” mean? How does Cortex decentralize AI?  

To understand this question, we need to first understand the infrastructure of the Cortex blockchain.

We offer a blockchain platform for AI developers to upload their models and for Dapp developers to easily integrate these models in their Dapps (without the hassle of dealing with different protocols of different AI model service providers). A helpful analogy is to think of Cortex as a decentralized eBay for machine learning model API calls, where the sellers are the AI model providers and the buyers are the Dapp developers. Via smart contracts, AI model provider gets a portion of the transaction fee whenever the model is inferred. 

This creates an ecosystem where individual AI developers, not just big corporations, are incentivized to upload their AI models to the blockchain, and Dapp developers have access to the best AI models in the world and have the freedom to choose between them. Hence the decentralization. The competition within the ecosystem between AI model providers will naturally lead to the evolution of better and better AI models. Hence the term “autonomous ecosystem.”

### Sometimes you use the word “AI” and sometimes you use the word “machine learning”, what is the relationship between these two terms?

Machine learning is a subfield of AI and by far the most promising one in helping achieve better artificial intelligence. The basic idea of machine learning is to train machines to certain perform tasks without explicitly programming them. Nowadays, they have been used rather interchangeably due to the dominance of machine learning as a method of aritificial intelligence. 

## Cortex Virtual Machine (CVM)
The Cortex Virtual Machine (CVM), is forked from the Ethereum Virtual Machine (EVM) with added support for AI inference and AI contracts. The CVM is compatible with EVM and capable of running both ethereum smart contracts and AI smart contracts. 
The CVM has two layers: infer instructions and deterministic inference engine. 
Infer instructions allows models to be called in contracts through instruction sets, including Infer (code: 0xc0), InferArray (code: 0xc1). 
The deterministic inference engine is called Synapse or the CVM Executor. It guarantees the consistency of AI inference results in heterogeneous computing environments, without significantly compromising performance or accuracy. Synapse proposes a model-based fixed-point execution framework and a corresponding deterministic machine learning operator library. AI developers can train and quantize their models using MRT to be executable on the CVM. 

## Model Representation Tool (MRT)
MRT, short for Model Representation Tool, is a deterministic quantization framework developed by Cortex that enables model inference in the limited-resource and strictly deterministic environment of blockchain, ushering in a new generation of AI smart contracts. 
MRT is designed to convert floating point models supported by nnvm into fixed-point models executable on the CVM while preventing significant loss of precision. The quantization method reduces the output number field of all layers of the model to INT8 or INT32 to simulate the floating-point network and converts the operators involved in the floating-point operation into integer operators using fuse and rewrite. Quantization ensures no overflow and guarantees the deterministic outcome of the model execution.

## Endorphin
Endorphin in Cortex is similar to Gas in Ethereum. 
To prevent abuse of the Cortex network, a fee is charged for each computational step executed in a transaction. Endorphin is the unit that measures the computational effort required for every transaction made on Cortex. The sender of each transaction is required to include an endorphin limit and an endorphin price. (Transaction fee = endorphin limit * endorphin price) The higher the endorphin price, the more likely and quicker miners will execute and verify the transaction. 
For AI inference, generally speaking, the cost of the endorphin is proportional to the size of the AI model. Cortex also sets an upper bound of 1GB on the parameter size of the model, corresponding to up to about 2 billion Float32 parameters.
Unlike the traditional blockchains where all of the block rewards go to miners, on Cortex, a portion of the block reward goes to the model providers to incentivize them to optimize better models. 

## Storage Layer
Cortex uses a distributed file system based on DHT (Distributed Hash Table) as a storage layer solution to reduce network load and network transmission cost. Storage quota is treated as a resource on the Cortex chain. Each mined block provides a 64K byte storage quota. Users freely bid on the use of storage quota with transaction fees.
AI models and input data are treated as a special type of smart contract on the Cortex chain. Creators need to send a special transaction with a function call to the contract in order to advance its upload progress. Each transaction will increase the file upload progress by 512K bytes, consuming the corresponding storage quota. 
After the completion of the upload phase, the file preparation phase is entered. This phase lasts for 100 blocks (about 25 minutes), and at the end of it, the prepared files enter the mature phase and can be used by AI inference contracts.
The owner is responsible for broadcasting the file to the network to reach the entire distributed file system; otherwise, the network consensus will reject relevant contract calls.  

## Cortex Remix
Cortex Remix is a browser-based compiler and IDE for programming language Solidity. It is based on the Remix IDE. It supports the compilation and deployment of AI smart contracts as well as debugging transactions.
Cortex Remix mainly consists of two functional modules: compilation and deployment. 
The compilation module supports compilation and optimization of AI smart contracts. Complied abi, bytecode, and additional information are also displayed in this module.
The deployment module can help deploy AI smart contracts to the Cortex network with the support of Cortex Wallet, allowing for on-chain inference. 

## Cortex Use Cases
* **DeFi:** credit report, anti-fraud in decentralized exchanges, p2p financing, insurance, cryptocurrency lending
* **Gaming:** AI judge, player agent, NPC, assistant/coaching/education
* **Global Climate Action & Carbon Credit Management and Trading:** collects environmental data and puts on the blockchain for a transparent carbon pricing system
* **AI Governance:** stablecoins based on machine learning, sentiment analysis, decentralized decision making, malicious behavior detection, smart resource allocation
* **Others:** on-chain data mining, facial recognition, recommendation, chatbot, machine translation, voice synthesis, etc.

Games and game AIs (such as Fomo3D or sports betting) are the most likely to be the first mass-market, because they form the shortest closed loop. Fintech blockchain technologies, such as anti-fraud in decentralized exchanges, credit systems, lending and smart investment, will probably be the next biggest market, considering all their data will be stored on the blockchain. In addition, we can realize stablecoin model controlled by AI-model on Cortex, and the on-chain  inference process makes it much more transparent than other stablecoins such as USDT. Furthermore,  decentralized autonomous token distribution, decentralized anonymous advertisement recommendation engine, autonomous driving, native Cortex AI Dapps, and really any mass markets that involve AI will see use cases on Cortex. 

### Specific Use Case Examples 
#### Defi 
For example, a decentralized lending app can run an AI algorithm to determine your interest rate based on your personal credit history. The AI used to analyze your credit score is not a black box, but instead, every step of the AI inference is transparent to prevent discrimination and ensure fairness. 

#### Gaming
CryptoKitties would be much cuter, more life-like, and unique if they incorporated AI. Imagine these kitties moving dynamically and behaving uniquely depending on your personal experience interacting with them. While Ethereum is not able to execute AI models and allow for this user experience, this is something that Cortex can uniquely enable.

#### Insurance
Blockchain finds many use cases in the insurance industry, where immutability, fairness, openness, and transparency are in high demand. AI can help improve underwriting decisions, better manage risks, and prevent fraud. An insurance DAO powered by on-chain AI can bring us better, cheaper, fairer, and less bureaucratic insurance. 

#### Decentralized Uber
Almost every aspect of Uber involves AI, from matching drivers and riders, route optimization, driver onboarding to determining fares. Therefore, if we want to build a decentralized Uber, it is necessary to be able to run AI on the blockchain. 

#### Anti-fake AI
The emergence of deepfakes (AI-manipulated videos that are indistinguishable to the human eye) poses a significant threat to society. Social stability will inevitably suffer if video recordings can simply be dismissed as untrustworthy in court. Anti-fake AI algorithms (algorithms that detect whether a video has been tampered with) will run on the blockchain to ensure their transparency and fairness, especially if there were to be used in court. 

The bullet points and specific examples above are only use cases thought of by the Cortex team alone. It is almost certain that the community will conceive many more and better use cases for AI on the blockchain. After all, rarely anyone thought of the best use cases for the internet today when it was first invented.


## Developing on Cortex
### Where can I get started developing on Cortex?
### What is the process to upload AI models to Cortex?


## Mining

### Mining intro and Spec
Cortex uses Cuckoo Cycle for its proof of work algorithm. 

Cuckoo Cycle is a graph theory-based algorithm that is far less energy-intensive than most other CPU, GPU or ASIC-bound PoW algorithms. The goal is to lower mining requirements, ensuring true decentralization and laying the foundation for future scalability.
The difficulty adjusts dynamically so that on average, a block is produced every 15 seconds, i.e., 15s block time. This rate ensures the synchronization of the system state while preventing double-spend and history alteration unless an attacker possesses more than 51% of the network's mining power.
Mining Minimum Requirements
System: Linux Ubuntu 16.04+
GPU: Nvidia GPU with >=10.7GB GDRAM (1080ti, 2080ti, Titan V, etc.)
Space: 2TB  (the size of the blockchain increases over time)
CUDA version: 9.2+
CUDA driver: 396+
Compiler: Go 1.10+, GCC 5.4+
Other stats
Quota general: 64k per block (model uploading space)
Uploading network bandwidth: 1MB/s
Model mature: 100 blocks
Model size limit: 1GB
TPS: 25.4
Pre-allocation: 149792458
Total reward for mining: 150000000
Total supply: 299792458
Reward: 2.5 per block (half every 4 years)  =  8409600



### What opeartion systems are supported?
Right now the official miner implementation only support Linux. However, developers can look into the <a href="https://github.com/CortexFoundation/PoolMiner">source code</a> and port it to their own operating systems. 

### No support for AMD, only for NVDIA?


### Hardware needed to run a Cortex full node?
A 1060 GPU or even a MX150 GPU laptop is enough. We currently have some nodes running the full node. You can check it out at http://monitor.cortexlabs.ai/table-list


### Does your platform support WASM or is WASM compatible?
WASM compatibility is not the focus of the Cortex MainNet, and WASM programming is not directly supported yet. However, if it turns out to be adopted by the blockchain industry mainstream, we will work to support it. We pay very close attention to Ethereum's progress in this regard.



## Tokenomics 

### What is token swap?

### Current exchanges that have completed the token swap for CTXCs?

As of right now, Bitforex and OKex are the only two exchanges that have completed CTXC token swaps for their users, meaning that the addresses on these exchanges are MainNet addresses. Warning: DO NOT try to send ERC20 CTXCs into a Cortex MainNet address nor send MainNet CTXCs into an ERC20 (Eth) address. If you don’t understand what this means, please reach out to us and we can help explain further. Our suggestions is that if you hold ERC20 CTXCs (bought before the MainNet launch), you carry out a token swap following this guide <a href="https://medium.com/cortexlabs/cortex-mainnet-token-swap-announcement-c06769c40663">here</a>.

### How long does token swap last?
At least a year

### How many CTXCs will be issued?




## Community
### How do you attract developers or companies to develop on Cortex? What moves has Cortex made to encourage developers to come?

We treat attracting developers and companies to Cortex as a system project that integrates improving development environment, maintaining user & developer community, and developing Cortex wallet on various platforms. Above all Cortex prioritizes enhancing the development environment, seeking to create a suite of tools analogous to the development ecological layout of XCode/Android Studio for IOS/Android. 

 As of right now there exists rarely any public chain with similar level of developer-friendliness as Ethereum, and we strive to change this by focusing on two general directions.

First, we guarantee a high degree of compatibility with Ethereum. We allow Ethereum developers to migrate their existing Ethereum Dapp to Cortex at almost zero cost and enhance their Dapps by incorporating AI features. This will drastically lower the cost of learning - developers familiar with Ethereum can start developing on Cortex with very little additional learning.

Second, we will highlight Cortex’s new unique computing environment that activates the AI features for Dapps, something remains to be seen by developers and companies. For the first time, developers will be able to create true AI Dapps such as The Master of Digital Clash by inferring models on the chain. 

In addition to the points already mentioned, from the perspective of development, Cortex is an open-source project that will be constantly evolving in accordance to the preferences of developers that build on them. We provide an web IDE for AI Dapp developers, and for model developers, we offer support for computational power, model libraries, and standardized data sets. Our team will continue to work closely with developers to help implement their technologies in various scenarios. 

From the perspective of operation, we will follow up with Hackathons and challenge bounties, activities closely linked to token incentives. In addition, we realize that developers like to interact with leading industry figures through activities such as AMAs and have included these in our operation plans. 


### What tools will you provide to help developers to develop?
We provide an web IDE for AI Dapp developers, and for model developers, we offer support for computational power, model libraries, and standardized data sets. Our team will continue to work closely with developers to help implement their technologies in various scenarios. 









